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

<!-- Add demo screenshots or GIFs here if available -->

---

## 💡 How It Works

1. **Face Detection**  
   - Captures live frames using OpenCV  
   - Detects faces using Haar cascades or CNN models  

2. **Face Recognition**  
   - Compares input face with stored encodings  
   - Identifies or labels unknown faces  

3. **Database Integration**  
   - MongoDB stores user info and attendance logs  
   - Real-time updates ensure accurate tracking  

4. **User Interface (Optional)**  
   - Register new users  
   - View attendance records  
   - Search or delete entries  

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
