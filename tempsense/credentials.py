import os

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

BOT_TOKEN=os.getenv("TOKEN")
CHAT_ID_G=os.getenv("CHAT_ID")
DOCS=os.getenv("DOCS")
ALARM_PASS=os.getenv("ALARM_PASS")