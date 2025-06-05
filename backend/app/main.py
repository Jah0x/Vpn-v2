 vava94-codex/следовать-файлу-read-me
"""FastAPI application setup for the VPN backend."""

from fastapi import FastAPI

from .routes import auth, subscription, bot_api


app = FastAPI(title="VPN v2 Backend")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
 vava94-codex/следовать-файлу-read-me
app.include_router(subscription.router, prefix="/subscription", tags=["subscription"])
app.include_router(bot_api.router, prefix="/bot", tags=["bot"])


@app.get("/")
async def root() -> dict[str, str]:
    """Health check endpoint returning API status."""


    return {"status": "ok"}
