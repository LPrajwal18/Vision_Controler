import cv2
import mediapipe as mp
import pyautogui
import time
import math
import os
from datetime import datetime
import threading

# Setup
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Constants
BLINK_THRESHOLD = 0.015
CLICK_COOLDOWN = 1.0
ZOOM_COOLDOWN = 1.0
ZOOM_SENSITIVITY = 8
SCREENSHOT_DURATION = 2.5

# Timers and state
last_click_time = 0
last_zoom_time = 0
eye_closed_start_time = None
screenshot_taken = False  # Global variable for screenshot status
prev_eye_distance = None
frame_skip_rate = 5  # Process every 5th frame to reduce load

# Helper functions
def is_eye_closed(top, bottom, frame_h):
    return abs(top - bottom) < BLINK_THRESHOLD * frame_h

def get_blink_status(landmarks, frame_h):
    is_left = is_eye_closed(landmarks[159].y * frame_h, landmarks[145].y * frame_h, frame_h)
    is_right = is_eye_closed(landmarks[386].y * frame_h, landmarks[374].y * frame_h, frame_h)
    return is_left, is_right

def get_eye_distance(landmarks, frame_w):
    left = (landmarks[33].x * frame_w, landmarks[33].y)
    right = (landmarks[263].x * frame_w, landmarks[263].y)
    return math.hypot(left[0] - right[0], left[1] - right[1])

def take_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"eyes_closed_screenshot_{timestamp}.png"
    filepath = os.path.join(os.path.expanduser('~'), 'Pictures', filename)
    try:
        pyautogui.screenshot(filepath)
        print(f"Screenshot saved: {filepath}")
    except Exception as e:
        print(f"[ERROR] Screenshot failed: {e}")

def handle_clicks(is_left_closed, is_right_closed, current_time):
    global last_click_time
    if current_time - last_click_time < CLICK_COOLDOWN:
        return
    if is_left_closed and not is_right_closed:
        pyautogui.click()
        print("Left Click via Blink")
        last_click_time = current_time
    elif is_right_closed and not is_left_closed:
        pyautogui.click(button='right')
        print("Right Click via Wink")
        last_click_time = current_time

def perform_zoom(eye_distance, frame_w, current_time):
    global prev_eye_distance, last_zoom_time
    if prev_eye_distance is not None:
        delta = eye_distance - prev_eye_distance
        if abs(delta) > ZOOM_SENSITIVITY and (current_time - last_zoom_time > ZOOM_COOLDOWN):
            if delta > 0:
                pyautogui.hotkey('ctrl', '+')
                print("Zoom In")
            else:
                pyautogui.hotkey('ctrl', '-')
                print("Zoom Out")
            last_zoom_time = current_time
    prev_eye_distance = eye_distance

def process_frame(frame, results):
    global eye_closed_start_time, screenshot_taken  # Ensure we use the global variable
    frame_h, frame_w = frame.shape[:2]
    current_time = time.time()

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        # Cursor control
        landmark = landmarks[474]
        pyautogui.moveTo(screen_w * landmark.x, screen_h * landmark.y)

        # Blink detection
        is_left_closed, is_right_closed = get_blink_status(landmarks, frame_h)

        # Zoom detection
        eye_distance = get_eye_distance(landmarks, frame_w)
        perform_zoom(eye_distance, frame_w, current_time)

        # Screenshot logic
        if is_left_closed and is_right_closed:
            if eye_closed_start_time is None:
                eye_closed_start_time = current_time
                screenshot_taken = False
            else:
                duration = current_time - eye_closed_start_time
                if not screenshot_taken and duration >= SCREENSHOT_DURATION:
                    take_screenshot()
                    screenshot_taken = True
        else:
            if eye_closed_start_time is not None and (current_time - eye_closed_start_time) > 0.5:
                eye_closed_start_time = None
                screenshot_taken = False

            handle_clicks(is_left_closed, is_right_closed, current_time)

        # Display eye status
        cv2.putText(frame, f"Left Eye: {'Closed' if is_left_closed else 'Open'}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0) if is_left_closed else (0, 0, 255), 2)
        cv2.putText(frame, f"Right Eye: {'Closed' if is_right_closed else 'Open'}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0) if is_right_closed else (0, 0, 255), 2)
    else:
        # Face not detected
        cv2.putText(frame, "Face Not Detected", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print("Alert: Face not detected!")  # Print message to terminal

    return frame

def detect_face_and_control():
    global frame_skip_rate
    ret, frame = cam.read()
    if not ret:
        return

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    # Process every frame_skip_rate frames
    if int(time.time() * 1000) % frame_skip_rate == 0:
        frame = process_frame(frame, results)

    # Display the frame
    cv2.imshow("Eye Controlled Mouse | Click, Screenshot, Zoom", frame)

# Main loop with multi-threading for continuous background operations
def main_loop():
    while True:
        detect_face_and_control()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

# Run the main loop in a separate thread
thread = threading.Thread(target=main_loop)
thread.start()
