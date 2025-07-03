from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from deepface import DeepFace
import base64

app = Flask(__name__)

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        img_data = data["image"].split(",")[1]
        img_bytes = base64.b64decode(img_data)
        np_arr = np.frombuffer(img_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        emotions = []

        for (x, y, w, h) in faces:
            face_crop = frame[y:y+h, x:x+w]
            analysis = DeepFace.analyze(face_crop, actions=['emotion'], enforce_detection=False)
            emotion = analysis[0]['dominant_emotion']
            emotions.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h), "emotion": emotion})

        return jsonify({"success": True, "emotions": emotions})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

