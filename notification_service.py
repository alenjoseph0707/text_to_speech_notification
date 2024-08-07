from gtts import gTTS
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from datetime import datetime

# Generate a text notification
def generate_notification():
    return " this is an text to speech notification."

# Convert text to speech and save as an audio file
def text_to_speech(text):
    tts = gTTS(text)
    audio_file_path = "notification.mp3"
    tts.save(audio_file_path)
    return audio_file_path

# Send the audio file via email
def send_email(audio_file_path, to_email):
    from_email = "yourfrom mail"
    password = "your password"  # Use an App Password if you have 2-Step Verification enabled
    
    msg = MIMEMultipart()
    msg['From'] = "Unknown <>"
    msg['To'] = to_email
    msg['Subject'] = "Audio Notification"
    
    # Attach the audio file
    with open(audio_file_path, 'rb') as audio_file:
        part = MIMEAudio(audio_file.read(), _subtype="mp3")
        part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(audio_file_path))
        msg.attach(part)
    
    # Send the email using SMTP_SSL for port 465 / if TLS 587
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
    
    # Log the email sent
    now = datetime.now()
    formatted_date = now.strftime("%d/%b/%Y %H:%M:%S")
    print(f"Sent email to {to_email} at {formatted_date}")

# Example usage
if __name__ == '__main__':
    notification_text = generate_notification()
    audio_file_path = text_to_speech(notification_text)
    
    # Replace with the recipient's email address
    recipient_email = 'your recipient mail'
    
    send_email(audio_file_path, recipient_email)
