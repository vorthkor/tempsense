from time import sleep
import lights
import RPi.GPIO as GPIO


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
