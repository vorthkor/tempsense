import time
import messages
import thebot


# INITIAL MESSAGE
messages.startMessage()


# MAIN
def main():
    thebot.masterbot()
    while True:
        time.sleep(10)


try:
    main()
except KeyboardInterrupt:
    thebot.lastMessage()
    print('\nOff\n')
