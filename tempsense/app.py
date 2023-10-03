import time
import messages
import index
import subprocess
from credentials import HOME


# INITIAL MESSAGE
messages.startMessage()


# MAIN
def main():
    subprocess.run([f"{HOME}/tempsense/settg.sh"],shell=True)
    index.masterbot()
    while True:
        time.sleep(10)


try:
    main()
except KeyboardInterrupt:
    index.lastMessage()
    print('\nOff\n')
