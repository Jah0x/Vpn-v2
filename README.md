# Vpn-v2

Backend API and Telegram bot for VPN subscriptions.

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
