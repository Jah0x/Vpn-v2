"""Authentication routes for user management."""

from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from pydantic import EmailStr

from ..models.user import UserCreate, User

router = APIRouter()

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
    fake_users[user.email] = {"id": user_id, "email": user.email, "password": hashed}
    # TODO: send registration email
    return User(id=user_id, email=user.email)


@router.post("/login", response_model=User)
async def login(email: EmailStr, password: str) -> User:
    """Authenticate a user and return the profile."""

    stored = fake_users.get(email)
    if not stored or not verify_password(password, stored["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # TODO: issue JWT token
    return User(id=stored["id"], email=stored["email"])
