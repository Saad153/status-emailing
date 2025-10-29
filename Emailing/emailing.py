import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "mail.seanetpk.com"
SMTP_PORT = 587
SMTP_USER = "sharmeen@seanetpk.com"
SMTP_PASS = "A6O373VfWieu"

TO_EMAIL = "saadalam996@gmail.com"  # Test email ✅

def send_email():
    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = TO_EMAIL
    msg["Subject"] = "🚚 Shipment Status Notification Test"

    body = """
    Hi Saad! 👋

    ✅ This is a test email from your shipment tracking software.
    Once DB integration is enabled, this email will be sent automatically
    whenever your shipment status changes. 🚀

    Best regards,
    Your Tracking System 😎
    """

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)

        server.sendmail(SMTP_USER, TO_EMAIL, msg.as_string())
        server.quit()

        print("✅ Email sent successfully to", TO_EMAIL)

    except Exception as e:
        print("❌ Email sending failed:", e)


if __name__ == "__main__":
    send_email()
