# Fire-Detection-Using-tkinter
# Fire Detection System

This Python script uses OpenCV, Pygame, Twilio, and Tkinter to create a fire detection system from a video file. When a fire is detected, it triggers an alert sound, sends an SMS with the location, and provides a link to the location on Google Maps.

## Dependencies

- Python 3.x
- Tkinter
- Pygame
- Twilio
- OpenCV
- Numpy

## Setup

1. Install the required dependencies using the following:
    ```bash
    pip install tk pygame twilio opencv-python numpy
    ```

2. Obtain a Twilio account SID, authentication token, and a Twilio phone number to send SMS.

3. Update the following variables in the script with your Twilio account SID, authentication token, Twilio phone numbers, and the path to the alert sound file:
    - `account_sid`
    - `auth_token`
    - `from_`
    - `to`

4. Ensure you have a video file (in formats like mp4, avi, or mkv) for testing the fire detection.

## How to Run

1. Run the script using the following command:
    ```bash
    python fire_detection.py
    ```

2. The script will prompt you to select a video file. Choose a video file containing scenes with potential fire.

3. The script will process the video frames, and if a fire is detected, it will trigger an alert sound, send an SMS, and display the video frame with the fire.

4. Press 'q' to exit the video frame display.

## Note
- The script uses a basic fire detection algorithm based on color thresholding. Adjust the color range (`lower` and `upper`) in the script according to your video characteristics for better accuracy.

- The SMS functionality requires a working Twilio account with a balance to send messages.

- The Google Maps link in the SMS provides the GPS coordinates. You may want to customize the `location` variable in the `SMS_GPS` function accordingly.

- The script uses the Pygame library for playing the alert sound. Make sure your system has audio capabilities.

- It is recommended to test the system with different video files and adjust the fire detection parameters for optimal performance.

## Credits

- This script was created by [Sri Harsha].
