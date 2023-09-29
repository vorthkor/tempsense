import time
import messages
import index


# INITIAL MESSAGE
messages.startMessage()


# MAIN
def main():
    index.masterbot()
    while True:
        time.sleep(10)


try:
    main()
except KeyboardInterrupt:
    index.lastMessage()
    print('\nOff\n')
