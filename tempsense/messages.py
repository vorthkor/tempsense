import random
import lights
import alarms
import os


def startMessage():
    os.system('clear')
    print('Welcome to the tempsense project!')
    print("""\
                                  _                          
                    __      _____| | ___ ___  _ __ ___   ___ 
                    \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ |
                     \ V  V /  __/ | (_| (_) | | | | | |  __/
                      \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
                                                                

                    """)


def jokeQuestions():
    msgJoke = ['Pq a galinha atravessou a rua?', 'Qual o cumulo do absurdo?',
               'toc toc...', 'qual o numero do pi?', 'mais vale um passaro na mao...']
    msg = random.choice(msgJoke)
    return msg


def jokeAnswers():
    msgJoke = ['...Tambem nao sei kkkkkkk', 'para chegar ao outro lado ;p',
               '...do que dois passaros voando', 'pizza eh bom demais',
               'meia noite te conto', '3.141592653589794334']
    msg = random.choice(msgJoke)
    return msg


def botGreeting():
    msgGrt = ['Salve salve galerinha', 'sou eu o Kelvinho',
              'nao sei dar grau kkkkk', 'como voce ta se sentindo??',
              'essas molecula tao agitada em kkkk', 'peeeeei', 'bom trabalho bot']
    msg = random.choice(msgGrt)
    return msg


def tempAnswers(var):
    if var == 1:
        return 'Friacaaaaa!!! 🥶 '
    elif var == 2:
        return 'Que inferno de calooor 🥵'
    else:
        return 'ta tranquilo ta favoravel 🤙'


def botLight(aux):
    if aux == 1:
        lights.lightsOn()
        msg = 'Acendendo luz'
    elif aux == 2:
        lights.lightsOff()
        msg = 'Apagando luz'
    return msg


def botLed(aux):
    if aux == 1:
        lights.ledOn()
        msg = 'Acendendo led'
    else:
        lights.ledOff()
        msg = 'Apagando led'
    return msg


def botAlarm(aux):
    if aux == 1:
        alarms.alarmOn()
        msg = 'Liga alarme'
    elif aux == 2:
        alarms.alarmOff()
        msg = 'Desliga alarme'
    elif aux == 3:
        alarms.alarmMicrowaveLed()
        msg = 'Alarme microwave led'
    else:
        alarms.alarmMicrowaveBuzzer()
        msg = 'Alarme microwave buzzer'
    return msg


def notFound():
    msg = "404 command not found!"
    return msg


def whichCommands():
    msg = '''
/temperatura - verifica temperatura no sensor
/piada - conta piadinha
/salve - opa
/luz1 - liga luz
/luz2 - apaga luz
/led1 - liga led
/led2 - apaga led
/alarm1 - liga alarme
/alarm2 - desliga alarme
/alarm3 - alarme mw led
/alarm4 - alarme mw buzzer
/commands - lista os comandos
    '''
    return msg
