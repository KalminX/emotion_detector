const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const emotionOutput = document.getElementById("emotion-output");

// Emotion to emoji map
const emojiMap = {
  angry: "😠",
  disgust: "🤢",
  fear: "😨",
  happy: "😄",
  sad: "😢",
  surprise: "😲",
  neutral: "😐",
};

navigator.mediaDevices
  .getUserMedia({ video: true })
  .then((stream) => {
    video.srcObject = stream;
    setInterval(captureAndSend, 2000); // every 2 seconds
  })
  .catch((err) => {
    alert("Could not access webcam.");
    console.error(err);
  });

function captureAndSend() {
  const context = canvas.getContext("2d");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  context.drawImage(video, 0, 0, canvas.width, canvas.height);

  const imageData = canvas.toDataURL("image/jpeg");

  fetch("/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image: imageData }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.success && data.emotions.length > 0) {
        const emotion = data.emotions[0].emotion.toLowerCase();
        const emoji = emojiMap[emotion] || "❓";
        emotionOutput.innerText = `Detected: ${emotion} ${emoji}`;
      } else {
        emotionOutput.innerText = "No face detected";
      }
    })
    .catch((err) => {
      console.error("Error analyzing frame:", err);
      emotionOutput.innerText = "Error analyzing emotion";
    });
}
