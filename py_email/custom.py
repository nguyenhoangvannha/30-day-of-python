import smtplib
host = 'smtp.gmail.com'
port = 587
username = "address@gmail.com"
password = "yourpassword"
from_email = username
to_list = [username]

#Send an email
email_conn = smtplib.SMTP(host, port)
print(email_conn.ehlo())
print(email_conn.starttls())
print(email_conn.login(username, password))
print(email_conn.sendmail(from_email, to_list, "Helo i am python"))
print(email_conn.quit())
print("Sent ok")

#Handle exception
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

wrong_password = smtplib.SMTP(host, port)
print(wrong_password.ehlo())
print(wrong_password.starttls())
try:
	print(wrong_password.login(username, "wrong password"))
	print(wrong_password.sendmail(from_email, to_list, "Helo i am python"))
	print(wrong_password.quit())
except SMTPAuthenticationError:
	print("Authentication error")
except:
	print("An error")
#connected to gmail
