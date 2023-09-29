import random
import externalapi
from credentials import DOCS


def talkPhrases():
    with open(f'{DOCS}/phrases', 'r') as f:
        phrs = f.readlines()
    f.close()
    
    last = len(phrs) - 1
    rnd = random.randint(0,last)
    talk = phrs[rnd]

    if talk == "BB" or talk == "BB\n":
        msg = externalapi.bbPhrase()
    elif talk == "MEOW" or talk == "MEOW\n":
        msg = externalapi.meowFacts()
    elif talk == "SPACE" or talk == "SPACE\n":
        msg = externalapi.spacePeople()
    elif talk == "BORED" or talk == "BORED\n":
        msg = externalapi.doBored()
    elif talk == "CORPORATE" or talk == "CORPORATE\n":
        msg = externalapi.corporate()
    elif talk == "RANDOM" or talk == "RANDOM\n":
        msg = externalapi.rndFacts()
    elif talk == "TECHSH" or talk == "TECHSH\n":
        msg = externalapi.techGib()
    elif talk == "MATH" or talk == "MATH\n":
        msg = externalapi.mathrivia()
    else:
        msg = talk
    
    return msg
