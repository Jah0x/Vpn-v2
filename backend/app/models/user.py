 vava94-codex/следовать-файлу-read-me
"""User models used by the API."""


from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
 vava94-codex/следовать-файлу-read-me
    """Data required to create a new user account."""


    email: EmailStr
    password: str


class User(BaseModel):
 vava94-codex/следовать-файлу-read-me
    """Public representation of a user profile."""


    id: int
    email: EmailStr
    telegram_id: int | None = None
