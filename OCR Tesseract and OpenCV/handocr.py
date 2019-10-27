# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import numpy as np


def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    #cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    ret,img = cv2.threshold(np.array(img), 125, 255, cv2.THRESH_BINARY)

    # Write the image after apply opencv to do some ...
    cv2.imwrite("./thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("./thres.png"))

 # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(img_path))

#     Remove template file
#     os.remove(temp)
    return result

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to input image to be OCR'd")
args = vars(ap.parse_args())

print(get_string(args['image']))