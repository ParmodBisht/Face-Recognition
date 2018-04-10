import face_recognition
import cv2
from sqlalchemy.sql import *
import psycopg2


TEST_IMAGES = [
    "tarun.jpg"   
]
try:
    conn = psycopg2.connect("dbname='Testing' user='postgres' host='localhost' password='Popdiv99@12345'")
except:
    print ("I am unable to connect to the database")
    
cur = conn.cursor()

for k in TEST_IMAGES:
    my_image = face_recognition.load_image_file(k)
    my_face_encoding = face_recognition.face_encodings(my_image)[0]
    print(my_face_encoding)
    print (type(my_face_encoding))
    print (str(my_face_encoding))
    
    lst=list(my_face_encoding)
    #print(lst)
    #print(type(my_face_encoding))
    query1="insert into ImageRecognition values(ARRAY"+str(lst)+")"
    #print (query1)
    cur.execute(query1)
    #print (query1)
    conn.commit()


