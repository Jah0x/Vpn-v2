# Vpn-v2

Backend API and Telegram bot for VPN subscriptions.

This repository contains a small FastAPI backend and a Telegram bot skeleton.
Configuration is handled via environment variables.

## Development

Create a virtual environment and install requirements:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn backend.app.main:app --reload
```

Run the bot:

```bash
python bot/main.py
```

## Configuration

Set the following environment variables before running the services:

- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD` – SMTP server credentials
  used to send notification emails.
- `JWT_SECRET` – secret key for JWT token generation.
- `BOT_TOKEN` – Telegram bot token from BotFather.

## Repository Structure

```
backend/      # FastAPI application code
bot/          # Telegram bot implementation
requirements.txt
```

## Tests

Run the tests with:

```bash
pytest
```
