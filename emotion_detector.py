import cv2
from deepface import DeepFace

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Use default camera without Windows-only flag
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: Could not open webcam. Is it connected and free?")
    exit()

print("[INFO] Webcam opened successfully. Press 'q' to quit.")

while True:
    ret, frame = video.read()
    if not ret:
        print("[WARNING] Failed to read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (89, 2, 236), 1)

        try:
            # Analyze only the face region (crop for better performance)
            face_crop = frame[y:y+h, x:x+w]
            analysis = DeepFace.analyze(face_crop, actions=['emotion'], enforce_detection=False)

            emotion = analysis[0]['dominant_emotion']
            print("Emotion:", emotion)

            # Show emotion label on frame
            cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (224, 77, 176), 2)

        except Exception as e:
            print("Analysis error:", str(e))

    # Show video frame
    cv2.imshow("Emotion Detector", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video.release()
cv2.destroyAllWindows()

