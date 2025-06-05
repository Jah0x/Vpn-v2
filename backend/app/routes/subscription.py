"""Subscription management endpoints."""

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/active")
async def get_active_subscription() -> dict[str, str | None]:
    """Return active subscription details if present."""

    # TODO: query subscription service / database
    return {"subscription": None}


@router.get("/config/{format}")
async def get_config(format: str) -> dict[str, str]:
    """Return configuration in the requested format."""

    # TODO: generate configuration
    if format not in {"vless", "vmess", "json", "qr"}:
        raise HTTPException(status_code=400, detail="Unsupported format")
    return {"config": f"dummy-{format}"}


@router.post("/activate")
async def activate_subscription(key: str) -> dict[str, str]:
    """Activate subscription by key."""

    # TODO: activation logic
    return {"status": "activated"}


@router.get("/user/status")
async def user_status() -> dict[str, str]:
    """Return subscription status and limits."""

    # TODO: fetch status from subscription service
    return {"status": "inactive"}
