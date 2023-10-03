import controller
import talk
import messages
import lights
import show
import externalapi


def routes(route):
    if route in ('/temperature'):
        answ = messages.tempOptions()
    elif route in ('/lumiere'):
        answ = lights.controlLamp()
    elif route in('/led'):
        answ = lights.controlLed()
    elif route in('/naozhong'):
        answ = messages.naozhongOptions()
    elif route in ('/fala'):
        answ = talk.talkPhrases()
    elif route in ('/miseru'):
        answ = show.showPhotos()
    elif route in ('/dailyinfo'):
        answ = messages.dailyOptions()
    elif route in ('/astronomydaily'):
        answ = externalapi.lastAstro(1)
    elif route in ('/marsdaily'):
        answ = externalapi.lastMars(1)
    elif route in('/listagem'):
        answ = messages.whichCommands()
    elif route in('/whoami'):
        answ = messages.whoami()
    elif route in('/update'):
        controller.doUpdate()
        return 'updating'
    else:
        answ = controller.otherControls(route)

    return answ
