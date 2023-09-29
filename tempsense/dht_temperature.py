import Adafruit_DHT

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
