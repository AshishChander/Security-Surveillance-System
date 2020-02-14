import tkinter
import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import os
import time
from tkinter import messagebox
import datetime
from datetime import datetime
import sys


top=None
tbox=None
filename=''
conn=sqlite3.connect('criminalDb.db')
c=conn.cursor()

def displaySpec(name1):
     sql='select * from criminal where name="'+str(name1)+'"'
     c.execute(sql )
     global record
     record=c.fetchone()
     return record
    
def clear_history():
     pass


def search_history(ent1,ent2):
     global top,tbox
     search_date=ent1
     search_loc=ent2
     conn=sqlite3.connect('criminalDb.db')
     c=conn.cursor()
     tup=(search_date,search_loc)
     sql='''select name,TLevel,LastKnownTime,offence from criminal WHERE LastknownDate=? AND LastKnownLoc=?'''
     c.execute(sql,tup)
     rows=c.fetchall()
     try:
          col=len(rows[0])
          row=len(rows)
     except:
          messagebox.showinfo("invalid","Record Doesnt Exist!")
          return
     #print(rows[0][0])
     #a=0;b=20;c=23;d=33
     xp = 60
     yp = 190
     l = Label(top,text="NAME",font="Times 10 normal").place(x=60,y=160, width=120, height=25)
     l = Label(top,text="THREAT LEVEL",font="Times 10 normal").place(x=185,y=160, width=120, height=25)
     l = Label(top,text="LAST SEEN",font="Times 10 normal").place(x=310,y=160, width=120, height=25)
     l = Label(top,text="COMITTED CRIMES",font="Times 10 normal").place(x=435,y=160, width=200, height=25)
     
     for i in range(row+1):
          yp+=30
          xp = 60
          for j in range(col):
               
               if j == 3:
                    l = Text(top,font='none 10 normal')
                    l.delete(0.0,END)
                    try:
                         string=str(rows[i][j])
                         l.configure(state='normal')
                         l.insert(0.0,string)
                    except:
                         l.configure(background='black')
                         pass
                    l.configure(state='disabled')
                    #l.configure(width=400, height=25)
                    l.place(x=xp,y=yp, width=200, height=25)
                    
               else:
                    l = Text(top,font='none 10 normal')
                    l.delete(0.0,END)
                    try:
                         string=str(rows[i][j])
                         l.configure(state='normal')
                         l.insert(0.0,string)
                    except:
                         l.configure(background='black')
                         pass
                    l.configure(state='disabled')
                    l.place(x=xp,y=yp,width=120, height=25)
                    xp+=125
                    
               
               


     
