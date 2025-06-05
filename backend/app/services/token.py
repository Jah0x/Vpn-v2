"""JWT token creation and validation helpers."""

import os
from datetime import datetime, timedelta
from typing import Any

import jwt

SECRET_KEY = os.environ.get("JWT_SECRET", "secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    """Generate a JWT access token for the given payload."""

    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> dict[str, Any]:
    """Decode and validate a JWT access token."""

    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
