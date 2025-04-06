# 🔗 InviteLinkBot™

A powerful Telegram bot that automatically generates, revokes, and refreshes invite links for your channels and groups. It also updates a pinned message with clickable HTML links and sends you the latest invite links every 10 minutes.

---

## 🚀 Features

- Auto-generate new invite links
- Auto-revoke old invite links
- Auto-update pinned message in a main channel
- Admin-only alerts for every link refresh
- Emoji-tagged channel titles
- Fully hardcoded — no `.env` or `channels.json` needed
- Lightweight & perfect for Termux or VPS

---

## 📦 Requirements

- Python 3.10+
- Telegram Bot Token
- Admin Telegram ID
- Target channel ID and message ID
- Some channels/groups where the bot is an **admin with invite rights**

---

## ⚙️ Installation (Termux / VPS)

### 1. Clone the Bot

```bash
git clone https://github.com/yourusername/invitelinkbot
cd invitelinkbot
pkg update && pkg install python -y
pip install python-telegram-bot==20.6 apscheduler
```

## 2. Edit the Script

```BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
ADMIN_ID = 123456789
TARGET_CHANNEL_ID = -1001234567890
MESSAGE_ID = 111
CHANNELS = [
    "-100xxxxxxxxxx",
    "-100yyyyyyyyyy"
]
```

## ▶️ Run the Bot
```
python main.py
nohup python main.py &
```
