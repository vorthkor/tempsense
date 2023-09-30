import random
import externalapi


def showPhotos():
    showPic = ['CAT', 'DUCK', 'FOX', 'DOG', 'CAFE']
    shw = random.choice(showPic)

    if shw == "CAT" or shw == "CAT\n":
        externalapi.catPic()
        msg = 404
    elif shw == "DUCK" or shw == "DUCK\n":
        externalapi.duckPic()
        msg = 404
    elif shw == "FOX" or shw == "FOX\n":
        externalapi.foxPic()
        msg = 404
    elif shw == "DOG" or shw == "DOG\n":
        externalapi.dogPic()
        msg = 404
    elif shw == "CAFE" or shw == "CAFE\n":
        externalapi.cafePic()
        msg = 404
    else:
        msg = shw
    return msg
    