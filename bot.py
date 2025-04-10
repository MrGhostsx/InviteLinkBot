import time
import requests
import telebot

# Bot token and IDs
BOT_TOKEN = "7432835582:AAF-86sHcgKBVEtJRqb7rtWR3Kd-v3Zn5t0"
CHANNEL_ID = -1002472718132
OWNER_ID = 7535818274

bot = telebot.TeleBot(BOT_TOKEN)
last_invite_link = None

def revoke_invite_link(invite_link):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/revokeChatInviteLink"
    payload = {
        "chat_id": CHANNEL_ID,
        "invite_link": invite_link
    }
    response = requests.post(url, data=payload)
    return response.json()

def create_invite_link():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/createChatInviteLink"
    payload = {
        "chat_id": CHANNEL_ID,
        "name": "10-sec-link"
    }
    response = requests.post(url, data=payload)
    return response.json()

while True:
    try:
        # Revoke the old invite link
        if last_invite_link:
            revoke_response = revoke_invite_link(last_invite_link)
            if not revoke_response.get("ok"):
                bot.send_message(OWNER_ID, f"⚠️ Failed to revoke old link:\n{revoke_response}")
        
        # Create a new invite link
        new_link_response = create_invite_link()
        if new_link_response.get("ok"):
            new_link = new_link_response["result"]["invite_link"]
            last_invite_link = new_link
            bot.send_message(OWNER_ID, f"✅ New invite link:\n{new_link}")
        else:
            bot.send_message(OWNER_ID, f"❌ Failed to create new link:\n{new_link_response}")

    except Exception as e:
        bot.send_message(OWNER_ID, f"⚠️ Error occurred:\n{e}")

    time.sleep(10)  # wait 10 seconds