class display:
    def clear(self):
        #clear all field in section C
        
        self.text9.delete(0,END)

        self.text10.configure(state='normal') 
        self.text10.delete(0.0,END)
        self.text10.configure(state='disabled')


        self.text6.configure(state='normal')
        self.text6.delete(0.0,END)
        self.text6.configure(state='disabled')


        self.text5.configure(state='normal')
        self.text5.delete(0.0,END)
        self.text5.configure(state='disabled')


        self.text2.configure(state='normal')
        self.text2.delete(0.0,END)
        self.text2.configure(state='disabled')


        self.text4.configure(state='normal')
        self.text4.delete(0.0,END)
        self.text4.configure(state='disabled')


        self.text3.configure(state='normal')
        self.text3.delete(0.0,END)
        self.text3.configure(state='disabled')


    def setcolor(self,lvl):
        
        if lvl==1:
            self.frameimage.configure(background='yellow')
            
        elif lvl== 2:
            self.frameimage.configure(background='yellow2')
            
        elif lvl== 3:
            self.frameimage.configure(background='tomato')
            
        elif lvl== 4:
            self.frameimage.configure(background='orange')
            
        elif lvl== 5:
            self.frameimage.configure(background='red')
            
        else:
            self.frameimage.configure(background='black')

    def clearimg(self):
        try: 
             self.panel3.destroy()
        except:
             pass
        self.frameimage.configure(background='black')
        self.clear()
        
    def search(self):

        global filename
        name=str(self.text9.get())
        records=displaySpec(name)
       
        if records!=None:

            lvl=records[2]
            self.clear()
            filename=str(records[6])
            
            self.img3=Image.open(filename)
            self.img3=self.img3.resize((180,200),Image.ANTIALIAS)
            self.img3=ImageTk.PhotoImage(self.img3)
            self.panel3=Label(window,image=self.img3,width=180,height=200)
            self.panel3.place(x=905,y=165)
            self.setcolor(lvl)
            
            self.text10.configure(state='normal')
            self.text10.insert(0.0,"   "+records[0])
            self.text10.configure(state='disabled')

            self.text6.configure(state='normal')
            self.text6.insert(0.0,"   "+records[5])
            self.text6.configure(state='disabled')

            self.text5.configure(state='normal')
            self.text5.insert(0.0,"   "+records[4]+"  "+records[7])
            self.text5.configure(state='disabled')

            self.text2.configure(state='normal')
            self.text2.insert(0.0,"   "+records[1])
            self.text2.configure(state='disabled')

            self.text4.configure(state='normal')
            self.text4.insert(0.0,"   "+records[3])
            self.text4.configure(state='disabled')

            self.text3.configure(state='normal')
            self.text3.insert(0.0,"   "+str(records[2]))
            self.text3.configure(state='disabled')
            
        else:
            self.clearimg()
            messagebox.showinfo("invalid","Record Doesnt Exist!")
    

    def Next(self):

        # next image
        
        #if self.count==8:
            #sys.exit()
        #if self.count<2:    
          nextpic=self.count
          nextpic+=3
          img=Image.open("D:\\ASHSIH\\PROJECTS\\version2\\Ryy\\"+"r"+str(nextpic)+".jpg")
          img=img.resize((540,350),Image.ANTIALIAS)
          self.my_images1.append(ImageTk.PhotoImage(img))

        # change image
          self.canvas1.itemconfig(self.image_on_canvas1, image = self.my_images1[self.count])
          window.after(5000,self.Next2)
        
    def Next2(self):

        # next image
        
        #if self.count==8:
            #sys.exit()
        #if self.count<2:    
          nextpic=self.count
          nextpic+=3


          img=Image.open("Processed/"+"p"+str(nextpic)+".jpg")
          img=img.resize((540,350),Image.ANTIALIAS)
          self.my_images2.append(ImageTk.PhotoImage(img))
        # change image
          self.canvas2.itemconfig(self.image_on_canvas2, image = self.my_images2[self.count])
          self.count+=1
          window.after(5000,self.Next) 

   
#------------------------------------------------------------------
             
    def __init__(self,window):

         self.canvas1=Canvas(window,width=640,height=360)
         self.canvas1.configure(background='black')
         self.canvas1.place(x=70,y=10)

#------------------------------------------------------
 
         self.canvas2=Canvas(window,width=640,height=360)
         self.canvas2.configure(background='black')
         self.canvas2.place(x=70,y=385)
        
#------------------------------------------------------------------
        # images
         self.my_images1 = []
         img=Image.open("D:\\ASHSIH\\PROJECTS\\version2\\Ryy\\r1.jpg")
         img=img.resize((540,350),Image.ANTIALIAS)
         self.my_images1.append(ImageTk.PhotoImage(img))
         img=Image.open("D:\\ASHSIH\\PROJECTS\\version2\\Ryy\\r2.jpg")
         img=img.resize((540,350),Image.ANTIALIAS)
         self.my_images1.append(ImageTk.PhotoImage(img))
         self.count = 0
         
#-------------------------------------------------------

         self.my_images2 = []
         img=Image.open("Processed/p1.jpg")
         img=img.resize((540,350),Image.ANTIALIAS)
         self.my_images2.append(ImageTk.PhotoImage(img))
         img=Image.open("Processed/p2.jpg")
         img=img.resize((540,350),Image.ANTIALIAS)
         self.my_images2.append(ImageTk.PhotoImage(img))
         
        # set first image on canvas
         self.image_on_canvas1 = self.canvas1.create_image(50,7,  anchor = NW, image = self.my_images1[self.count])
         self.image_on_canvas2 = self.canvas2.create_image(50,7, anchor = NW, image = self.my_images2[self.count])

#------------------------------------------------------
 



         
#Frame for the Side Section C

       
         self.label1=Label(window, text="Search Criminal Records",bg='black',fg='white',font='Times 20 bold ')
         self.label1.place(x=840,y=8)
         
