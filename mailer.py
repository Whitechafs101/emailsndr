import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email ['from'] = ' ' #enter sender
email ['to'] = ' ' #enter recipient
email ['subject'] = ' ' #enter subject

email.set_content (html.substitute({'name': '  '}), 'html') #put reciepient's name

with smtplib.SMTP(host='smtp-mail.outlook.com',port=587) as smtp: #set your smtp server depending on the email you are using
	smtp.ehlo()
	smtp.starttls()
	smtp.login('youremail@mail.com', 'password') #enter your email address and password

	smtp.send_message(email)
	print('all done boss')