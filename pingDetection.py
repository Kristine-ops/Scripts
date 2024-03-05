from scapy.all import sniff, ICMP
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("Starting Ping Scan Detection...")

email_config = {
    'sender_email': 'email',
    'sender_password': 'password',
    'receiver_email': 'email',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}

def send_email_alert(subject, message):
    try:
        server = smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port'])
        server.starttls()
        server.login(email_config['sender_email'], email_config['sender_password'])

        msg = MIMEMultipart()
        msg['From'] = email_config['sender_email']
        msg['To'] = email_config['receiver_email']
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server.sendmail(email_config['sender_email'], email_config['receiver_email'], msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", str(e))

def ping_scan_callback(pkt):
    if ICMP in pkt and pkt[ICMP].type == 8: 
        print(f"Ping scan detected from: {pkt.src}")
        send_email_alert("Ping Scan Alert", f"Ping scan detected from: {pkt.src}")

sniff(prn=ping_scan_callback, filter="icmp", store=0)

