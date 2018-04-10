import face_recognition
import cv2
from sqlalchemy.sql import *
import psycopg2




obama_image = face_recognition.load_image_file("pops.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

#lst=list(obama_face_encoding)
#print(lst)
#print(type(obama_face_encoding))
#for i in lst:
    #print(lst[i])


try:
    conn = psycopg2.connect("dbname='Testing' user='postgres' host='localhost' password='Pop'")
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()

query1="select * from tictactoe3"
cur.execute(query1)

data=cur.fetchall()
print(data)




