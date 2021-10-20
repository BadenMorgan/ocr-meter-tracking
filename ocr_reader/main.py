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

import pytesseract
from PIL import Image
import cv2

img = cv2.imread('random_capture.png',cv2.IMREAD_COLOR) #Open the image from which charectors has to be recognized
#img = cv2.resize(img, (620,480) ) #resize the image if required

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey to reduce detials
gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise

original = pytesseract.image_to_string(gray, config='')
#test = (pytesseract.image_to_data(gray, lang=None, config='', nice=0) ) #get confidence level if required
#print(pytesseract.image_to_boxes(gray))

print (original)
# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.framerate = 30

# rawCapture = PiRGBArray(camera, size=(640, 480))

# for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
# 	image = frame.array
# 	cv2.imshow("Frame", image)
# 	key = cv2.waitKey(1) & 0xFF
	
# 	rawCapture.truncate(0)

# 	if key == ord("s"):
# 		text = pytesseract.image_to_string(image)
# 		print(text)
# 		cv2.imshow("Frame", image)
# 		cv2.waitKey(0)
# 		break

# cv2.destroyAllWindows()

if __name__ == "__main__":
    print(pytesseract.image_to_string(Image.open("random_capture.png")))
    # while 1:
    #     try:
    #         pass
                    
    #     except KeyboardInterrupt:
    #         print("keyboard interrupt found")
    #         break
