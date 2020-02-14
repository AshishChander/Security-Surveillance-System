import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib
import shutil

HOST='192.168.43.90'
PORT=8000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')
a=0
conn,addr=s.accept()

data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))
while True:
    a=a+1
    while len(data) < payload_size:
        print("Recv: {}".format(len(data)))
        data += conn.recv(4096)

    print("Done Recv: {}".format(len(data)))
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    print("msg_size: {}".format(msg_size))
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    #cv2.imshow('ImageWindow',frame)
    moveit="D:\\ASHSIH\\PROJECTS\\version2\\Ryy\\"+"r"+str(a)+".jpg"
    savesource="D:\\ASHSIH\\PROJECTS\\version2\\Ry\\ "+"r"+str(a)+".jpg"
    cv2.imwrite(savesource,frame)
    shutil.move(savesource,moveit)
    cv2.waitKey(0)
    
