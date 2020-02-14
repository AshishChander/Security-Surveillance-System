import face_recognition
import cv2
import numpy as np
import pickle
person_name=person_encoding=input("enter person's name")
person_encoding+="_encoding"
known_face_encodings=[]
known_face_names=[] 
try:
    file_open=open(person_encoding,"rb")
    known_face_encodings=pickle.load(file_open)
    file_open.close()

    namesfile_open=open(person_name,"rb")
    known_face_names=pickle.load(namesfile_open)
    namesfile_open.close()
except:
    pass
file_open=open(person_encoding,"wb")
namesfile_open=open(person_name,"wb")

flag=True
while flag:        
    upload_image = face_recognition.load_image_file(input("image name with extension"))
    upload_face_encoding = face_recognition.face_encodings(upload_image)[0]
    name=person_name
    known_face_encodings.append(upload_face_encoding )
    known_face_names.append(name)
    flagch=input("want to upload more? y/n")
    if flagch!="y":
        break
pickle.dump(known_face_encodings,file_open)
file_open.close()

pickle.dump(known_face_names,namesfile_open)
namesfile_open.close()    


      
        
