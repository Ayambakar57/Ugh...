from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    """Schema for user login"""
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")


class TokenResponse(BaseModel):
    """Schema for token response"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    """Schema for refresh token request"""
    refresh_token: str = Field(..., description="Refresh token")


class RegisterRequest(BaseModel):
    """Schema for user registration"""
    code_id: str = Field(..., description="User code ID")
    full_name: str = Field(..., description="Full name")
    username: str = Field(..., min_length=3, description="Username (min 3 characters)")
    password: str = Field(..., min_length=6, description="Password (min 6 characters)")


class ChangePasswordRequest(BaseModel):
    """Schema for changing password"""
    old_password: str = Field(..., description="Current password")
    new_password: str = Field(..., min_length=6, description="New password (min 6 characters)")
