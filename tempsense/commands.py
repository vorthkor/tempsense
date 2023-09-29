import controllers as ctrls

def commandss(ccmd, chatid):
    print('peiiii')
    if ccmd in ('/temperatura'):
        cc = ctrls.sensorTemp(chatid)
        print(cc)
    elif ccmd in ('/piada'):
        cc = ctrls.sensorJoke(chatid)
        print(cc)
    elif ccmd in ('/salve'):
        cc = ctrls.sensorGreeting(chatid)
        print(cc)
    elif ccmd in ('/luz1'):
        luz = 1
        cc = ctrls.sensorLight(chatid, luz)
        print(cc)
    elif ccmd in('/luz2'):
        luz = 2
        cc = ctrls.sensorLight(chatid, luz)
    elif ccmd in('/commands'):
        cc = ctrls.whichCommands(chatid)
        print(cc)
    elif ccmd in('/led1'):
        led = 1
        cc = ctrls.controlLed(chatid, led)
        print(cc)
    elif ccmd in('/led2'):
        led = 2
        cc = ctrls.controlLed(chatid, led)
        print(cc)
    elif ccmd in('/alarm1'):
        alarm = 1
        cc = ctrls.controlAlarm(chatid, alarm)
        print(cc)
    elif ccmd in('/alarm2'):
        alarm = 2
        cc = ctrls.controlAlarm(chatid, alarm)
        print(cc)
    elif ccmd in('/alarm3'):
        alarm = 3
        cc = ctrls.controlAlarm(chatid, alarm)
        print(cc)
    elif ccmd in('/alarm4'):
        alarm = 4
        cc = ctrls.controlAlarm(chatid, alarm)
        print(cc)
    else:
        cc = ctrls.notFound(chatid)
        print(cc)
        