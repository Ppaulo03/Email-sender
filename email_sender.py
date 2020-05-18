import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

'''
dummyb28
Dummy_123
'''

email = EmailMessage()
email['from'] = 'Dummy'
email['to'] = 'ppaulo030601@gmail.com'
email['subject'] = 'The World Needs You'
email.set_content(html.substitute({'name': 'Hero'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummyb28@gmail.com', 'Dummy_123')
    smtp.send_message(email)
    print('ALl good Boss!')
