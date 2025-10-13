"""
FastAPI Dependencies Module
Centralized dependencies for authentication and authorization.
"""
from typing import Optional, Dict, Any
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.crud.user import crud_user
from app.models.user import User


# OAuth2 scheme for token authentication
# tokenUrl points to the login endpoint for Swagger UI "Authorize" button
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token.
    
    Args:
        data: Dictionary containing user data (typically {"sub": user_id})
        expires_delta: Optional custom expiration time
    
    Returns:
        Encoded JWT token string
    
    Note:
        - Default expiry: 15 minutes (or ACCESS_TOKEN_EXPIRE_MINUTES from settings)
        - Token type is marked as "access" in payload
        - TODO: Ensure SECRET_KEY is strong and stored in environment variables
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({
        "exp": expire,
        "type": "access"
    })
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT refresh token.
    
    Args:
        data: Dictionary containing user data (typically {"sub": user_id})
        expires_delta: Optional custom expiration time
    
    Returns:
        Encoded JWT token string
    
    Note:
        - Default expiry: 7 days (or REFRESH_TOKEN_EXPIRE_DAYS from settings)
        - Token type is marked as "refresh" in payload
        - TODO: Consider storing refresh tokens in DB for revocation capability
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    
    to_encode.update({
        "exp": expire,
        "type": "refresh"
    })
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_token(token: str, token_type: str = "access") -> Optional[Dict[str, Any]]:
    """
    Verify and decode a JWT token.
    
    Args:
        token: JWT token string
        token_type: Expected token type ("access" or "refresh")
    
    Returns:
        Decoded payload dictionary if valid, None otherwise
    
    Note:
        - Validates token signature, expiration, and type
        - Returns None on any validation failure
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        
        # Verify token type
        if payload.get("type") != token_type:
            return None
        
        return payload
    except JWTError:
        return None


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """
    FastAPI dependency to get the current authenticated user.
    
    This dependency:
    1. Extracts the JWT token from Authorization header
    2. Validates the token (signature, expiration, type)
    3. Retrieves the user from database
    4. Returns the User object
    
    Args:
        token: JWT access token from Authorization header (auto-extracted)
        db: Database session dependency
    
    Returns:
        Authenticated User object
    
    Raises:
        HTTPException 401: If token is invalid, expired, or user not found
    
    Usage:
        @router.get("/protected")
        async def protected_route(current_user: User = Depends(get_current_user)):
            return {"user_id": current_user.id}
    
    Note:
        - TODO: Consider adding user status checks (e.g., is_active, is_verified)
        - TODO: Add rate limiting for security
        - This is async-compatible for use with async route handlers
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Verify the access token
    payload = verify_token(token, token_type="access")
    if payload is None:
        raise credentials_exception
    
    # Extract user ID from token payload
    user_id: str = payload.get("sub")
    if user_id is None:
        raise credentials_exception
    
    # TODO: Fetch user from database
    # Ensure your User model and crud_user.get() method exist
    user = crud_user.get(db, id=user_id)
    if user is None:
        raise credentials_exception
    
    # TODO: Optional - check if user is active/enabled
    # if not user.is_active:
    #     raise HTTPException(status_code=400, detail="Inactive user")
    
    return user


# Optional: Additional dependencies for role-based access control
def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Optional dependency to check if user is active.
    Extend this for role-based access control.
    """
    # TODO: Implement if you have an is_active field
    # if not current_user.is_active:
    #     raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
