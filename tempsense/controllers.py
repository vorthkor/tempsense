import app as pp
import dht_temperature
import messages
import time



def sensorTemp(chat_id):

    msg = 'Perai que vou ver quanto que ta a temperatura e umidade...'
    pp.theMessage(chat_id, msg)


    checking = dht_temperature.tempCheck()

    if (checking[0] is None and checking[1] is None):
        msgTemp = 'deu ruim, tenta novamente enviando outro comando!'
        pp.theMessage(chat_id,msgTemp)
        varTemp = 3
        return varTemp
    else:
        warn = dht_temperature.tempWarning(checking[0])
        pp.theMessage(chat_id,messages.tempAnswers(warn))
        msgTemp = f'deu {checking[0]} graus Celsius eitaa\n e ta {checking[1]} % de umidade uouu!'
        pp.theMessage(chat_id,msgTemp)
        varTemp = 1
        return varTemp
    

def sensorJoke(chat_id):
    pp.theMessage(chat_id,messages.jokeQuestions())
    time.sleep(3)
    pp.theMessage(chat_id,messages.jokeAnswers())
    varJoke = 2
    return varJoke


def sensorGreeting(chat_id):
    pp.theMessage(chat_id,messages.botGreeting())
    time.sleep(3)
    varGreet = 4
    return varGreet


def sensorLight(chat_id, luz):
    pp.theMessage(chat_id,messages.botLight(luz))
    time.sleep(3)
    varLight = 5
    return varLight


def controlLed(chat_id, led):
    pp.theMessage(chat_id,messages.botLed(led))
    time.sleep(3)
    varLight = 51
    return varLight


def controlAlarm(chat_id, alarm):
    pp.theMessage(chat_id,messages.botAlarm(alarm))
    time.sleep(3)
    varAlarm = 8
    return varAlarm


def notFound(chat_id):
    pp.theMessage(chat_id,messages.notFound())
    varFound = 6
    return varFound


def whichCommands(chat_id):
    pp.theMessage(chat_id,messages.whichCommands())
    varFound = 7
    return varFound
