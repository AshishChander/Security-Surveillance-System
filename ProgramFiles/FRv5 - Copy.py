import face_recognition
import cv2
import tkinter
from tkinter import *
from PIL import Image,ImageTk
import numpy as np
import pickle
import time
import threading
from threading import Timer
import sqlite3
import datetime
from datetime import  datetime
import serial
import os.path
import sys
import shutil


file=''
ser=serial.Serial('COM6',9600)
t1=None
root=None
count=0
loadpath='D:\\ASHSIH\\PROJECTS\\version2\\Ry\\'
movepath='D:\\ASHSIH\\PROJECTS\\version2\\Ryy\\'
savepath='D:\\ASHSIH\\PROJECTS\\version2\\Processed\\'
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
match_percentage=[]
start_time=time.time()
    # Grab a single frame of video
locate='BMSCE'    
flag=0
        
namesfile_open=open("all_ppl_name","rb");
known_face_names=pickle.load(namesfile_open)

def update_table(name):
    conn=sqlite3.connect('criminalDb.db')
    c=conn.cursor()
    now = datetime.now()
    CurrTime = now.strftime('%Y-%m-%d %H:%M:%S')
    time_date=CurrTime.split(' ')
    datee=time_date[0]
    timee=time_date[1]
    try:
        if name=='unknown':
            print(name)
            return
        c.execute("update criminal SET LastKnownTime= ?,LastKnownLoc=?,LastknownDate=? WHERE name=?",(timee,locate,datee,name))
        conn.commit()
        print('updated')
        conn.close()
    except Exception as e:
        print(e)
def raise_alert(name):
    conn=sqlite3.connect('criminalDb.db')
    c=conn.cursor()
    sql='''select * from criminal WHERE name=?'''
    c.execute(sql,(name,))
    row=c.fetchone()
    if row==None:
        return
    lvl=row[2]
    if lvl==5:
        #Serial.write
        #message3=b''
        #message2="Level 5 threat detected..! "+str(row[1])+" was found in "+str(row[5])+" at "+str(row[7])+" , "+str(row[4])
        #meassage3=b"str(message2)"
        ser.write(b'Level 5 Threat Detected')
        global flag
        flag=1
    conn.close()

def show_img(small_frame):
    global flag
    #print(small_frame)
    #try:
        #root.destroy()
    #except:
        #pass
    def kill():
        root.destroy()
    root=Tk()
    root.geometry("400x350")
    root.title("LEVEL 5 THREAT !!!")
    root.attributes('-topmost',True)
    root.configure(background='red')
    def toggle():
        root.configure(background='red')
        root.after(3,togg)
    def togg():
        root.configure(background='yellow')
        root.after(3,toggle)
    img=Image.open(small_frame)
    img=img.resize((380,330),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    panel1=Label(root,image=img,width=380,height=330)
    panel1.place(x=10,y=10)
    
    flag=0
    togg()
    root.after(8000,kill)
    root.mainloop()
         
def recognition():

    global count,process_this_frame
    count+=1
    #if count>8:
        #sys.exit()
        #pass
    source=loadpath+'r'+str(count)+'.jpg'
    moveit=movepath+'r'+str(count)+'.jpg'
    #shutil.move(source,moveit)
    dest=savepath+'p'+str(count)+'.jpg'
    
    small_frame =cv2.imread(moveit)
    #print(small_frame)
    # Resize frame of video to 1/4 size for faster face recognition processing
    #small_frame = cv2.resize(small_frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    
    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            #open file to save encoding
             
        
        face_names = []
        for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
            temp_distance=[]
            temp_names=[]
            temp_matches=[]
            encodings=[]
            names=[]
            
            name = "unknown"
            less="0"
            for i in known_face_names:
            
                    filename=str(i)+"_encoding"
                    namesfile_open=open(filename,"rb");
                    encodings=pickle.load(namesfile_open)
                    namesfile_open.close()
                    mat=face_recognition.compare_faces(encodings, face_encoding)
                    j=0
                    for flag1 in mat:
                        if flag1:
                            enc=[]
                            enc.append(encodings[j])
                            face_distances = face_recognition.face_distance(enc,face_encoding)
                            temp_distance.append(face_distances)
                            temp_names.append(i)
                            j+=1
                        else:
                            j+=1
                
                
            #print(temp_names)
            #print(temp_distance)
            try:
                best_match_index = np.argmin(temp_distance)
                notmatch=100*min(temp_distance)
                matching=100-notmatch
                if matching>55:
                    name = temp_names[best_match_index]
                    less="-"+str(int(100-notmatch))+"%"
                    name+=less
            except:
                pass
            face_names.append(name)


    for each_name in face_names:
        each_name=each_name.split('-')
        each_name=each_name[0]
        print(each_name)
        update_table(each_name)
        raise_alert(each_name)

        # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(small_frame, (left, top), (right, bottom), (0,0,255), 2)
            # Draw a label with a name below the face
        #cv2.rectangle(small_frame, (left-15, bottom), (right+25,bottom+25), (15,214,245), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(small_frame, name, (left-10, bottom+45), font,1.4,(0,0,255),2)
        # Display the resulting image
    cv2.imwrite(dest,small_frame)
    global flag,t1
    if flag==1:
        #show_img(dest)
        try:
            if t1.is_alive():
                print('alive')
                root.destroy()
                t1.cancel()
        except:
            pass
        t1=threading.Thread(target=show_img,args=(dest,))
        t1.start()

    print(time.time()-start_time)
    
    t=Timer(8.0,recognition)
    t.start()
recognition()
namesfile_open.close()
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()





















