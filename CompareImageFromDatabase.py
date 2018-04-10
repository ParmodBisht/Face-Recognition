import face_recognition
import cv2
from sqlalchemy.sql import *
import psycopg2
import collections
import numpy as np

try:
    conn = psycopg2.connect("dbname='Testing' user='postgres' host='localhost' password='Popdiv99@12345'")
except:
    print ("I am unable to connect to the database")
cur = conn.cursor()
query1="select * from ImageRecognition"
cur.execute(query1)
rows=cur.fetchall()
data_from_table=[]
#fetching Data From Backend

for row in rows:
    data_from_table.append(row)


arr=np.array((data_from_table), dtype='<U32')
arr2 = [float(i) for i in arr[1][0]]
print(type(arr2))
print(arr2)
arr3=np.array(arr2)
print(type(arr3))
print(arr3.shape)


video_capture = cv2.VideoCapture(0)

while True:
    
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

   
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        match = face_recognition.compare_faces([arr3], face_encoding)

        name = "Unknown"
        if match[0]:
            name = "Matched"

        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    
    cv2.imshow('Video', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
