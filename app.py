from notification_service import generate_notification, text_to_speech, send_email

def main():
    # Generate a text notification
    text = generate_notification()
    
    # Convert the text notification to speech
    audio_file_path = text_to_speech(text)
    
    # Email address of the receiver
    receiver_email = "alenjoseph0707@gmail.com"
    
    # Send the audio notification via email
    send_email(audio_file_path, receiver_email)
    
    print("Notification sent successfully!")

if __name__ == "__main__":
    main()
