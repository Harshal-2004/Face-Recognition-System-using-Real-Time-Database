import cv2
import face_recognition
import pickle
import os
from pymongo import MongoClient
import gridfs



#---------------------------------------------------------------------------------------------

from dotenv import load_dotenv
import os

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")


#---------------------------------------------------------------------------------------------

# MongoDB connection string (replace with your actual connection string)
connection_string = mongo_uri

# Connect to MongoDB
client = MongoClient(connection_string)
db = client['AttendanceDB']  # Name of the database
fs = gridfs.GridFS(db)  # Create a GridFS object for storing files


# Importing the student images into a list
folderPath = 'images'
PathList = os.listdir(folderPath)
print(PathList)

imgList = []
studentsIds = []

for path in PathList:
    # Loading the image from the folder path
    img = cv2.imread(os.path.join(folderPath, path))

    # Check if the image is successfully loaded
    if img is None:
        print(f"Error: Unable to load image {path}")
        continue

    # Append the loaded image and student ID to respective lists
    imgList.append(img)
    studentsIds.append(os.path.splitext(path)[0])

    # Store image in GridFS (MongoDB's file storage)
    fileName = f'{folderPath}/{path}'
    with open(fileName, 'rb') as file:  # Open image file in binary mode
        fs.put(file, filename=path)  # Upload the image to MongoDB GridFS
        print(f"Uploaded {path} to GridFS")

# Print student IDs
print(studentsIds)


def findEncodings(imagesList):
    encodeList = []  # Initialize the list to store face encodings
    for img in imagesList:
        # Convert image to RGB (because OpenCV loads as BGR by default)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Get face encodings
        encodings = face_recognition.face_encodings(img_rgb)
        if encodings:
            encodeList.append(encodings[0])  # Add the first encoding to the list
        else:
            print("No faces detected in this image.")
    return encodeList



print("Encoding started...")

# Ensure you have loaded the images properly into imgList
encodeListKnown = findEncodings(imgList)
encodeListKnownwithIds = [encodeListKnown,studentsIds]
print('Encoding complete')

file=open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownwithIds, file)
file.close()


























# # #
# # # from pymongo import MongoClient
# # #
# # # # Replace with your connection string
# # # connection_string = "mongodb+srv://Admin:Harshal@cluster0.dgzs7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# # #
# # #
# # # # Connect to MongoDB
# # # client = MongoClient(connection_string)
# # # db = client.test  # Test connection
# # #
# # # # Print database names
# # # print("Databases:", client.list_database_names())
# #
# # from pymongo import MongoClient
# # import gridfs
# # import os
# #
# # # MongoDB connection string (replace with your connection string)
# # client = MongoClient("<your_connection_string>")
# # db = client["<your_database_name>"]  # Replace with your database name
# #
# # # Initialize GridFS for file storage
# # fs = gridfs.GridFS(db)
# #
# # # Folder containing images
# # folderPath = 'Images'  # Change this to your images folder
# # pathList = os.listdir(folderPath)
# #
# # # Loop through the images in the folder
# # for path in pathList:
# #     file_path = os.path.join(folderPath, path)
# #
# #     # Upload file to GridFS
# #     with open(file_path, 'rb') as file:
# #         file_id = fs.put(file, filename=path)  # Upload and store with filename
# #         print(f"Uploaded {path} to GridFS with file_id: {file_id}")
# #
# # # Verify if the file has been uploaded by checking fs.files collection
# # files = fs.find()  # Retrieve all files from GridFS
# # for file in files:
# #     print(file)  # Print file metadata
# Test MongoDB Query
from pymongo import MongoClient

# from datetime import datetime
#
# from AddDataToDatabase import db
#
# # Update total_attendance and last_attendance_time for _id "1"
# result = db['Students'].update_one(
#     {"_id": "1"},
#     {
#         "$set": {
#             "total_attendance": 2,
#             "last_attendance_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         }
#     }
# )
#
# print("Modified Count:", result.modified_count)
