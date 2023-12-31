import tkinter as tk
from tkinter import filedialog
import pygame
from twilio.rest import Client
import cv2
import numpy as np
import time

# Initialize Pygame
pygame.init()

# Alarm Generation
def alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("alert.mp3")
    pygame.mixer.music.play(-1)

    # Allow the sound to play for up to 10 seconds
    time.sleep(10)

    # Stop the Pygame mixer
    pygame.mixer.music.stop()
    pygame.mixer.quit()

# SMS & GPS
def SMS_GPS():
    alert_message = "Fire Detected"
    location = "IIIT NUZVIDU CAMPUS"
    gps_link = "https://goo.gl/maps/q8YkbXs1am8qxTNq9"
    account_sid = "AC0bf99de39c0be1cefab6a23c4e5d001d"
    auth_token = "11b5f8aea75585ecbab3bb5b8575578c"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=alert_message + " at " + location + "\n" + gps_link,
        from_='+17193575948',
        to='+916303164462'
    )
    print("Message Sent successfully")

# Function to get the video file path from the user
def get_video_path():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])

    return file_path

# Fire Detection
video_path = get_video_path()

if not video_path:
    print("No video selected. Exiting.")
else:
    video = cv2.VideoCapture(video_path)

    while True:
        ret, frame = video.read()

        if frame is None:
            print("Fire Not Detected")
            break

        frame = cv2.resize(frame, (1000, 600))
        blur = cv2.GaussianBlur(frame, (15, 15), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        lower = [18, 50, 50]
        upper = [35, 255, 255]
        lower = np.array(lower, dtype='uint8')
        upper = np.array(upper, dtype='uint8')
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(frame, hsv, mask=mask)
        cv2.imshow("Output", frame)
        size = cv2.countNonZero(mask)
        if int(size) > 15000:
            print("Fire Detected")
            SMS_GPS()
            alarm()  # Play the alert sound
            break

        if not ret:
            break
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()
    video.release()
    pygame.mixer.quit()  # Close the pygame mixer at the end
