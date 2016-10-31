'''
This program works only for windows because the command is written for windows console.
'''

import subprocess, re, smtplib
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def charge():
    command = "WMIC PATH Win32_Battery Get EstimatedChargeRemaining"
    argu = command.split()

    fromm =  # sender gmail id
    to =   # gmail id where the notification has to be sent
    msg = MIMEMultipart()
    msg['From'] = fromm
    msg['To'] = to
    msg['Subject'] = "Remove Charger"
    body = "Please remove your laptop from charging."
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    while True:
        outpu = subprocess.check_output(argu, universal_newlines=True, shell=True)
        outpu.strip()
        percen = re.findall('([0-9]+)', outpu)
        print(percen[0])
        if int(percen[0]) > 90:  # We can set the value at which we want the notification.
            # send a mail
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(fromm, "password")
            server.sendmail(fromm, to, text)
            server.close()
            break
        else:
            print("still charging")
            sleep(120)

if __name__ == "__main__":
    charge()
