import cv2 as cv
import numpy as np

def resize(frame, scale=0.15):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize( frame, dimensions, interpolation=cv.INTER_AREA)

frame = cv.imread("D:\Videos\Hollow Knight.exe\Hollow Knight.exe Screenshot 2025.09.04 - 23.00.50.67.png")
resized_image = resize(frame)
#cv.imshow("Hollow", resized_image)


blank_image = np.zeros((500,500,3), dtype="uint8")
#cv.imshow("Blank", blank_image)
blank_image_2 = np.zeros((500,500,3), dtype="uint8")

# 1) paint the image a certain colour
blank_image[100:400, 225:275 ] = 0,250,0
#cv.imshow("Green", blank_image)

# 2) Draw a rectangle("dikdörtgen")
cv.rectangle(blank_image, (150,160), (350,205), (0,250,0), thickness=-1)
#cv.imshow("rectangle", blank_image)

# 3) Draw a circle
cv.circle(blank_image,(249,245), (170), (0,100,0),thickness=3 )
#cv.imshow("circle", blank_image)

# 4) Draw a line
cv.line(blank_image, (100,430), (400,430), (250,250,250), thickness=2)
#cv.imshow("line", blank_image)

# 5) Write text
cv.putText(blank_image, "FOR THE HOLY LORDS", (15,60), cv.FONT_HERSHEY_COMPLEX, 1.3, (0,200,0) )
cv.imshow("FINAL", blank_image)

cv.waitKey(0)