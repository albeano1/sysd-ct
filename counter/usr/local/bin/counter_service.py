import time
import signal
import sys
import os
from datetime import datetime

running = True

# Replace os.getlogin() with a more robust method
user = os.getenv('USER') or os.getenv('LOGNAME') or 'unknown_user'

def handle_sigterm(signum, frame):
    global running
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("/tmp/currentCount.out", "a") as f:
        f.write(f"{user}: {timestamp} Received SIGTERM, exiting\n")
        f.flush()
    running = False
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)

def main():
    counter = 0
    with open("/tmp/currentCount.out", "w") as f:
        while running:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            output = f"{user}: {timestamp} #{counter}\n"
            print(output, end="", flush=True)
            f.write(output)
            f.flush()
            counter += 1
            time.sleep(1)

if __name__ == "__main__":
    main()