"""User models used by the API."""

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """Data required to create a new user account."""

    email: EmailStr
    password: str


class User(BaseModel):
    """Public representation of a user profile."""

    id: int
    email: EmailStr
    telegram_id: int | None = None
