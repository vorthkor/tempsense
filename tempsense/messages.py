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


def tempAnswers(var, temp, hum):
    if var == 1:
        return 'Cold as ice!!! 🥶 ' 
    elif var == 2:
        return 'Hell of a day 🥵'
    elif var == 3:
        return 'Tranquility base 🤙'
    elif var == 4:
        return 'Please try again! ⚠️ '
    elif var == 5:
        return f'The temperature is {temp} degrees Celsius 🌡 \n The air humidity is {hum} % 💦'
    elif var == 6:
        return f'The temperature is {temp} degrees Celsius 🌡 \n The time now is {hum} 🕤'
    elif var == 7:
        return f'The CPU temperature is {temp} degrees Celsius 🌡 \n The time now is {hum} 🕤'


def botLight(aux):
    if aux == 1:
        msg = 'Allumage de la lampe 💡'
    elif aux == 2:
        msg = 'Éteindre la lampe 🌚'
    return msg


def botLed(aux):
    if aux == 1:
        msg = 'Illuminazione del LED 🕯️'
    else:
        msg = 'Spegnimento del LED 🕯'
    return msg


def botAlarm(aux):
    if aux == 1:
        msg = 'Liga alarme 🔊'
    elif aux == 2:
        msg = 'Desliga alarme 🔇'
    elif aux == 3:
        msg = 'Alarme microwave led 🪔'
    else:
        msg = 'Alarme microwave buzzer 🔔⏰'
    return msg


def notFound():
    msg = "404 command not found! 🚫"
    return msg


def whichCommands():
    msg = '''
/temperature - Verifies the room's temperature 🌡
/lumiere - Allumer la lampe 💡
/led - Accendere il LED 🔦
/naozhong - Dǎkāi nàozhōng ⏰
/fala - Conversas aletórias 🗣️
/miseru - 写真を見せる 📸
/dailyinfo - Info about the mars or astronomy picture of the day 📝
/astronomydaily - The astronomy picture of the day 🔭
/marsdaily - The latest mars picture 🚀
/listagem - Listagem de los comandos disponibles 📜
/whoami - 🗣️
    '''
    return msg


def tempOptions():
    msg = '''
        Please choose an option number 🔢: 
        1 - Room temperature 🛌
        2 - Raspberry Pi's CPU temperature 🖥️
        '''
    return msg


def naozhongOptions():
    msg = '''
        Please choose an option number 🔢: 
        1 - Buzzer on 🔊
        2 - Buzzer off 🔇
        3 - Blink LED 🪔
        4 - Microwave 🔔⏰
        '''
    return msg

def dailyOptions():
    msg = '''
        Please choose an option number 🔢: 
        1 - Astronomy picture of day info 🔭
        2 - Last mars picture info 🚀
        '''
    return msg


def whoami():
    msg = "I'm cakinho 🐒 a telegram bot 🦾 running in a Raspberry Pi Zero W 💻 somewhere in the world 🌐 Check out my computer temperature through the /temperature command. You can also see my repository on https://github.com/vorthkor/tempsense and check out to news! \nThis version is from 2023-11-28."
    return msg