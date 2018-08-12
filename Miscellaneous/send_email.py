from email.mime.text import MIMEText
import smtplib


message = """
Check out
this test
message
"""
msg = MIMEText(message)
msg["Subject"] = "Test"
msg["From"] = "subhayan.b.bhattacharya@oracle.com"
msg["To"] = "subhayan.here@gmail.com"

t = smtplib.SMTP()
t.connect()
check = t.sendmail("subhayan.b.bhattacharya@oracle.com", "subhayan.here@gmail.com", msg.as_string())
print check
