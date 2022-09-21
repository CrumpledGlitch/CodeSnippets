#This script displays a colourful banner that shows the time and updates every second

import os
import time
import datetime
import sys

def main():
    while True:
        os.system('clear')
        print(datetime.datetime.now().strftime("\033[1;31m %H:%M:%S"))
        time.sleep(1)

if __name__ == "__main__":
    main()  
