
import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import gridfs
from pymongo import MongoClient
from datetime import datetime, timedelta
import time



#---------------------------------------------------------------------------------------------

from dotenv import load_dotenv
import os

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")


#---------------------------------------------------------------------------------------------
# MongoDB connection stringH
connection_string = mongo_uri

# Connect to MongoDB
client = MongoClient(connection_string)
db = client['AttendanceDB']
students_collection = db["Students"]
fs = gridfs.GridFS(db)

from EncodeGenerator import encodeListKnownwithIds

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imBackground = cv2.imread('Resources/background.png')

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = [cv2.imread(os.path.join(folderModePath, path)) for path in modePathList]

# Load the encoding file
file = open('EncodeFile.p', 'rb')
encodeListKnown, studentsIds = pickle.load(file)
file.close()

modeType = 0
counter = 0
id = 0
imgStudent = []

while True:
    success, img = cap.read()

    # Reduce frame size for faster face detection
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurrFrame = face_recognition.face_locations(imgS)
    encodeCurrFrame = face_recognition.face_encodings(imgS, faceCurrFrame)

    # Display webcam feed on the background
    imBackground[162:162 + 480, 55:55 + 640] = img
    imBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurrFrame:
        for encodeFace, faceLoc in zip(encodeCurrFrame, faceCurrFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance=0.6)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imBackground = cvzone.cornerRect(imBackground, bbox, rt=0)
                id = studentsIds[matchIndex]

                if counter == 0:
                    cvzone.putTextRect(imBackground, "Loading...", (275, 600))
                    cv2.imshow("Face Attendance", imBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

    if counter != 0:
        if counter == 1:
            # Fetch student data from MongoDB
            studentInfo = db['Students'].find_one({"_id": id})

            # Fetch the image from GridFS
            file_data = fs.find_one({"filename": f"{id}.png"})
            imgStudent = None
            if file_data:
                img_data = file_data.read()
                img_array = np.frombuffer(img_data, np.uint8)
                imgStudent = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            # Attendance management with a 30-second restriction
            student_info = students_collection.find_one({"_id": id})
            if student_info:
                last_attendance_str = student_info.get("last_attendance_time")
                current_time = datetime.now()

                if last_attendance_str:
                    last_attendance_time = datetime.strptime(last_attendance_str, "%Y-%m-%d %H:%M:%S")

                    if (current_time - last_attendance_time) > timedelta(seconds=30):
                        student_info = students_collection.find_one_and_update(
                            {"_id": id},
                            {
                                "$inc": {"total_attendance": 1},
                                "$set": {"last_attendance_time": current_time.strftime("%Y-%m-%d %H:%M:%S")}
                            },
                            return_document=True
                        )
                        print(f"Updated student attendance: {student_info['total_attendance']} at {student_info['last_attendance_time']}")
                    else:
                        print("Attendance update is restricted. Please wait 30 seconds.")
                        modeType = 3
                        counter = 0
                        imBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
                        continue

                else:
                    student_info = students_collection.find_one_and_update(
                        {"_id": id},
                        {
                            "$inc": {"total_attendance": 1},
                            "$set": {"last_attendance_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                        },
                        return_document=True
                    )
                    print(f"First attendance recorded: {student_info['total_attendance']} at {student_info['last_attendance_time']}")

        if modeType != 3:
            if 10 < counter < 20:
                modeType = 2
                imBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

            if counter <= 10:
                # Update the background image with student data
                cv2.putText(imBackground, str(studentInfo['total_attendance']), (861, 125), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(imBackground, str(studentInfo['Department']), (1006, 550), cv2.FONT_HERSHEY_COMPLEX, 0.55, (255, 255, 255), 2)
                cv2.putText(imBackground, str(id), (1006, 493), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
                cv2.putText(imBackground, str(studentInfo['standing']), (910, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 2)
                cv2.putText(imBackground, str(studentInfo['year']), (1025, 625), cv2.FONT_HERSHEY_COMPLEX, 1, (100, 100, 100), 2)
                cv2.putText(imBackground, str(studentInfo['starting_year']), (1125, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 2)
                (w, h), _ = cv2.getTextSize(studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                offset = (414 - w) // 2
                cv2.putText(imBackground, str(studentInfo['name']), (808 + offset, 445), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 2)

                if imgStudent is not None:
                    imgStudent_resized = cv2.resize(imgStudent, (216, 216))
                    imBackground[175:175 + 216, 909:909 + 216] = imgStudent_resized

            counter += 1
            if counter >= 20:
                counter = 0
                modeType = 0
                studentInfo = None
                imgStudent = None
                imBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
        else:
            # Reset variables after mode 3
            counter = 0
            modeType = 0
            id = 0
            studentInfo = None
            imgStudent = None
            imBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    cv2.imshow("Face Attendance", imBackground)
    cv2.waitKey(1)
