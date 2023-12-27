import controller
import talk
import messages
import lights
import show
import externalapi


def routes(route):
    if route == '/temperature':
        answ = messages.tempOptions()
    elif route == '/naozhong':
        answ = messages.naozhongOptions()
    elif route == '/dailyinfo':
        answ = messages.dailyOptions()
    elif route == '/listagem':
        answ = messages.whichCommands()
    elif route == '/whoami':
        answ = messages.whoami()
    elif route == '/echo':
        answ = messages.echo()
    elif route == '/astronomydaily':
        answ = externalapi.lastAstro(1)
    elif route == '/marsdaily':
        answ = externalapi.lastMars(1)
    elif route == '/lumiere':
        answ = lights.controlLamp()
    elif route == '/led':
        answ = lights.controlLed()
    elif route == '/fala':
        answ = talk.talkPhrases()
    elif route == '/miseru':
        answ = show.showPhotos()
    elif route == '/update':
        controller.doUpdate()
        return 'updating'
    elif route == '/omg':
        return 405
    elif route == '/archive':
        return 406
    else:
        answ = controller.otherControls(route)

    return answ
