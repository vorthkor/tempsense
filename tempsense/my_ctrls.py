import dht_temperature
import messages
import time
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()


def sensorTemp():
    tnow = datetime.now()
    msg = 'Perai que vou ver quanto que ta a temperatura e umidade...\n'

    with open(f'{os.getenv("DOCS")}/logh.txt', 'r') as f:
        last_line = f.readlines()[-2]
        time_last =  datetime.strptime(last_line,"%Y-%m-%d %H:%M:%S.%f\n")
    f.close()

    if tnow - time_last < timedelta(hours=0.01):
        with open(f'{os.getenv("DOCS")}/temp.txt', 'r') as f:
            last_line = f.readlines()[-1]
            msgTemp = msg+f'deu {last_line} graus Celsius eitaa\n e a hora eh {tnow}\n'
        f.close()
        return msgTemp

    else:
        checking = dht_temperature.tempCheck()

        theTemp = checking[0]

        theHumi = checking[1]

        if (theTemp is None and theHumi is None):
            msgTemp = msg+'deu ruim, tenta novamente enviando outro comando!\n'
            return msgTemp
        else:
            warn = dht_temperature.tempWarning(theTemp)
            msg = f'{messages.tempAnswers(warn)}\n'
            tnow = datetime.now()
            msgTemp = msg+f'deu {theTemp} graus Celsius eitaa\n e ta {theHumi} % de umidade uouu!\n hora eh {tnow}\n'

            with open(f'{os.getenv("DOCS")}/temp.txt', 'a') as f:
                f.write(f'\n')
                f.write(f'{theTemp}')
            f.close()
            
            return msgTemp    


def sensorJoke():
    msg = messages.jokeQuestions()
    msg2 = messages.jokeAnswers()
    last = f'{msg}\n{msg2}'
    return last


def sensorGreeting():
    time.sleep(3)
    return messages.botGreeting()


def sensorLight(luz):
    return messages.botLight(luz)


def controlLed(led):
    msg = messages.botLed(led)
    return msg


def controlAlarm(alarm):
    msg = messages.botAlarm(alarm)
    return msg


def notFound():
    msg = messages.notFound()
    return msg


def whichCommands():
    msg = messages.whichCommands()
    return msg
