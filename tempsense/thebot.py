import telepot
from telepot.loop import MessageLoop
from datetime import datetime
import my_cmds
import os
from dotenv import load_dotenv

load_dotenv()

# BOT SETTING
botToken = os.getenv("TOKEN")
bot = telepot.Bot(botToken)
firstM = False
lastM = False
chat_id_g = os.getenv("CHAT_ID")

def theMessage(chtid,mss):
    bot.sendMessage(chtid, mss)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type != 'text':
        return
    
    command = msg['text']

    print(f'Got message: {command} from {chat_id}')
    with open(f'{os.getenv("DOCS")}/log.txt', 'a') as f:
        f.write(f'Got message: {command} from {chat_id} at {datetime.now()}')
        f.write('\n')
    f.close()
    
    with open(f'{os.getenv("DOCS")}/logh.txt', 'a') as f:
        f.write('\n')
        f.write(f'{datetime.now()}')
    f.close()

    theMessage(chat_id,my_cmds.commandss(command))


def firstMessage():
    global firstM
    if firstM:
        return
    firstM = True
    bot.sendMessage(chat_id_g, "Hello, World! Bot started!")
    return


def lastMessage():
    global lastM
    if lastM:
        return
    lastM = True
    bot.sendMessage(chat_id_g, "Goodbye, World! Bot stopped!")
    return


def masterbot():
    MessageLoop(bot, handle).run_as_thread()    # runs last updates
    print('I am listening...\n')
    firstMessage()
    