# gesture-detection-opencv

# Gesture & Body Detection with OpenCV & MediaPipe
![Screencast from 2025-02-12 19-44-33](https://github.com/user-attachments/assets/f5474ee1-5801-49b9-a5e6-bb4460962132)

## 📌 Project Overview
This project uses **OpenCV** and **MediaPipe** to detect:
- **Hand gestures**
- **Finger counting**
- **Body gestures (e.g., raised arms)**

It captures real-time video from a webcam, processes the frames to identify hands and body movements, and displays the results on-screen.

---

## 🖥 System Information
- **Operating System:** Ubuntu (Linux)
- **Working Environment:** Terminal (Command Line)
- **Virtual Environment:** `projects` (Python Virtual Environment)
- **Programming Language:** Python 3

---

## 📂 Project Setup & Installation

### **1️⃣ Clone the Repository**
```bash
cd ~/Documents/workshop
git clone https://github.com/atharvakanchan25/gesture-detection-opencv.git
cd gesture-detection-opencv
```

### **2️⃣ Set Up a Virtual Environment**
```bash
python3 -m venv projects
source projects/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install opencv-python mediapipe numpy
```
Save the dependencies for future use:
```bash
pip freeze > requirements.txt
```

---

## 🚀 Running the Project

### **Start Gesture & Body Detection**
```bash
python gesture_detection.py
```
Press **'q'** to exit.

---

## 🔬 How It Works
1. **Captures frames from the webcam.**
2. **Processes frames using OpenCV & MediaPipe.**
3. **Detects hand and body landmarks.**
4. **Counts raised fingers based on y-coordinates.**
5. **Checks for specific body gestures (e.g., raised arm).**
6. **Displays detection results on the video feed.**

---

## 📤 Pushing Updates to GitHub
```bash
git add .
git commit -m "Updated README and detection script"
git push origin main
```

---

## 🔗 References
- [OpenCV Documentation](https://docs.opencv.org/)
- [MediaPipe Hands](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)
- [MediaPipe Pose](https://developers.google.com/mediapipe/solutions/vision/pose_landmarker)

---

## 💡 Future Improvements
- Add **gesture classification** for more hand signs.
- Implement **gesture-based controls** (e.g., volume control with hand gestures).
- Improve **body gesture detection** for full-body tracking.

🚀 **Happy Coding!**
