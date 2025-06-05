# Vpn-v2

Backend API and Telegram bot for VPN subscriptions.

This repository contains a small FastAPI backend and a Telegram bot skeleton.
Configuration is handled via environment variables. See the list below for
required settings.

## Development

Create a virtual environment and install requirements:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the backend during development:

```bash
uvicorn backend.app.main:app --reload
```

Run the bot in polling mode:

```bash
python bot/main.py
```

## Configuration

Set the following environment variables before running the services:

- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD` – SMTP server credentials
  used to send notification emails.
- `JWT_SECRET` – secret key for JWT token generation.
- `GLAUTH_HOST`, `GLAUTH_PORT`, `GLAUTH_BIND_DN`, `GLAUTH_BIND_PASSWORD`,
  `GLAUTH_BASE_DN` – connection details for the GLAuth LDAP server.
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

## API Overview

`/auth` — маршруты для регистрации и авторизации пользователей:

- `POST /auth/register`
- `POST /auth/link-telegram`
- `POST /auth/login`
- `POST /auth/login/telegram`
- `POST /auth/set-password`
- `GET /auth/me`

`/subscription` — работа с подписками:

- `GET /subscription/active`
- `GET /subscription/config/{format}`
- `POST /subscription/activate`
- `GET /subscription/user/status`

`/bot` — взаимодействие с телеграм-ботом:

- `POST /bot/user/{telegram_id}/status`
- `POST /bot/user/{telegram_id}/set-password`

## Development Log

Лог изменений и заметки по разработке хранятся в файле `docs/DEVLOG.md`.
