import cv2 as cv

def resize(frame, scale=0.4):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize( frame, dimensions, interpolation=cv.INTER_AREA)

frame = cv.imread("D:\Videos\Hollow Knight.exe\Hollow Knight.exe Screenshot 2025.09.04 - 23.00.50.67.png")
resized_image = resize(frame)
cv.imshow("original", resized_image)

# Converting to grayscale.
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray_Image", gray)

# Blur the Image.
blur = cv.GaussianBlur(gray, (3,3),cv.BORDER_DEFAULT)
#cv.imshow("Blur", blur)

# Edge Cascade.
canny = cv.Canny(resized_image, 125,175)
#cv.imshow("canny", canny)

# Dilating the Image.
dilated = cv.dilate(canny, (3,3), iterations=1)
#cv.imshow("dialeted", dilated)

# Eroding 
eroded = cv.erode(dilated, (3,3), iterations=1)     # Eroding=/ Dilating.  =canny
#cv.imshow("eroded" ,eroded)

# Resize
resized = cv.resize(frame, (500,500))
cv.imshow("resized", resized)

# Cropping
cropped = frame[550:600,530,600]
cv.imshow("bla", cropped)

cv.waitKey(0)
