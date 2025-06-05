"""FastAPI application setup for the VPN backend."""

from fastapi import FastAPI

from .routes import auth

app = FastAPI(title="VPN v2 Backend")

app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/")
async def root() -> dict[str, str]:
    """Health check endpoint returning API status."""

    return {"status": "ok"}
