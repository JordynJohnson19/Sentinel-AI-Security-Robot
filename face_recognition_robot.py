#!/usr/bin/env python3
import time
import datetime
import os
import smtplib
from email.message import EmailMessage
from xgolib import XGO
from xgoedu import XGOEDU

# === Initialize Robot and EDU modules ===
dog = XGO('xgomini')
edu = XGOEDU()

# === Email configuration ===
EMAIL_SENDER = "youremail@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use a Gmail App Password
EMAIL_RECEIVER = "receiver_email@example.com"

def send_email_alert(image_path, timestamp):
    msg = EmailMessage()
    msg["Subject"] = f"Unknown Face Detected - {timestamp}"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg.set_content(f"An unknown face was detected at {timestamp}. See attached image.")

    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            msg.add_attachment(
                img_file.read(),
                maintype="image",
                subtype="jpeg",
                filename=os.path.basename(image_path)
            )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email alert sent at {timestamp}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# === Setup Display ===
edu.lcd_clear()
edu.lcd_text(40, 110, "Face Tracker Ready", fontsize=20)
print("Starting face tracking and recognition...")

# === Main Loop ===
try:
    while True:
        result = edu.face_detect()
        if result:
            x, y, w, h = result
            face_center_x = x + w // 2
            screen_center_x = 160
            offset = face_center_x - screen_center_x

            edu.lcd_clear()
            edu.lcd_text(40, 20, "Face Detected", fontsize=18)

            # Tracking logic
            if abs(offset) < 30:
                edu.lcd_text(20, 80, "Centered", fontsize=18)
                dog.stop()
            elif offset < -30:
                edu.lcd_text(20, 80, "Turning Left", fontsize=18)
                dog.turn(60)
            elif offset > 30:
                edu.lcd_text(20, 80, "Turning Right", fontsize=18)
                dog.turn(-60)

        else:
            edu.lcd_clear()
            edu.lcd_text(20, 20, "No Face Detected", fontsize=18)
            dog.stop()

            # Save snapshot
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            date_folder = datetime.datetime.now().strftime('%Y-%m-%d')
            folder = f"/home/pi/logs/{date_folder}"
            os.makedirs(folder, exist_ok=True)

            photo_name = f"unknown_{timestamp}.jpg"
            edu.xgoTakePhoto(photo_name)

            src = f"/home/pi/xgoPictures/{photo_name}"
            dest = f"{folder}/{photo_name}"

            if os.path.exists(src):
                os.rename(src, dest)
                send_email_alert(dest, timestamp)
            else:
                print(f"Photo not found: {src}")

            time.sleep(5)

        time.sleep(0.5)

except KeyboardInterrupt:
    dog.stop()
    edu.lcd_clear()
    edu.lcd_text(60, 110, "System Stopped", fontsize=20)
    print("Program stopped by user.")
