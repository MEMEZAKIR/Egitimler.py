import cv2 as cv
import numpy as np

def resize(frame, scale=0.15):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize( frame, dimensions, interpolation=cv.INTER_AREA)

frame = cv.imread("D:\Videos\Hollow Knight.exe\Hollow Knight.exe Screenshot 2025.09.04 - 23.00.50.67.png")
resized_image = resize(frame)

def Translation(frame, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (frame.shape[1], frame.shape[0])
    return cv.warpAffine(frame, transMat, dimentions)

translated = Translation(resized_image, 100, 100)
cv.imshow("bla", translated)


cv.waitKey(0)


