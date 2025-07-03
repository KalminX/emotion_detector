# 🎭 Real-Time Emotion Detection Web App

A web-based application that uses your **webcam** to detect your **facial expressions in real time**, draws a **green rectangle** around your face, and displays your **current emotion with a matching emoji**.

It combines the speed of **OpenCV** for face detection with the accuracy of **DeepFace** for emotion recognition — all powered by a **Flask backend** and a sleek **HTML/JavaScript frontend**.

---

## ✨ Demo

> A camera stream opens in your browser. Every 2 seconds:
>
> * A green rectangle is drawn around your detected face.
> * Your current emotion (like “happy” 😊 or “sad” 😢) is displayed in real time.
> * If no face is detected, a fallback message appears.

---

## 🧠 How It Works

### 🔍 1. **Face Detection**

* Your browser captures video from your webcam.
* A frame is sent every 2 seconds to the Flask server.
* OpenCV's Haar Cascade (`haarcascade_frontalface_default.xml`) detects the face coordinates.

### 🤖 2. **Emotion Recognition**

* The detected face is cropped and passed to **DeepFace**.
* DeepFace returns the **dominant emotion** (e.g., `happy`, `neutral`, `sad`, etc.)

### 🎨 3. **Frontend Overlay**

* The emotion is displayed on the webpage with a matching **emoji**.
* You see: `Detected: happy 😄` and a green rectangle drawn around your face.

---

## 🖼️ Screenshot

![demo](https://your-screenshot-url.com/demo.png) <!-- Replace with real image -->

---

## 📁 Folder Structure

```
emotion-detector/
├── app.py                 # Flask server with face + emotion detection
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Main frontend page
├── static/
│   └── style.css          # (Optional) custom styles
└── README.md              # You’re reading it!
```

---

## 📦 Requirements

Install Python dependencies:

```bash
pip install -r requirements.txt
```

**requirements.txt** contains:

```txt
Flask
opencv-python
deepface
numpy
```

---

## ▶️ How to Run

1. **Start the Flask server:**

```bash
python app.py
```

2. **Open your browser:**

Visit `http://localhost:5000`

3. **Allow camera access:**

Your browser will prompt for webcam permissions.

---

## 💬 Emotions Detected

The following emotions are detected by DeepFace and mapped to emojis:

| Emotion  | Emoji |
| -------- | ----- |
| happy    | 😄    |
| sad      | 😢    |
| angry    | 😠    |
| surprise | 😲    |
| disgust  | 🤢    |
| fear     | 😨    |
| neutral  | 😐    |

---

## 🧪 Development Notes

* Uses `navigator.mediaDevices.getUserMedia` to stream webcam.
* Uses `<canvas>` to capture frames from the video feed.
* Sends base64 JPEG image to Flask backend for analysis.
* Frontend updates DOM every 2 seconds with emotion + emoji.

---

## 🔧 Future Improvements

* [ ] Draw emoji or text bubble **near the detected face**
* [ ] Support multiple faces with individual emotions
* [ ] Add live charts to show emotional trends
* [ ] Deploy to Heroku, Render, or Docker

---

## 🛡️ Privacy

All processing is local and temporary — no images are saved or transmitted externally. Webcam access is browser-isolated and only granted with your permission.

---

## 🧑‍💻 Author

**Kalmin**
Motivated software developer passionate about combining AI and web technologies to create interactive tools.

---

## 📄 License

This project is licensed under the MIT License.
Feel free to use, modify, and share!

---

Let me know if you want me to include:

* A GIF demo
* Deployment instructions (Render, Docker, Heroku)
* A CLI version of this tool
