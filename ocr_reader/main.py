VERSIONNO = "V1.0.0"
AUTHOR = "Baden Morgan"
PROGRAMNAME = "OCR Energy Meter Monitor"
import sys
sys.path.append('.')

#3rd party libs
from PIL import Image
import pytesseract
import cv2 

# from picamera.array import PiRGBArray
# from picamera import PiCamera

import subprocess

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

# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.framerate = 0.1

# rawCapture = PiRGBArray(camera, size=(640, 480))


# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.framerate = 30



if __name__ == "__main__":
    # for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    #     image = frame.array
    # img = cv2.imread("image.jpg", 1)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite('grayed.jpg', gray)
    #     # cv2.imshow("Frame", image)
    #     # key = cv2.waitKey(1) & 0xFF
        
    #     rawCapture.truncate(0)
    while 1:
        # if key == ord("s"):
        subprocess.call("raspistill -o /home/pi/git/ocr-meter-tracking/ocr_reader/image.jpg", shell=True)
        img = cv2.imread("image.jpg", 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('grayed.jpg', gray)
        text = pytesseract.image_to_string("grayed.jpg")
        print(text)
        # cv2.imshow("Frame", image)
        # cv2.waitKey(0)
        # break
    # cv2.destroyAllWindows()
