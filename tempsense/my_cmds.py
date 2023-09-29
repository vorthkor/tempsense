import my_ctrls

def commandss(ccmd):
    if ccmd in ('/temperatura'):
        cc = my_ctrls.sensorTemp()
        return cc
    elif ccmd in ('/piada'):
        cc = my_ctrls.sensorJoke()
        return cc
    elif ccmd in ('/salve'):
        cc = my_ctrls.sensorGreeting()
        return cc
    elif ccmd in ('/luz1'):
        luz = 1
        cc = my_ctrls.sensorLight(luz)
        return cc
    elif ccmd in ('/luz2'):
        luz = 2
        cc = my_ctrls.sensorLight(luz)
        return cc
    elif ccmd in('/commands'):
        cc = my_ctrls.whichCommands()
        return cc
    elif ccmd in('/led1'):
        led = 1
        cc = my_ctrls.controlLed(led)
        return cc
    elif ccmd in('/led2'):
        led = 2
        cc = my_ctrls.controlLed(led)
        return cc
    elif ccmd in('/alarm1'):
        alarm = 1
        cc = my_ctrls.controlAlarm(alarm)
        return cc
    elif ccmd in('/alarm2'):
        alarm = 2
        cc = my_ctrls.controlAlarm(alarm)
        return cc
    elif ccmd in('/alarm3'):
        alarm = 3
        cc = my_ctrls.controlAlarm(alarm)
        return cc
    elif ccmd in('/alarm4'):
        alarm = 4
        cc = my_ctrls.controlAlarm(alarm)
        return cc
    else:
        cc = my_ctrls.notFound()
        return cc
