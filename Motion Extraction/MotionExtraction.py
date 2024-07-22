# Motion Extraction
'''
0 - Logitech Webcam
1 - Laptop WebCam
2 - Logitech Capture

ToDo:
- Make it GitHub ready
'''
 
# Imports
import numpy as np
import cv2 as cv
from collections import deque
import string
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

# Var / Config
src = 0
res = (640, 480)
fps = 60
dq = 2
motion_extraction = True
prev_neg_frame = None

# Initialize
vid = cv.VideoCapture(src, cv.CAP_DSHOW)    # Video Capture
vid.set(3, res[0])                          # Width
vid.set(4, res[1])                          # Height
vid.set(cv.CAP_PROP_FPS, fps)               # FPS
frame_buffer = deque([], dq)                # Buffer Frame Deque

# Functions
def create_input_box(title, input_text=""):
    img = np.zeros((200, 400, 3), dtype=np.uint8)
    cv.putText(img, title, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv.LINE_AA)
    cv.putText(img, input_text, (10, 100), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv.LINE_AA)
    cv.imshow("Input", img)

def keyboard_input(title):
    text = ""
    letters = string.ascii_lowercase + string.digits + "x"
    while True:
        create_input_box(title, text)
        key = cv.waitKey(1) & 0xFF
        if key == 8:
            text = text[:-1]
        elif key in [10, 13]:  # Enter key (10 - Linux , 13 - Windows)
            break
        elif 32 <= key <= 126:
            char = chr(key).lower()
            if char in letters:
                text += char
    cv.destroyWindow("Input")
    return text

def change_res():
    global vid, res
    resolution = keyboard_input("Resolution")
    if resolution == f"{res[0]}x{res[1]}":
        return res
    w, h = map(int, resolution.split('x'))
    vid.set(3, w)
    vid.set(4, h)
    return (w, h)
    
def change_fps():
    global vid
    print(vid.get(cv.CAP_PROP_FPS))
    fps = int(keyboard_input("FPS"))
    vid.release()
    vid = cv.VideoCapture(src, cv.CAP_DSHOW)

    vid.set(3, res[0])
    vid.set(4, res[1])
    vid.set(5, int(fps))
    print(vid.get(cv.CAP_PROP_FPS))

def adjust_buffer_size(event, x, y, flags, param):
    global frame_buffer, dq
    if event == cv.EVENT_MOUSEWHEEL:
        n_dq = dq + (1 if flags > 0 else -1)
        n_dq = max(1, n_dq)  # dq >= 1
        dq = n_dq
        frame_buffer = deque(frame_buffer, n_dq)


window_name = "Motion Extraction"
cv.namedWindow(window_name)
cv.setMouseCallback(window_name, adjust_buffer_size)

# Main Loop
while True:
    _, frame = vid.read()
    if not _:
        break 
    
    neg_value = np.full(frame.shape, 255, dtype=np.uint8)               # Pure White Frame
    neg_frame = cv.subtract(neg_value, frame)                           # 255 - 'rgbValue' = Negetive
    frame_buffer.append(neg_frame)                                      # Negetive as Buffer
    prev_neg_frame = frame_buffer[0]
    final_frame = cv.addWeighted(frame, 0.5, prev_neg_frame, 0.5, 0)    # Opacity = 50%
    fps = vid.get(cv.CAP_PROP_FPS)
    
    cv.setWindowTitle(f"{window_name}", f"{window_name} | {res[0]}x{res[1]}@{int(fps)} | Delay: {dq} | [Q]uit")
    cv.imshow(f"{window_name}", (final_frame if motion_extraction else frame))
        
    key = cv.waitKey(1) & 0xFF
    
    if key == ord('q'):                             # Quit
        break
    
    elif key == ord('m'):                           # Disable/Enable Motion Extraction
        motion_extraction = not motion_extraction
        frame_buffer.clear()
        
    elif key == ord('r'):                           # Change Resolution
        res = change_res()
        frame_buffer.clear()
        fps = vid.get(cv.CAP_PROP_FPS)
        
    elif key == ord('f'):                           # Change FPS
        change_fps()
        frame_buffer.clear()
    
vid.release()
cv.destroyAllWindows()