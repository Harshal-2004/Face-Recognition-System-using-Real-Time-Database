# 🎯 Face Recognition System using Real-Time Database

Welcome to the **Face Recognition System with MongoDB Integration** — a practical project that implements real-time face detection and recognition using Python. This project is ideal for real-world applications such as **attendance management**, **secure access**, and **live monitoring**.

---

## 🚀 Overview

This system enables you to:

- Detect and recognize faces from a **live webcam/video feed**
- Store and retrieve face data using a **real-time MongoDB database**
- Support use cases like **automated attendance marking**, **authentication**, and more

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV** (Face detection & recognition)
- **NumPy**
- **MongoDB** (Real-time database)
- **Tkinter** (Simple UI interface)
- Other Python libraries as needed

---

## 📦 Key Features

- ✅ Real-time face detection & recognition  
- ✅ Easy new face enrollment  
- ✅ Live attendance marking with timestamps  
- ✅ MongoDB real-time sync  
- ✅ Optional user interface for smooth interaction  
- ✅ Scalable & modular architecture

---

## 📸 Demo

## 📸 Demo

Below is a step-by-step demonstration of how the application works:

| Step | Screenshot | Caption |
|------|------------|---------|
| 1. Face Detected Encoded & Information Page | ![Step 1 Placeholder](demo/Sundar_Attend.png) | As soon as a face appears in the frame, the system detects and encodes the face data. || After encoding, an information window pops up showing user details and confirmation. |
| 2. Attendance Marked | ![Step 4 Placeholder](demo/Sundar_Marked.png) | The system marks attendance and displays a success message. |
| 3. Re-Entry Within 30 Seconds | ![Step 5 Placeholder](demo/sundar_Already.png) | If the same face is detected again within 30 seconds, a notification appears: "Already marked." |

---
## 💡 How It Works

### 📸 Face Detection
- Captures live video frames using OpenCV and your webcam.
- Utilizes **HOG-based face detection** (via the `face_recognition` library) for fast and accurate face location tracking in real time.

### 🧠 Face Recognition
- Encodes facial features using the `face_recognition` library.
- Compares detected faces against the database of stored face encodings.
- Automatically identifies known faces and marks unknown faces for registration or alert.

### 🗄️ Database Integration (MongoDB)
- Uses MongoDB to store:
  - User details (such as name, ID, and face encodings)
  - Real-time attendance logs with timestamps
- Ensures data persistence, instant updates, and easy retrieval of attendance history.

### 🖥️ User Interface (Optional)
- Register new users directly via webcam.
- View, search, and manage attendance records.
- Delete or update specific entries from the database through a simple UI.

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Harshal-2004/Face-Recognition-System-using-Real-Time-Database.git
cd Face-Recognition-System-using-Real-Time-Database
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Database

- Set up your MongoDB cluster (e.g., MongoDB Atlas)
- Replace the connection string inside `config.py` with your MongoDB URI

### 4️⃣ Run the Application

```bash
python main.py
```

Use the CLI or GUI to enroll users and start recognition.

---

## 🔒 Security & Privacy

> ⚠️ This project is for educational/demo purposes.  
> If deploying in production, ensure:
> - Proper encryption of data
> - Compliance with local data privacy laws
> - Secure access controls

---

## 👤 Author

**Harshal Shirole**  
[GitHub Profile](https://github.com/Harshal-2004)

---

## 📝 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## ⭐ Show Your Support

If you found this project helpful or inspiring, please give it a ⭐ on GitHub and feel free to fork and contribute!
