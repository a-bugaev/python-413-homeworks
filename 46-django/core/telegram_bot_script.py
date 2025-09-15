"""
sends message by signal from django
"""

import re
import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

SPECIALS = r"_*\[]()~`>#+-=|{}.!\\"


def escape_md2(text):
    """
    ithy.com/article/markdownv2-escaping-python-0tt3b7d6
    """
    return re.sub(f"([{re.escape(SPECIALS)}])", r"\\\1", text)


def send_message(text):
    """
    sends given massage to your chat
    """
    asyncio.run(Bot(token=BOT_TOKEN).send_message(CHAT_ID, text, parse_mode="MarkdownV2"))
