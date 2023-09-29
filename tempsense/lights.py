import RPi.GPIO as GPIO


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


def ledOn():
    GPIO.output(led, GPIO.HIGH)


def ledOff():
    GPIO.output(led, GPIO.LOW)
