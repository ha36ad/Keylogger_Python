from pynput.mouse import Listener
import logging

#Log directory
log_directory = " "
#Create .txt file
logging.basicConfig(filename = (log_directory+ "mouse_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#Check mouse's coordinates
def on_move(x, y):
    logging.info("Mouse at: ({0}, {1})".format(x, y))

#Check if the mouse has been pressed
def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

with Listener(on_move= on_move, on_click = on_click) as listener:
    listener.join()
