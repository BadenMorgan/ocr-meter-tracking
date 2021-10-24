VERSIONNO = "V1.0.0"
AUTHOR = "Baden Morgan"
PROGRAMNAME = "OCR Energy Meter Monitor"
import sys
sys.path.append('.')

#3rd party libs
from PIL import Image
import pytesseract
import cv2 

from picamera.array import PiRGBArray
from picamera import PiCamera
# from picamera.array import PiRGBArray
# from picamera import PiCamera

#my libs

import sentry_sdk

# def start_sentry():
#     if __name__ == "__main__":
#         print("-----------------")
#         print("Setting up Sentry")
#         print("-----------------")
#         sentry_sdk.init(
#             "https://2dc9964c331d4c20b5a8dd4997131485@o1041360.ingest.sentry.io/6010269",

#             # Set traces_sample_rate to 1.0 to capture 100%
#             # of transactions for performance monitoring.
#             # We recommend adjusting this value in production.
#             traces_sample_rate=1.0
#         )

# start_sentry()

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

rawCapture = PiRGBArray(camera, size=(640, 480))


# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.framerate = 30



if __name__ == "__main__":
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        
        rawCapture.truncate(0)

        if key == ord("s"):
            text = pytesseract.image_to_string(image)
            print(text)
            cv2.imshow("Frame", image)
            cv2.waitKey(0)
            break
    cv2.destroyAllWindows()
