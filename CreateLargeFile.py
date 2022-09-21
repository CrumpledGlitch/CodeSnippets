# This script creates 1GB of files in the current directory with the name of the file being the current date and time

import os
import time

def main():
    # Get current date and time
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    # Create a file with the current date and time
    os.system("dd if=/dev/zero of=" + current_time + ".txt bs=1G count=1")

if __name__ == "__main__":
    main()

