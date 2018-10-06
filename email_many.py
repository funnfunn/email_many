import smtplib	# Import smtplib for the actual sending function
from email.message import EmailMessage	# Import the email modules we'll need
import numpy as np
from time import sleep
import getpass

#WHOOOOO

sender_email_address = input("Enter the email address you wish to send the emails from (only lower case letters): ")
password = getpass.getpass("Enter your password: ")

if '@globalharmonization.net' in sender_email_address:
    s = smtplib.SMTP('send.one.com:587')
elif '@outlook.com' in sender_email_address:
    s = smtplib.SMTP('smtp-mail.outlook.com:587')
else:
    s = input('Enter the outgoing email server address:')


s.starttls()	#Start connection secured with TLS
s.login(sender_email_address, password)


with open('list_email_addresses.txt') as el:
    addressees = np.loadtxt(el, dtype = 'str', delimiter = '\t', usecols = (0, 1))


with open('message.txt') as fp:
    text = fp.read()


subject_email = input("Enter the text for the subject field of the email: ")


for addressee in addressees:
    email_text = 'Dear ' + addressee[0] + '\n' + '\n' + text
    msg = EmailMessage()
    msg.set_content(email_text)
    sleep(1)
    msg['Subject'] = subject_email
    msg['From'] = sender_email_address
    msg['To'] = addressee[1]
    s.send_message(msg)
    print('Sent email to:' + addressee[0])


s.quit()	#Close connection to the server


print('Done')
