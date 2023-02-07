# importing the module

import smtplib
import os

username = os.environ["username"]
receiver_add = "sent4ashu@gmail.com"
password = os.environ["password"]


smtp_server = smtplib.SMTP("smtp.gmail.com", 580)
smtp_server.ehlo()  # setting the ESMTP protocol

smtp_server.starttls()  # setting up to TLS connection
smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()

smtp_server.login(username, password)

msg_to_be_sent = """
Hello, Ashutosh!
How are you!
"""

smtp_server.sendmail(username, receiver_add, msg_to_be_sent)
print("Successfully the mail is sent")  
smtp_server.quit()
