# -*- coding:utf-8 -*-

import time
import sys
from telebot.async_telebot import AsyncTeleBot
from telebot.util import antiflood

db = {
    "TOKEN": "", # Your bot token, you can get this from BotFather
    "delay": 600, # Default delay time as seconds (integer)
    "chat_list": [

# Your chats list, you should add chats to here as string example "-10013********"

    ],
    "message": """
This is example AD message.
Please join my channel.

https://t.me/{yourchannelusername}

Also follow me on instagram.

https://instagram.com/{yourusername}
""" # Your ad message.
}

bot = AsyncTeleBot(db["TOKEN"], parse_mode="HTML")

def sleepEffect(delay = db['delay']):
    temp = delay
    while temp != 0:
        sys.stdout.write(f"\r[{temp}] sleeping...")
        sys.stdout.flush()
        time.sleep(1)
        temp -= 1

async def process():
    while True:
        for cid in db["chat_list"]:
            await antiflood(bot.send_message, cid, db["message"])
            print(f"[{cid}] Message sent.")
        sleepEffect()