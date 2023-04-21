import logging
import os

import cv2
import pytesseract
from pynput import keyboard

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

video_path = "oop.mp4"
video = cv2.VideoCapture(video_path)

def extract_and_output_text(frame):
    text = pytesseract.image_to_string(frame)
    logging.debug(f"Extracted text: {text}")

def on_key_release(key):
    global video, paused, playback_speed

    if key == keyboard.Key.space:
        paused = not paused
        logging.debug(f"Toggled pause: {paused}")
    elif key == keyboard.KeyCode.from_char("1"):
        playback_speed = 1
        logging.debug("Playback speed set to 1x")
    elif key == keyboard.KeyCode.from_char("2"):
        playback_speed = 2
        logging.debug("Playback speed set to 2x")
    elif key == keyboard.Key.left:
        current_position = video.get(cv2.CAP_PROP_POS_MSEC)
        video.set(cv2.CAP_PROP_POS_MSEC, current_position - 10000)
        logging.debug("Rewound 10 seconds")
    elif key == keyboard.Key.right:
        current_position = video.get(cv2.CAP_PROP_POS_MSEC)
        video.set(cv2.CAP_PROP_POS_MSEC, current_position + 10000)
        logging.debug("Forwarded 10 seconds")
    elif key == keyboard.KeyCode.from_char("R"):
        ret, frame = video.read()
        if ret:
            frame_copy = frame.copy()
            extract_and_output_text(frame_copy)
            video.set(cv2.CAP_PROP_POS_FRAMES, video.get(cv2.CAP_PROP_POS_FRAMES) - 1)

paused = False
playback_speed = 1

with keyboard.Listener(on_release=on_key_release) as listener:
    while video.isOpened():
        if not paused:
            ret, frame = video.read()
            if ret:
                cv2.imshow("Video", frame)
                wait_time = int(1000 / (30 * playback_speed))
                if cv2.waitKey(wait_time) & 0xFF == ord("q"):
                    break
            else:
                break

    video.release()
    cv2.destroyAllWindows()
    listener.join()
