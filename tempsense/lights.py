import RPi.GPIO as GPIO
import messages
from credentials import DOCS


# disable warnings (optional)
GPIO.setwarnings(False)

# Select GPIO Mode
GPIO.setmode(GPIO.BCM)

# set light relay
relay = 25
led = 16

# set pins as outputs
GPIO.setup(relay, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

def lightsOn():
    GPIO.output(relay, GPIO.HIGH)


def lightsOff():
    GPIO.output(relay, GPIO.LOW)


def controlLamp():
    with open(f"{DOCS}/lamp", 'r') as f:
        last_line = int(f.readlines()[-1])
    f.close()

    if last_line == 1:
        lightsOn()
        with open(f"{DOCS}/lamp", 'w') as f:
            f.write("0")
        f.close()
        return messages.botLight(1)
    else:
        lightsOff()
        with open(f"{DOCS}/lamp", 'w') as f:
            f.write("1")
        f.close()
        return messages.botLight(2)


def ledOn():
    GPIO.output(led, GPIO.HIGH)


def ledOff():
    GPIO.output(led, GPIO.LOW)


def controlLed():
    with open(f"{DOCS}/lamp", 'r') as f:
        last_line = int(f.readlines()[-1])
    f.close()

    if last_line == 1:
        ledOn()
        with open(f"{DOCS}/lamp", 'w') as f:
            f.write("0")
        f.close()
        return messages.botLed(1)
    else:
        ledOff()
        with open(f"{DOCS}/lamp", 'w') as f:
            f.write("1")
        f.close()
        return messages.botLed(2)
    