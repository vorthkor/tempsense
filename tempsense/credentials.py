import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN=os.getenv("TOKEN")
CHAT_ID_G=os.getenv("CHAT_ID")
CHAT_ID_G2=os.getenv("CHAT_ID2")
DOCS=os.getenv("DOCS")
ALARM_PASS=os.getenv("ALARM_PASS")