from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    code_id: str
    full_name: str
    username: str


class UserCreate(UserBase):
    password: str  # Plain password that will be hashed


class UserUpdate(BaseModel):
    code_id: Optional[str] = None
    full_name: Optional[str] = None
    username: Optional[str] = None
    enc_password: Optional[str] = None
    last_login_at: Optional[datetime] = None


class UserResponse(UserBase):
    id: UUID
    last_login_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
