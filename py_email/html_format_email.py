import smtplib
#Handle exception
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
host = 'smtp.gmail.com'
port = 587
username = "address@gmail.com"
password = "yourpassword"
from_email = username
to_list = [username]
try:
	#Send an email
	email_conn = smtplib.SMTP(host, port)
	print(email_conn.ehlo())
	print(email_conn.starttls())
	print(email_conn.login(username, password))


	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	the_msg = MIMEMultipart("alternative")
	the_msg['Subject'] = "Hello there!"
	the_msg['From'] = from_email
	#the_msg['To'] = to_list[0]

	plain_txt = "Testing the message"
	html_txt = """\
	<html>
		<head></head>
		<body>
			<p> Hey! <br>
				Tesing this email <b>message</>. Made by me
			</p>
		</body>
	</html>
	"""
	part_1 = MIMEText(plain_txt, 'plain')
	part_2 = MIMEText(html_txt, 'html')
	the_msg.attach(part_1)
	the_msg.attach(part_2)
	#print(the_msg.as_string())

	print(email_conn.sendmail(from_email, to_list, the_msg.as_string()))
	print(email_conn.quit())
	print("Sent ok")
except SMTPAuthenticationError:
	print("Authentication error")
except:
	print("An error")