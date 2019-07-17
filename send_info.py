import socket
import os
import sys

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def get_device_ip_address():

    try:
        gw = os.popen("ip -4 route show default").read().split()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((gw[2], 0))
        ipaddr = s.getsockname()[0]
        gateway = gw[2]
        host = socket.gethostname()
        result = "OS: Raspbian<br/>IP: " + ipaddr + "<br/>Gateway: " + gateway + "<br/>Host: " + host
        return result
    except:
        return "Could not detect ip address"

def send_email(text):

    message = Mail(
    from_email='<your email address>',
    to_emails='<your email address>',
    subject='Wifi Info',
    html_content=text)

    try:
        sg = SendGridAPIClient('<API Key>')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

message = get_device_ip_address()
print("Sending email, can take a while.")
send_email(message)
print("Done.")

sys.exit()
