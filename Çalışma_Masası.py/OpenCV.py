import cv2
import pyttsx3
import time

# Initialize TTS
tts = pyttsx3.init()
tts.setProperty('rate', 150)

# Cooldown so it doesn't repeat every frame
LAST_SPEAK = 0
SPEAK_COOLDOWN = 4.0  # seconds

# Load Haar cascade (OpenCV includes the path)
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

cap = cv2.VideoCapture(0)  # 0 = default camera
if not cap.isOpened():
    raise SystemExit("Could not open camera. Check camera permissions.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60,60))

        # Draw rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

        # If face detected and cooldown expired, say a phrase
        if len(faces) > 0 and (time.time() - LAST_SPEAK) > SPEAK_COOLDOWN:
            tts.say("Hello there! I see you.")
            tts.runAndWait()
            LAST_SPEAK = time.time()

        cv2.imshow("Laptop Robot: Vision", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
