from pymongo import MongoClient






#---------------------------------------------------------------------------------------------


from dotenv import load_dotenv
import os

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")


#---------------------------------------------------------------------------------------------



# MongoDB connection string (replace with your own credentials)
connection_string = mongo_uri

# Connect to MongoDB
client = MongoClient(connection_string)

# Select the database and collection
db = client['AttendanceDB']  # MongoDB database name
students_collection = db['Students']  # MongoDB collection name

# Data to insert
data = {
    "1": dict(name="Harshal", Department="IT", starting_year=2022, total_attendance=73, standing="G", year=4,
              last_attendance_time="2025-2-2 00:54:34"),
    "2": dict(name="Elon Musk", Department="IT", starting_year=2022, total_attendance=12, standing="G", year=4,
              last_attendance_time="2025-2-2 00:54:34"),
    "3": dict(name="sundar", Department="IT", starting_year=2022, total_attendance=24, standing="G", year=4,
              last_attendance_time="2025-2-2 00:54:34"),
    # "4": dict(name="OMKAR", Department="IT", starting_year=2022, total_attendance=1, standing="G", year=4,
    #           last_attendance_time="2025-2-2 00:54:34"),
    "4": dict(name="Papa", Department="IT", starting_year=2022, total_attendance=1, standing="G", year=4,
              last_attendance_time="2025-2-2 00:54:34"),
    "5": dict(name="Mummy", Department="IT", starting_year=2022, total_attendance=1, standing="G", year=4,
              last_attendance_time="2025-2-2 00:54:34"),
    
    "6": dict(name="Unnati", Department="IT", starting_year=2022, total_attendance=1, standing="G", year=4,
              last_attendance_time="2025-2-2 00:54:34")
    

}

# Insert the data into the collection
for key, value in data.items():
    # Insert each student as a new document in MongoDB
    students_collection.update_one(
        {"_id": key},  # Match by student ID
        {"$set": value},  # Update the document
        upsert=True  # If the document does not exist, insert a new one
    )

print("Data inserted successfully into MongoDB!")
