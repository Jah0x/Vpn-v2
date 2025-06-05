"""API endpoints used by the Telegram bot."""

from fastapi import APIRouter

router = APIRouter()


@router.post("/user/{telegram_id}/status")
async def get_user_status(telegram_id: int) -> dict[str, str]:
    """Return subscription status for a Telegram user."""

    # TODO: integrate with user/subscription services
    return {"status": "unknown"}


@router.post("/user/{telegram_id}/set-password")
async def bot_set_password(telegram_id: int, password: str) -> dict[str, str]:
    """Allow the bot to set a password for a user."""

    # TODO: update password in user store
    return {"status": "password-updated"}
