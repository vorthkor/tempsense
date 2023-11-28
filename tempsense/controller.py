import externalapi
import alarms
import dht_temperature
import subprocess
from credentials import DOCS,ALARM_PASS,HOME


def doUpdate():
    subprocess.run([f"{HOME}/doupdate.sh"],shell=True)


def notFound():
    externalapi.notHere()
    msg = 404
    return msg

def otherControls(route):
    with open(f"{DOCS}/log.txt", 'r') as f:
        last_line = f.readlines()[-3]
    f.close()

    with open(f"{DOCS}/log.txt", 'r') as f:
        lastt_line = f.readlines()[-5]
    f.close()

    if last_line == '/naozhong\n' or lastt_line == '/naozhong\n':
        if route == "1" or route == "4":
            answ = 'Please enter the password 🔎'
        elif route == "2" or route == "3":
            answ = alarms.masterAlarm()
        elif route == ALARM_PASS:
            answ = alarms.masterAlarm()
        else:
            answ = 'invalid! ⛔'

    elif last_line == '/temperature\n':
        answ = dht_temperature.tempMaster()

    elif last_line == '/dailyinfo\n':
        if route == "1":
            answ = externalapi.lastAstro(2)
        elif route == "2":
            answ = externalapi.lastMars(2)
        else:
            answ = 'invalid! ⛔'

    else:
        answ = notFound()
    return answ
