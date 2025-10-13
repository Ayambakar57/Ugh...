# Authentication System Documentation

## Overview

This authentication system provides secure user authentication using JWT (JSON Web Tokens) with access and refresh tokens. Passwords are hashed using **Argon2**, one of the most secure password hashing algorithms.

## Features

- **User Registration**: Create new user accounts with secure password hashing
- **Login**: Authenticate users and receive JWT tokens
- **Access Token**: Short-lived token (30 minutes) for accessing protected endpoints
- **Refresh Token**: Long-lived token (7 days) for getting new access tokens
- **Password Change**: Secure password update functionality
- **Protected Routes**: Use dependency injection to protect endpoints

## Security

- **Password Hashing**: Argon2 (via `argon2-cffi` and `passlib`)
- **Token Type**: JWT (JSON Web Tokens) via `python-jose`
- **Token Types**: Separate access and refresh tokens with different lifetimes
- **Token Validation**: Automatic validation of token type and expiration

## Configuration

Update your `.env` file with the following settings:

```env
SECRET_KEY=your-secret-key-here-generate-a-strong-random-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

## API Endpoints

### 1. Register New User

**Endpoint**: `POST /api/auth/register`

**Request Body**:
```json
{
  "code_id": "USR001",
  "full_name": "John Doe",
  "username": "johndoe",
  "password": "securepassword123"
}
```

**Response** (201 Created):
```json
{
  "id": "uuid-here",
  "code_id": "USR001",
  "full_name": "John Doe",
  "username": "johndoe",
  "last_login_at": null,
  "created_at": "2025-10-11T02:00:00Z",
  "updated_at": "2025-10-11T02:00:00Z"
}
```

**Notes**:
- Password must be at least 6 characters
- Username must be at least 3 characters and unique
- Password is automatically hashed using Argon2

---

### 2. Login

**Endpoint**: `POST /api/auth/login`

**Request Body**:
```json
{
  "username": "johndoe",
  "password": "securepassword123"
}
```

**Response** (200 OK):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Notes**:
- Updates the user's `last_login_at` timestamp
- Returns both access and refresh tokens
- Access token expires in 30 minutes
- Refresh token expires in 7 days

---

### 3. Refresh Access Token

**Endpoint**: `POST /api/auth/refresh`

**Request Body**:
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response** (200 OK):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Notes**:
- Use when access token expires
- Returns new access token and new refresh token
- Old refresh token becomes invalid

---

### 4. Get Current User

**Endpoint**: `GET /api/auth/me`

**Headers**:
```
Authorization: Bearer <access_token>
```

**Response** (200 OK):
```json
{
  "id": "uuid-here",
  "code_id": "USR001",
  "full_name": "John Doe",
  "username": "johndoe",
  "last_login_at": "2025-10-11T02:00:00Z",
  "created_at": "2025-10-11T01:00:00Z",
  "updated_at": "2025-10-11T02:00:00Z"
}
```

**Notes**:
- Requires valid access token
- Returns current authenticated user information

---

### 5. Change Password

**Endpoint**: `POST /api/auth/change-password`

**Headers**:
```
Authorization: Bearer <access_token>
```

**Request Body**:
```json
{
  "old_password": "securepassword123",
  "new_password": "newsecurepassword456"
}
```

**Response** (200 OK):
```json
{
  "message": "Password changed successfully"
}
```

**Notes**:
- Requires valid access token
- Validates old password before updating
- New password must be at least 6 characters
- New password is hashed using Argon2

---

## Using Authentication in Your Code

### Protecting Endpoints

To protect an endpoint and require authentication, use the `get_current_user` dependency:

```python
from fastapi import APIRouter, Depends
from app.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/protected-endpoint")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {
        "message": "This is a protected endpoint",
        "user": current_user.username
    }
```

### Example: Protected Company Creation

```python
from fastapi import APIRouter, Depends
from app.auth import get_current_user
from app.models.user import User
from app.schemas.company import CompanyCreate, CompanyResponse

@router.post("/api/companies", response_model=CompanyResponse)
def create_company(
    company: CompanyCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Only authenticated users can create companies
    # current_user contains the authenticated user
    new_company = crud_company.create(db, obj_in=company)
    return new_company
```

## Client-Side Usage

### JavaScript/TypeScript Example

```javascript
// 1. Login
const loginResponse = await fetch('http://localhost:8000/api/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    username: 'johndoe',
    password: 'securepassword123'
  })
});

const { access_token, refresh_token } = await loginResponse.json();

// Store tokens (e.g., in localStorage or secure storage)
localStorage.setItem('access_token', access_token);
localStorage.setItem('refresh_token', refresh_token);

// 2. Access protected endpoint
const response = await fetch('http://localhost:8000/api/auth/me', {
  headers: {
    'Authorization': `Bearer ${localStorage.getItem('access_token')}`
  }
});

const userData = await response.json();

// 3. Refresh token when access token expires
if (response.status === 401) {
  const refreshResponse = await fetch('http://localhost:8000/api/auth/refresh', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      refresh_token: localStorage.getItem('refresh_token')
    })
  });
  
  const newTokens = await refreshResponse.json();
  localStorage.setItem('access_token', newTokens.access_token);
  localStorage.setItem('refresh_token', newTokens.refresh_token);
}
```

## Error Responses

### 401 Unauthorized
```json
{
  "detail": "Could not validate credentials"
}
```

### 400 Bad Request
```json
{
  "detail": "Username already registered"
}
```

### 404 Not Found
```json
{
  "detail": "User not found"
}
```

## Token Structure

### Access Token Payload
```json
{
  "sub": "user-uuid",
  "type": "access",
  "exp": 1696982400
}
```

### Refresh Token Payload
```json
{
  "sub": "user-uuid",
  "type": "refresh",
  "exp": 1697587200
}
```

## Security Best Practices

1. **Never commit your SECRET_KEY**: Keep it in `.env` file and add `.env` to `.gitignore`
2. **Use HTTPS in production**: JWT tokens should always be transmitted over HTTPS
3. **Store tokens securely**: Use httpOnly cookies or secure storage on the client side
4. **Implement token rotation**: The refresh endpoint provides new tokens each time
5. **Set appropriate token lifetimes**: Balance security and user experience
6. **Validate tokens on every request**: FastAPI dependency injection handles this automatically

## Files Created/Modified

### New Files:
- `app/auth.py` - Authentication utilities (password hashing, JWT creation/validation)
- `app/schemas/auth.py` - Authentication request/response schemas
- `app/routers/auth.py` - Authentication endpoints

### Modified Files:
- `app/config.py` - Added `REFRESH_TOKEN_EXPIRE_DAYS`
- `app/crud/user.py` - Added `get_by_username()` method
- `app/schemas/user.py` - Changed `UserCreate` to use plain `password` field
- `app/routers/user.py` - Updated to hash passwords when creating users
- `main.py` - Added auth router

## Testing with cURL

### Register
```bash
curl -X POST "http://localhost:8000/api/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "code_id": "USR001",
    "full_name": "John Doe",
    "username": "johndoe",
    "password": "securepass123"
  }'
```

### Login
```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepass123"
  }'
```

### Get Current User
```bash
curl -X GET "http://localhost:8000/api/auth/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Dependencies Used

- **passlib[argon2]** - Password hashing with Argon2
- **python-jose[cryptography]** - JWT token creation and validation
- **fastapi.security.OAuth2PasswordBearer** - OAuth2 password flow

All dependencies are already installed in your `requirements.txt`.
