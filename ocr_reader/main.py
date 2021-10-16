VERSIONNO = "V1.0.0"
AUTHOR = "Baden Morgan"
PROGRAMNAME = "OCR Energy Meter Monitor"
import sys
sys.path.append('.')

#3rd party libs
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
#my libs

import sentry_sdk

def start_sentry():
    if __name__ == "__main__":
        print("-----------------")
        print("Setting up Sentry")
        print("-----------------")
        sentry_sdk.init(
            "https://2dc9964c331d4c20b5a8dd4997131485@o1041360.ingest.sentry.io/6010269",

            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=1.0
        )

start_sentry()

if __name__ == "__main__":
    while 1:
        try:
            pass
                    
        except KeyboardInterrupt:
            print("keyboard interrupt found")
            break
