#LetsGO
from tkinter import *
lightBG='light slate blue'
def secondIN():
    #global name, board, reg, section, stream,  level, name, reg, section, level, info, first, gender
    #global 
    second = Tk(className=" Quizi")
    #second.wm_attributes('-fullscreen', 'true')
    bg = PhotoImage(master=second,file="bg.png")
    Label(second, image=bg).place(relwidth=1, relheight=1)
    close = PhotoImage(master=second, file="close.png")
    Button(second, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=second.destroy).place(x=1320,y=10)

    Label(second,text="Enter Your Academic Details", font=("Courier",30,"bold underline"),bg=lightBG, fg="#27292b").place(x=350,y=25)
    
    Label(second, text="Subject", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=480, y=100)   
    Label(second, text="Theory", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=660, y=100)
    Label(second, text="Practical", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=810, y=100)
    Label(second, text="Attendance", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=985,y=100)
    Label(second, text="Project", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=1150, y=100)

    Label(second, text="Language I(ENG)", fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=140)
    Label(second, text="Language II", fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=180)
    if(streamVal==1):
        Label(second, text="Mathematics",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=220)
    elif(streamVal==2):
        Label(second, text="History",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=220)
    else:
        Label(second, text="Accountancy",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=220)

    if(streamVal==1):
        Label(second, text="Physics",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=260)
    elif(streamVal==2):
        Label(second, text="Geography",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=260)
    else:
        Label(second, text="Economics",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=260)

    if(streamVal==1):
        Label(second, text="Chemistry",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=300)
    elif(streamVal==2):
        Label(second, text="Political Sci.",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=300)
    else:
        Label(second, text="Business Std.",fg="#27292b",font=("Courier",14,"bold"), bg=lightBG).place(x=490,y=300)


        
    

#subject marks::
    sub1T=IntVar()
    sub1Prc=IntVar()
    sub1A=IntVar()
    sub1P=IntVar()
      
    sub1T=Entry(second,font=("Arial",14))
    sub1T.place(x=660,y=140)
    sub1Prc=Entry(second,font=("Arial",14))
    sub1Prc.place(x=810,y=140)
    sub1A=Entry(second,font=("Arial",14))
    sub1A.place(x=980,y=140)
    sub1P=Entry(second,font=("Arial",14))
    sub1P.place(x=1120,y=140)
    
    sub1Tv=sub1T.get()
    sub1Prcv=sub1Prc.get()
    sub1Av=sub1A.get()
    sub1Pv=sub1P.get()        
    sub1=[]
    sub1.extend([sub1Tv,sub1Prcv,sub1Av,sub1Pv])
#sub2
    sub2T=IntVar()
    sub2Prc=IntVar()
    sub2A=IntVar()
    sub2P=IntVar()
        
    sub2T=Entry(second,font=("Arial",14))
    sub2T.place(x=660,y=180)
    sub2Prc=Entry(second,font=("Arial",14))
    sub2Prc.place(x=810,y=180)
    sub2A=Entry(second,font=("Arial",14))
    sub2A.place(x=980,y=180)
    sub2P=Entry(second,font=("Arial",14))
    sub2P.place(x=1120,y=180)
    
    sub2Tv=sub1T.get()
    sub2Prcv=sub1Prc.get()
    sub2Av=sub1A.get()
    sub2Pv=sub1P.get()        
    sub2=[]
    sub2.extend([sub2Tv,sub2Prcv,sub2Av,sub2Pv])
#sub3
    sub3T=IntVar()
    sub3Prc=IntVar()
    sub3A=IntVar()
    sub3P=IntVar()
      
    sub3T=Entry(second,font=("Arial",14))
    sub3T.place(x=660,y=220)
    sub3Prc=Entry(second,font=("Arial",14))
    sub3Prc.place(x=810,y=220)
    sub3A=Entry(second,font=("Arial",14))
    sub3A.place(x=980,y=220)
    sub3P=Entry(second,font=("Arial",14))
    sub3P.place(x=1120,y=220)
    
    sub3Tv=sub1T.get()
    sub3Prcv=sub1Prc.get()
    sub3Av=sub1A.get()
    sub3Pv=sub1P.get()        
    sub3=[]
    sub3.extend([sub3Tv,sub3Prcv,sub3Av,sub3Pv])

#sub4
    sub4T=IntVar()
    sub4Prc=IntVar()
    sub4A=IntVar()
    sub4P=IntVar()
      
    sub4T=Entry(second,font=("Arial",14))
    sub4T.place(x=660,y=260)
    sub4Prc=Entry(second,font=("Arial",14))
    sub4Prc.place(x=810,y=260)
    sub4A=Entry(second,font=("Arial",14))
    sub4A.place(x=980,y=260)
    sub4P=Entry(second,font=("Arial",14))
    sub4P.place(x=1120,y=260)
    
    sub4Tv=sub1T.get()
    sub4Prcv=sub1Prc.get()
    sub4Av=sub1A.get()
    sub4Pv=sub1P.get()        
    sub4=[]
    sub4.extend([sub4Tv,sub4Prcv,sub4Av,sub4Pv])

#sub5
    sub5T=IntVar()
    sub5Prc=IntVar()
    sub5A=IntVar()
    sub5P=IntVar()
      
    sub5T=Entry(second,font=("Arial",14))
    sub5T.place(x=660,y=300)
    sub5Prc=Entry(second,font=("Arial",14))
    sub5Prc.place(x=810,y=300)
    sub5A=Entry(second,font=("Arial",14))
    sub5A.place(x=980,y=300)
    sub5P=Entry(second,font=("Arial",14))
    sub5P.place(x=1120,y=300)
    
    sub5Tv=sub5T.get()
    sub5Prcv=sub5Prc.get()
    sub5Av=sub5A.get()
    sub5Pv=sub5P.get()        
    sub5=[]
    sub5.extend([sub5Tv,sub5Prcv,sub5Av,sub5Pv])

secondIN()
