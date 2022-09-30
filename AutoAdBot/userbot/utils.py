# -*- coding:utf-8 -*-

import sys
import time
from pyrogram import Client
from pyrogram.enums.parse_mode import ParseMode

db = {
    "delay": 600, # Default wait time as seconds (integer)
    "between_delay": 0, # This delay for sending each message (as seconds and integer). Algorihtm -> Send message, wait {between_delay}, send next message.
    "auth": {
        "api_id": "1******", # Your tg account api_id
        "api_hash": "7******************************", # Your tg account api_hash
    },
    "chat_list": [],
    "message": """
<strong>Example ad Message</strong>
Please join my channel.

https://t.me/{yourchannelusername}
"""
}

app = Client(
    "account",
    db["auth"]["api_id"],
    db["auth"]["api_hash"],
    phone_number="", # Your phone number (international type with +)
    parse_mode=ParseMode.HTML, # String parsing mode. Default is HTML
    password="", # Your tg account 2FA password (if available).
)

def process():
    for cid in db['chat_list']:
        with app:
            try:
                app.send_message(chat_id=cid, text=db['message'])
            except Exception as err:
                print(err)
        print(f"[{cid}] Message sent.")
        time.sleep(db["between_delay"])

def sleepEffect(delay = db['delay']):
    temp = delay
    while temp != 0:
        sys.stdout.write(f"\r[{temp}] sleeping...")
        sys.stdout.flush()
        time.sleep(1)
        temp -= 1

def getChats():
    with app:
        dialogs = app.get_dialogs()
        for x in dialogs:
            cid = x.chat.id
            ctype = x.chat.type
            if str(ctype).strip() == "ChatType.SUPERGROUP": # For SUPERGROUP filtering
                if not cid in db['chat_list']:
                    db['chat_list'].append(cid)