from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_validator
from typing import Optional, Union
from enum import Enum
from uuid import UUID

class UserCreate(BaseModel):
    first_name: str = Field(min_length=3, max_length=50, description="The first name of the user")
    last_name: str = Field(min_length=3, max_length=50, description="The last name of the user")
    email: EmailStr = Field(max_length=120, description="The email address of the user")
    photo: Optional[str] = Field(None, max_length=200, description="A URL to the user's profile photo")
    password: str = Field(min_length=8, max_length=200, description="The password for the user account")
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        # Implement password validation logic here (e.g., check for complexity)
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for char in value):
            raise ValueError("Password must contain at least one special character")
        return value
    
class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    photo: Optional[str] = None

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    message: str
    data: Optional[Union[UserOut, list[UserOut]]] = None
    
class UserLogin(BaseModel):
    email: EmailStr = Field(max_length=120, description="The email address of the user")
    password: str = Field(min_length=8, max_length=200, description="The password for the user account")
    
class UserLoginResponse(BaseModel):
    message: str