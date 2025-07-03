# 🎭 Real-Time Emotion Detection Web App

A web-based application that uses your **webcam** to detect your **facial expressions in real time** and displays your **current emotion with a matching emoji**.

This app leverages **OpenCV** for face detection and **DeepFace** for emotion recognition — all running on a **Flask backend** with a sleek **HTML/JavaScript frontend**.

> **Note:** The current version **does not draw rectangles** around faces yet; it only displays the detected emotion and emoji.

---

## ✨ Demo

> When you open the camera stream in your browser:
>
> * Your dominant emotion (e.g., “happy” 😊 or “sad” 😢) is displayed in real time.
> * If no face is detected, a fallback message appears.
> * No bounding boxes or rectangles are drawn around the face yet.

---

## 🧠 How It Works

### 🔍 1. **Face Detection**

* Your browser captures video from your webcam.
* A frame is sent every 2 seconds to the Flask server.
* OpenCV's Haar Cascade (`haarcascade_frontalface_default.xml`) detects the face location.

### 🤖 2. **Emotion Recognition**

* The detected face is cropped and passed to **DeepFace**.
* DeepFace returns the **dominant emotion** (e.g., `happy`, `neutral`, `sad`, etc.)

### 🎨 3. **Frontend Display**

* The detected emotion is shown on the webpage with a matching **emoji**.
* No rectangles or overlays are drawn around the face yet.

---

## 🖼️ Screenshot

![demo](https://your-screenshot-url.com/demo.png) <!-- Replace with your actual screenshot -->

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
└── README.md              # This file
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

Go to `http://localhost:5000`

3. **Allow camera access:**

Grant permission when your browser asks for webcam access.

---

## 💬 Emotions Detected

DeepFace recognizes these emotions and they map to the following emojis:

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

* Uses `navigator.mediaDevices.getUserMedia` to stream webcam video.
* Captures frames using an HTML `<canvas>`.
* Sends base64-encoded JPEG frames to Flask backend every 2 seconds.
* Frontend updates the displayed emotion and emoji dynamically.
* **Rectangle drawing around faces is not yet implemented.**

---

## 🔧 Future Improvements

* [ ] Draw green rectangles around detected faces.
* [ ] Draw emoji or text bubbles near faces.
* [ ] Support multiple faces with individual emotions.
* [ ] Add live emotion trend charts.
* [ ] Deploy with Docker, Heroku, or Render.

---

## 🛡️ Privacy

All processing is local and temporary — no images are saved or sent externally. Webcam access requires your permission and is restricted to your browser session.

---

## 🧑‍💻 Author

**Kalmin**
Motivated software developer passionate about AI and web technologies.

---

## 📄 License

MIT License — Feel free to use, modify, and share!
