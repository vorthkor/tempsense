import telepot
import os
import routes
import talk
from credentials import BOT_TOKEN,CHAT_ID_G,CHAT_ID_G2,DOCS
from telepot.loop import MessageLoop
from datetime import datetime


# BOT SETTING
bot = telepot.Bot(BOT_TOKEN)
chat_id_g = CHAT_ID_G
chat_id_g2 = CHAT_ID_G2
chat_id_gg = int(CHAT_ID_G)
chat_id_gg2 = int(CHAT_ID_G2)
ids = [chat_id_gg, chat_id_gg2]
firstM = False
lastM = False
botName = bot.getMe()['first_name']


def checkSize(file):
    size = os.path.getsize(f"{DOCS}/{file}.txt")
    if size > 200000:
        os.system(f'echo "cleared" > {DOCS}/{file}.txt')

def theMessage(chtid,mss,name):
    bot.sendMessage(chtid, f'{talk.greetings()}, {name}! {talk.emojios()} \n {mss}')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    print(content_type, chat_type, chat_id)

    if content_type != 'text':
        if content_type == 'photo':
            print(msg['photo'][0])
            with open(f'{DOCS}/thephts.txt', 'a') as f:
                f.write('\n')
                f.write(msg['photo'][0]['file_id'])
            f.close()
            if chat_id == chat_id_gg:
                bot.sendMessage(chat_id_gg2, f"there's a new photo  👀 try /omg")
            elif chat_id == chat_id_gg2:
                bot.sendMessage(chat_id_gg, f"there's a new photo  👀 try /omg")
        return
    
    if chat_id not in ids:
        return
    
    command = msg['text']
    name = msg['from']['first_name']

    checkSize('log')

    print(f'Got message: {command} from {chat_id}')
    with open(f'{DOCS}/log.txt', 'a') as f:
        f.write(f'Got message: {command} from {chat_id} at {datetime.now()}')
        f.write('\n')
    f.close()

    with open(f'{DOCS}/log.txt', 'a') as f:
        f.write(command)
        f.write('\n')
    f.close()

    checkSize('last')

    with open(f'{DOCS}/last.txt', 'a') as f:
        f.write('\n'+command)
    f.close()

    checkSize('logh')

    with open(f'{DOCS}/logh.txt', 'a') as f:
        f.write('\n')
        f.write(f'{datetime.now()}')
    f.close()

    thecommnds = routes.routes(command)

    if thecommnds == 404:
        bot.sendPhoto(chat_id,photo=open('./photo.png', 'rb'))
    elif thecommnds == 405:
        with open(f"{DOCS}/thephts.txt", 'r') as f:
            last_line = f.readlines()[-1]
        f.close()
        capt=f'{talk.hmojis()} omg {talk.hmojis()}'
        bot.sendPhoto(chat_id,last_line, caption=capt)
        
    elif thecommnds == 406:
        with open(f"{DOCS}/thephts.txt") as f:
            lines = f.readlines()
            for i in lines:
                new = i.replace("\n","")
                bot.sendPhoto(chat_id,new)
        f.close()
    else:
        theMessage(chat_id,thecommnds,name)


def firstMessage():
    global firstM
    if firstM:
        return
    firstM = True
    theMessage(chat_id_g, "Hello, World! Bot started! newww! 🟢",botName)
    return


def lastMessage():
    global lastM
    if lastM:
        return
    lastM = True
    theMessage(chat_id_g, "Goodbye, World! Bot stopped! 🔴", botName)
    return


def masterbot():
    MessageLoop(bot, handle).run_as_thread()    # runs last updates
    print('I am listening...\n')
    firstMessage()
    