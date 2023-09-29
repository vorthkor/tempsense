from time import sleep
from credentials import DOCS
import RPi.GPIO as GPIO
import lights
import messages



# disable warnings (optional)
GPIO.setwarnings(False)

# Select GPIO Mode
GPIO.setmode(GPIO.BCM)

# set light relay
buzzer = 23

# set pins as outputs
GPIO.setup(buzzer, GPIO.OUT)


def alarmOn():
    GPIO.output(buzzer, GPIO.HIGH)


def alarmOff():
    GPIO.output(buzzer, GPIO.LOW)


def alarmMicrowaveLed():
    for i in range(3):
        lights.ledOn()
        sleep(0.5)
        lights.ledOff()
        sleep(0.5)
        i += 1


def alarmMicrowaveBuzzer():
    for i in range(3):
        alarmOn()
        sleep(0.5)
        alarmOff()
        sleep(0.5)
        i += 1
    lights.lightsOn()


def masterAlarm():

    with open(f"{DOCS}/last.txt", 'r') as f:
        last_line = int(f.readlines()[-1])
    f.close()

    with open(f"{DOCS}/last.txt", 'r') as f:
        lastt_line = f.readlines()[-2]
    f.close()

    if lastt_line == '/naozhong\n':
        msg = 'on'
    else:
        lastt_line = int(lastt_line)

    if lastt_line == 1:
        alarmOn()
        msg = messages.botAlarm(lastt_line)
    elif last_line == 2:
        alarmOff()
        msg = messages.botAlarm(last_line)
    elif last_line == 3:
        alarmMicrowaveLed()
        msg = messages.botAlarm(last_line)
    elif lastt_line == 4:
        alarmMicrowaveBuzzer()
        msg = messages.botAlarm(lastt_line)
    else:
        msg = messages.notFound()
        
    return msg