#Side Section C contents

         self.text9=Entry(window,width='30',bg='black',fg='white',font='none 12 bold')
         self.text9.pack(ipady=10)
         self.text9.place(x=855,y=60)
         

         
         self.search=Button(window,text='Search',width=10,height=1,bg='red',fg='white',font='none 14 bold',command=self.search)
         self.search.place(x=855,y=100)
         
         self.reset=Button(window,text='Clear',width=10,height=1,bg='red',fg='white',font='none 14 bold',command=self.clearimg)
         self.reset.place(x=1000,y=100)
         
    
#Suspect Image Frame
         self.frameimage=Frame(window,width=195,height=215)
         self.frameimage.configure(background='black')
         self.frameimage.place(x=900,y=160)

#Suspect PrisonerID Label
         self.label10=Label(window,text='ID :',bg='black',fg='white',font='none 12 bold')
         self.label10.place(x=820,y=400)
         self.text10=Text(window,width=30,height=2,bg='black',fg='white',font='none 12 normal',state='disabled')
         self.text10.place(x=900,y=400)
         

#Suspect Name Label
         self.label2=Label(window,text='Name :',bg='black',fg='white',font='none 12 bold')
         self.label2.place(x=820,y=450)
         self.text2=Text(window,width=30,height=2,bg='black',fg='white',font='none 12 normal',state='disabled')
         self.text2.place(x=900,y=450)
         

#Suspect Wanted Level Label
         self.label3=Label(window,text='Level :',bg='black',fg='white',font='none 12 bold')
         self.label3.place(x=820,y=500)
         self.text3=Text(window,width=30,height=2,bg='black',fg='white',font='none 12 normal',state='disabled')
         self.text3.place(x=900,y=500)
         

#Suspect Crime/offence Type
         self.label4=Label(window,text='Offence :',bg='black',fg='white',font='none 12 bold')
         self.label4.place(x=820,y=550)
         self.text4=Text(window,width=30,height=2,bg='black',fg='white',font='none 12 normal',state='disabled')
         self.text4.place(x=900,y=550)
         

#Last Found Date
         self.label5=Label(window,text='Date :',bg='black',fg='white',font='none 12 bold')
         self.label5.place(x=820,y=600)
         self.text5=Text(window,width=30,height=2,bg='black',fg='white',font='none 12 normal',state='disabled')
         self.text5.place(x=900,y=600)
         

         
#Last Known Location
         self.label6=Label(window,text='Last Known Location :',bg='black',fg='white',font='none 12 bold')
         self.label6.place(x=820,y=650)
         self.text6=Text(window,width=30,height=2,bg='black',fg='white',font='none 12 normal')
         self.text6.place(x=900,y=680)
         


#------------------------------------------------------------------
         
         self.Next()






#Main Window 
window=Tk()
window.title("Security Surveillance System - S3")
window.geometry('1250x770')
window.resizable(0,0)
window.configure(background='black')

#-------------------------------------------------------
#Main menu bar

menubar=Menu(window)
live=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Live',menu=live)

history=Menu(menubar,tearoff=0)

def popup_history():
     global top,tbox
     top=Toplevel(window)
     top.title("Date wise Records")
     top.geometry('700x600')
     top.resizable(0,0)
     top.configure(background='black')
     #tbox=Text(top,width=300,height=4,bg='blue',fg='white',text='',font='none 10 bold').place(x=50,y=120)
     mystring =StringVar(top)
     mystring1 =StringVar(top)
     lbl1=Label(top,bg='black',fg='white',text="Enter Date : ",font='none 10 bold').place(x=20,y=20)
     ent1=Entry(top,width=20,textvariable = mystring).place(x=160,y=20)
     lbl2=Label(top,bg='black',fg='white',text="Enter Location : ",font='none 10 bold').place(x=20,y=50)
     ent2=Entry(top,width=20,textvariable = mystring1).place(x=160,y=50)   
     submit = Button(top,width=10,height=1,text="Search", fg="white", bg="Red",font='none 10 bold',command=lambda:search_history(mystring.get(),mystring1.get()))
     submit.place(x=60,y=80)
     
     #tbox=Text(top,width=100,height=4,bg='blue',fg='white',font='none 10 bold')
     #tbox.place(x=50,y=120)
     top.mainloop()
    
menubar.add_cascade(label='History',menu=history)
history.add_command(label="HISTORY",command=popup_history)




window.config(menu=menubar)
mb=display(window)
window.mainloop()
