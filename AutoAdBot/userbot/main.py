# -*- coding:utf-8 -*-

from userbot.utils import *

print("""
Disclaimer:
If your answer to the question is no, you should add chat ids to list called "chat_list" in utils.py line 15.
""")
answer = str(input(f"[?] Do you wanna auto get your all groups ?: ")).lower()

if answer.startswith("y"):
    getChats()

while True:
    process()
    sleepEffect()