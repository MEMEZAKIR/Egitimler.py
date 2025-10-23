import cv2 as cv

def foto():
    img = cv.imread("D:\Videos\Hollow Knight.exe\Hollow Knight.exe Screenshot 2025.09.04 - 23.00.50.67.png")

    cv.imshow("Hollow Knight", img)

    cv.waitKey(0)

def Video():
    capture = cv.VideoCapture(0) # buraya bir numara da girebilirsin, mesela; 0  webcam

    while True:
        success, frame = capture.read()  # bir kare oku, aynı zamanda karenin okunup okunamamasına göre success için True ya da False değeri döndürür.
        cv.imshow("Video", frame)    # göster

        if cv.waitKey(20) & 0xFF == ord('d'):  #her 20 milisaniye kare'de "d"ye basıldı mı  diye kontrol eder.
                                               # videyu beklemeye alır ama aslında kare hızını da belirler, yenilenmeyi sağlar
            break
    capture.release()
    cv.destroyAllWindows()

Video()