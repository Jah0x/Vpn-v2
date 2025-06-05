"""Authentication routes for user management."""

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import EmailStr

from ..models.user import UserCreate, User
from ..services import token
from ..auth import LDAPClient

router = APIRouter()
ldap_client = LDAPClient()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# In-memory store for demo purposes
fake_users: dict[str, dict[str, str]] = {}


def get_password_hash(password: str) -> str:
    """Return a bcrypt hash of the given password."""

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check that the plaintext password matches the stored hash."""

    return pwd_context.verify(plain_password, hashed_password)


@router.post("/register", response_model=User)
async def register(user: UserCreate) -> User:
    """Create a new user with an email and password."""

    if user.email in fake_users:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed = get_password_hash(user.password)
    user_id = len(fake_users) + 1
    fake_users[user.email] = {
        "id": user_id,
        "email": user.email,
        "password": hashed,
        "telegram_id": None,
    }
    ldap_client.create_user(str(user_id), user.email, hashed)
    # TODO: send registration email
    return User(id=user_id, email=user.email)


@router.post("/link-telegram", response_model=User)
async def link_telegram(email: EmailStr, telegram_id: int) -> User:
    """Link a Telegram account to an existing user."""

    stored = fake_users.get(email)
    if not stored:
        raise HTTPException(status_code=404, detail="User not found")
    stored["telegram_id"] = telegram_id
    # TODO: send notification email
    return User(id=stored["id"], email=stored["email"], telegram_id=telegram_id)


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> dict[str, str]:
    """Authenticate a user and return a JWT token."""

    stored = fake_users.get(form_data.username)
    if not stored or not verify_password(form_data.password, stored["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access = token.create_access_token({"sub": stored["id"]})
    return {"access_token": access, "token_type": "bearer"}


@router.post("/login/telegram")
async def login_telegram(telegram_id: int, password: str) -> dict[str, str]:
    """Login using Telegram ID and password."""

    stored = next(
        (u for u in fake_users.values() if u.get("telegram_id") == telegram_id),
        None,
    )
    if not stored or not verify_password(password, stored["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access = token.create_access_token({"sub": stored["id"]})
    return {"access_token": access, "token_type": "bearer"}


@router.post("/set-password", response_model=User)
async def set_password(email: EmailStr, password: str) -> User:
    """Set or update password for a user (e.g., after Telegram login)."""

    stored = fake_users.get(email)
    if not stored:
        raise HTTPException(status_code=404, detail="User not found")
    stored["password"] = get_password_hash(password)
    return User(id=stored["id"], email=stored["email"], telegram_id=stored.get("telegram_id"))


def get_current_user(token_str: str = Depends(token.oauth2_scheme)) -> User:
    """Return the currently authenticated user based on JWT."""

    payload = token.decode_access_token(token_str)
    user_id = str(payload.get("sub"))
    stored = next((u for u in fake_users.values() if str(u["id"]) == user_id), None)
    if not stored:
        raise HTTPException(status_code=401, detail="Invalid token")
    return User(id=stored["id"], email=stored["email"], telegram_id=stored.get("telegram_id"))


@router.get("/me", response_model=User)
async def me(current_user: User = Depends(get_current_user)) -> User:
    """Return the currently authenticated user."""

    return current_user
