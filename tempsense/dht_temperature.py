from datetime import datetime, timedelta
from credentials import DOCS
import Adafruit_DHT
import messages
from gpiozero import CPUTemperature

cpu = CPUTemperature()

hum1lis, tem1lis = [], []


def tempCheck():
    hum1, tem1 = Adafruit_DHT.read_retry(11, 27)
    hum1lis.append(hum1)
    tem1lis.append(tem1)
    print(f'S1: Humidity = {hum1} %; Temperature = {tem1} C')

    return tem1, hum1


def tempWarning(tem1):
    if tem1 < 21.0:
        var = 1
        return var
    elif tem1 > 26.0:
        var = 2
        return var
    else:
        var = 3
        return var


def roomTemp():
    tnow = datetime.now()

    with open(f'{DOCS}/logh.txt', 'r') as f:
        last_line = f.readlines()[-2]
        time_last =  datetime.strptime(last_line,"%Y-%m-%d %H:%M:%S.%f\n")
    f.close()

    if tnow - time_last < timedelta(seconds=6):
        with open(f'{DOCS}/temp.txt', 'r') as f:
            last_line = f.readlines()[-1]
            warn = tempWarning(int(last_line))
            msg = f'{messages.tempAnswers(warn,0,0)}\n'
            msgTemp = messages.tempAnswers(6,last_line, tnow)
        f.close()
        return msg+msgTemp

    else:
        checking = tempCheck()

        theTemp = checking[0]

        theHumi = checking[1]

        if (theTemp is None and theHumi is None):
            msgTemp = messages.tempAnswers(4,0,0)
            return msgTemp
        else:
            warn = tempWarning(theTemp)
            msg = f'{messages.tempAnswers(warn,0,0)}\n'
            tnow = datetime.now()
            msgTemp = messages.tempAnswers(5,theTemp,theHumi)

            with open(f'{DOCS}/temp.txt', 'w') as f:
                f.write(f'{theTemp}')
            f.close()
            
            return msg+msgTemp
        

def cpuTemp():
    tnow = datetime.now()

    with open(f'{DOCS}/logh.txt', 'r') as f:
        last_line = f.readlines()[-2]
        time_last =  datetime.strptime(last_line,"%Y-%m-%d %H:%M:%S.%f\n")
    f.close()

    if tnow - time_last < timedelta(seconds=6):
        with open(f'{DOCS}/temp.txt', 'r') as f:
            last_line = f.readlines()[-1]
            warn = tempWarning(int(last_line))
            msg = f'{messages.tempAnswers(warn,0,0)}\n'
            msgTemp = messages.tempAnswers(6,last_line, tnow)
        f.close()
        return msg+msgTemp

    else:
        theTemp = cpu.temperature

        if (theTemp is None):
            msgTemp = messages.tempAnswers(4,0,0)
            return msgTemp
        else:
            warn = tempWarning(theTemp)
            msg = f'{messages.tempAnswers(warn,0,0)}\n'
            tnow = datetime.now()
            msgTemp = messages.tempAnswers(7,theTemp,tnow)

            with open(f'{DOCS}/temp.txt', 'w') as f:
                f.write(f'{theTemp}')
            f.close()
            
            return msg+msgTemp
        

def tempMaster():
    with open(f"{DOCS}/last.txt", 'r') as f:
        last_line = int(f.readlines()[-1])
    f.close()

    if last_line == 1:
        msg = roomTemp()
    elif last_line == 2:
        msg = cpuTemp()
    else:
        msg = messages.notFound()
    return msg
