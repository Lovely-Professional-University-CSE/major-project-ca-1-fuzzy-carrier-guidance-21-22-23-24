from tkinter import *
import sqlite3
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl



#==================================================


from tkcalendar import Calendar
from tkinter import ttk
import datetime

global listStr,listS1,listS2,listS3,listS4,listS5
global second, sub1T ,sub1Tv,sub1Prc,sub1A,sub1P
global sub2T,sub2Prc,sub2P,sub2A
global sub3T,sub3Prc,sub3P,sub3A
global sub4T,sub4Prc,sub4P,sub4A
global sub5T,sub5Prc,sub5P,sub5A
global sub1Tv, sub1Prcv, sub1Av, sub1Pv, sub1
global sub2Tv, sub2Prcv, sub2Av, sub2Pv, sub2
global sub3Tv, sub3Prcv, sub3Av, sub3Pv, sub3 
global sub4Tv, sub4Prcv, sub4Av, sub4Pv, sub4
global sub5Tv, sub5Prcv, sub5Av, sub5Pv, sub5
global streamVal
nameVal, boardVal , genVal, dobVal,dobVal="","", "", "",""
first, second, lb= None, None, None
lightBG, darkBG = "#eafde7", "#44484b"
splash = None
nik=None
name, reg, board, gender,dob , info,stream= None, None , None, None, None, None, None
cusFont = ("Times New Roman", 12, "bold")

#===============================================



def Home():
    global top,window
    if window==1:
        top.withdraw()
    window=1
    top=Toplevel()
    #top.geometry("1400x743+0+0")
    top.title("Home Page")
    image1 =PhotoImage(file="students.png")
    top.wm_attributes('-fullscreen', 'true')
    Form = Label(top, image=image1)
    Form.pack(side='top', fill='both', expand='yes')
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
    btn_login = Button(Form, text="Sign IN", width=25, command=login_window)
    btn_login.place(x=900, y=40)
    btn_login.bind('<Return>',login_window )
    top.mainloop()

def Signup_window():
    global top,window
    
    if window==1:
        top.withdraw()
    window=1
    
    global flag,USERNAME,PASSWORD,lbl_text 
    
    top=Toplevel()
    top.geometry("1400x700+0+0")
    top.title("SIGNUP")
    image1 =PhotoImage(file="Signup.png")
    top.wm_attributes('-fullscreen', 'true')
    Form1 = Label(top, image=image1)
    Form1.pack(side='top', fill='both', expand='yes')
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
    USERNAME = StringVar()
    PASSWORD = StringVar()
   

    lbl_username = Label(Form1, text = "Email ID:", font=(14), bd=10)
    lbl_username.place(x=450,y=350)
    lbl_password = Label(Form1, text = "Password:", font=(14), bd=10)
    lbl_password.place(x=450,y=430 )
    lbl_text = Label(Form1)
    lbl_text.grid(row=2, columnspan=2)

    
   
    username = Entry(Form1, textvariable=USERNAME, font=(14))
    username.place(x=570, y=360)
    password = Entry(Form1, textvariable=PASSWORD, show="*", font=(14))
    password.place(x=570, y=440)
    
    btn_Signup = Button(Form1, text="Sign Up", width=45, command=Signup)
    btn_Signup.place(x=450, y=500)
    btn_Signup.bind('<Return>', Signup)
    btn_login = Button(Form1, text="Sign IN", width=25, command=login_window)
    btn_login.place(x=900, y=40)
    btn_login.bind('<Return>',login_window )
    top.mainloop()
def Signup():
        
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        Database_Signup()
        lbl_home = Label(root, text="Successfully Registered!", font=(20)).pack()
        login_window()
    USERNAME.set("")
    PASSWORD.set("")
    #lbl_text.config(text="")
       
    
def Database_Signup():
    global conn, cursor,flag,USERNAME,PASSWORD
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("CREATE TABLE member (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        
    except:
        cursor.execute("INSERT INTO member (username, password) VALUES(?,?)",(USERNAME.get(), PASSWORD.get()))
        
    conn.commit()
    cursor.close()
    conn.close()
def login_window():
    global top,window
    if window==1:
        top.withdraw()
    window=1
    global flag,USERNAME,PASSWORD,lbl_text
    top=Toplevel()
    top.geometry("1400x700+0+0")
    top.title("Login")
    image1 =PhotoImage(file="login.png")
    top.wm_attributes('-fullscreen', 'true')
    Form = Label(top, image=image1)
    Form.pack(side='top', fill='both', expand='yes')
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
    USERNAME = StringVar()
    PASSWORD = StringVar()
    

    lbl_username = Label(Form, text = "Username:", font=(14), bd=10)
    lbl_username.place(x=50,y=450)
    lbl_password = Label(Form, text = "Password:", font=(14), bd=10)
    lbl_password.place(x=50,y=530 )
    lbl_text = Label(Form)
    lbl_text.grid(row=2, columnspan=2)

    
   
    username = Entry(Form, textvariable=USERNAME, font=(14))
    username.place(x=170, y=460)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
    password.place(x=170, y=540)
    
    flag=0
    btn_login = Button(Form, text="Login", width=45, command=Login)
    btn_login.place(x=50, y=600)
    btn_login.bind('<Return>', Login)
    btn_signup = Button(Form, text="New User Sign Up", width=25, command=Signup_window)
    btn_signup.place(x=900, y=40)
    btn_signup.bind('<Return>', Signup_window)
    top.mainloop()

    
def Database():
    global conn, cursor,flag
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("CREATE TABLE member (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("INSERT INTO member (username, password) VALUES('admin', 'admin')")
    except:
        cursor.execute("SELECT * FROM member WHERE username = ? AND password = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            flag=1
    conn.commit()
    cursor.close()
    conn.close()

    
    
def Login():
        
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        if flag==1:
            lbl_home = Label(root, text="Successfully Login!", font=(20)).pack()
            HomeWindow()
            
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    USERNAME.set("")
    PASSWORD.set("")
    #lbl_text.config(text="")

def HomeWindow():
    print("end")
    if window==1:
        top.withdraw()
    
    Fill_details()


def Fill_details():
    #letsGO
    #updated validation for subjects
    def Splash():
        global splash
        splash = Toplevel()
        splash.wm_attributes("-fullscreen","true")
        bg = PhotoImage(file="yu.png")
        Label(splash, image=bg).place(relwidth=1, relheight=1)
        close = PhotoImage(file="close.png")
        Button(splash, bd=0, image=close, bg="#eafde7", activebackground="#eafde7",command=splash.destroy).place(x=1320, y=10)
        start_img = PhotoImage(file="start.png")
        
        Button(splash, bd=0, image=start_img, bg="#44484b", activebackground="#44484b",command=loadUI).place(x=970, y=560)

        splash.mainloop()
        return

    def loadUI():
        splash.destroy()
        firstUI()
        return

    def firstUI():
        global fin, board, stream, name, info, first, gender,dob
        global sub1Tv, sub1Prcv, sub1Av, sub1Pv, sub1T
        global listStr,listS1,listS2,listS3
        global dobVal
        first = Toplevel()
        first.title("Home Page")
        first.wm_attributes('-fullscreen', 'true')
        bg = PhotoImage(master=first,file="bg.png")
        Label(first, image=bg).place(relwidth=1, relheight=1)
        close = PhotoImage(master=first, file="close.png")
        Button(first, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=first.destroy).place(x=1320,y=10)
        Label(first,text="Enter Your Details", font=("Courier",30,"bold underline"),bg=lightBG, fg="#27292b").place(x=490,y=130)
        Label(first, text="Name*: ", fg="#27292b",font=("Arial Black",12), bg=lightBG).place(x=520, y=260)
        #gender
        Label(first, text="Gender*: ",fg="#27292b" , font=("Arial Black",12), bg=lightBG). place(x=520, y=290)
        
        Label(first, text="12th Board*: ", fg="#27292b",font=("Arial Black",12), bg=lightBG).place(x=520, y=320)
        
        Label(first, text="DOB*: ",fg="#27292b" ,font=("Arial Black",12), bg=lightBG).place(x=520,y=350)
        
        Label(first, text="Stream*: ",fg="#27292b" ,font=("Arial Black",12), bg=lightBG). place(x=520, y=390)
        name = Entry(first, font=("Arial",12))
        board = IntVar()
        
        Radiobutton(first, text="CBSE",font=("Arial",12), bg=lightBG , variable=board, value=1).place(x=720, y=320)
        Radiobutton(first, text="SSC",font=("Arial",12), bg=lightBG, variable=board, value=2).place(x=820, y=320)
        Radiobutton(first, text="OTHERS",font=("Arial",12), bg=lightBG, variable=board, value=3).place(x=920, y=320)
        
        gender=IntVar()   
        level = IntVar()
        stream= IntVar()
        
        name.place(x=720, y=260)
        def example1():
            def print_sel():
                cal.destroy()
                global dobVal
                dobVal=cal.selection_get()
                print(dobVal)
                fin.config(text="YYYY/MM/DD : "+str(dobVal))
                
            
            mindate = datetime.date(year=1999, month=1, day=20)
            maxdate = datetime.date(year=2003, month=1, day=20)
            cal = Calendar(first, font="Arial 14", selectmode='day', locale='en_US',
            mindate=mindate, maxdate=maxdate, disabledforeground='red')
            
            cal.place(x=720,y=360)
            ttk.Button(first, text="save", command=print_sel).place(x=1100,y=350)

        
        ttk.Button(first, text='-select-', command=example1).place(x=720,y=350)    
        Radiobutton(first, text="Male",font=("Arial",12), bg=lightBG , variable=gender, value=1).place(x=720, y=290)
        Radiobutton(first, text="Female",font=("Arial",12), bg=lightBG , variable=gender, value=2).place(x=820, y=290)
        Radiobutton(first, text="Science",font=("Arial",12), bg=lightBG , variable=stream, value=1).place(x=720, y=390)
        Radiobutton(first, text="Humanities/Arts",font=("Arial",12), bg=lightBG, variable=stream, value=2).place(x=720, y=420)
        Radiobutton(first, text="Commerce",font=("Arial",12), bg=lightBG, variable=stream, value=3).place(x=720, y=450)
     
        start_img = PhotoImage(file="continue.png")
        Button(first, text="Click Here", relief=RIDGE, image=start_img, bg=darkBG, activebackground=darkBG, bd=0, command=startQuiz).place(x=640, y=590)
        info = Label(first, text="", font=("Helvetica",10), bg=lightBG, fg="red")
        info.place(x=620, y=475)
        
        fin=Label(first,text="",font=("Helvetica",12),bg=lightBG,fg="black")
        fin.place(x=800,y=350)
        
        first.mainloop()
        return

    def startQuiz():
        global nameVal, regVal, boardVal, dobVal, genVal, difLevel, streamVal,year,checkVal
        global sub1Tv,nik,sub1Prcv,sub1Av,sub1Pv
        nameVal = str(name.get()).title()
        boardVal= board.get()
        streamVal=stream.get()
        genVal = gender.get()
        
        if len(nameVal) == 0:
            info.config(text="*Please Enter Valid Name")
            return
        elif gender.get() not in range(1,3):
            info.config(text="*Please Select gender to proceed")
            return
        
        elif board.get() not in range(1,4):
            info.config(text="*Please Select valid BOARD to proceed")
            return
        elif stream.get() not in range(1,4):
            info.config(text="*Please Select valid STREAM to proceed")
            return      
        else:
            
            global first
            first.destroy()
            secondIN()
            
        '''elif len(dobVal) !=0:
            info.config(text="*Please Enter Valid Date Of Birth")
            return'''
        
                                    
    def secondIN():
        global listStr,listS1,listS2,listS3,listS4,listS5
        global name, board, reg, section, stream,  level, name, reg, section, level, info, first, gender,dobf,fin,check,nik
        global second, sub1T ,sub1Tv,sub1Prc,sub1A,sub1P
        global sub2T,sub2Prc,sub2P,sub2A
        global sub3T,sub3Prc,sub3P,sub3A
        global sub4T,sub4Prc,sub4P,sub4A
        global sub5T,sub5Prc,sub5P,sub5A
        global sub1Tv, sub1Prcv, sub1Av, sub1Pv, sub1
        global sub2Tv, sub2Prcv, sub2Av, sub2Pv, sub2
        global sub3Tv, sub3Prcv, sub3Av, sub3Pv, sub3 
        global sub4Tv, sub4Prcv, sub4Av, sub4Pv, sub4
        global sub5Tv, sub5Prcv, sub5Av, sub5Pv, sub5
        second = Toplevel()
        second.title(" Quizi")
        second.wm_attributes('-fullscreen', 'true')
        bg = PhotoImage(master=second,file="bg.png")
        Label(second, image=bg).place(relwidth=1, relheight=1)
        close = PhotoImage(master=second, file="close.png")
        Button(second, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=second.destroy).place(x=1320,y=10)

        Label(second,text="Enter Your Academic Details", font=("Courier",30,"bold underline"),bg=lightBG, fg="#27292b").place(x=350,y=25)

        
        
        Label(second, text="Subject", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=480, y=100)   
        Label(second, text="Theory(100)", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=660, y=100)
        Label(second, text="Practical(30)", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=810, y=100)
        Label(second, text="Attend.(100)", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=985,y=100)
        Label(second, text="Project(30)", fg="#27292b",font=("Courier",16,"bold"), bg=lightBG).place(x=1150, y=100)

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


     #sub2
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
        
        sub2Tv=sub2T.get()
        sub2Prcv=sub2Prc.get()
        sub2Av=sub2A.get()
        sub2Pv=sub2P.get()        

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
        
        sub3Tv=sub3T.get()
        sub3Prcv=sub3Prc.get()
        sub3Av=sub3A.get()
        sub3Pv=sub3P.get()        

        #sub3

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
        
        
        Label(second,text="Guidelines :",font=("Arial",12),bg=darkBG,fg="red").place(x=510,y=520)
        Label(second,text="*Language II mentioned above may vary from candidate to candidate", font=("Arial",12),bg=darkBG, fg="red").place(x=520,y=550)
        Label(second,text="*Language II could be HINDI, SANSKRIT, FRENCH, TELUGU ", font=("Arial",12),bg=darkBG, fg="red").place(x=520,y=580)
        Label(second,text="*It is mandatory for the candidate to enter the marks for all the above mentioned subjects ", font=("Arial",12),bg=darkBG, fg="red").place(x=520,y=610)
        
        board= IntVar()
        gender=IntVar()   
        level = IntVar()
        stream= IntVar()
        res = PhotoImage(file="sub_img.png")
        Button(second, text="submit", bd=0,relief=RIDGE, image=res,bg=lightBG,activebackground=lightBG, command=proceed).place(x=700, y=420)
        nik = Label(second, text="", font=("Helvetica",10,"bold"), bg=lightBG, fg="red")
        nik.place(x=680, y=400)
          
        
        second.mainloop()
        return
    def proceed():
        global sub1Tv,nik,sub1Prcv,sub1Av,sub1Pv
        global second,std_id 
        global listStr,listS1,listS2,listS3,listS4,listS5
        
        
        sub1Tv=sub1T.get()
        sub1Prcv=sub1Prc.get()
        sub1Av=sub1A.get()
        sub1Pv=sub1P.get()

        sub2Tv=sub2T.get()
        sub2Prcv=sub2Prc.get()
        sub2Av=sub2A.get()
        sub2Pv=sub2P.get()

        sub3Tv=sub3T.get()
        sub3Prcv=sub3Prc.get()
        sub3Av=sub3A.get()
        sub3Pv=sub3P.get()
        
        sub4Tv=sub4T.get()
        sub4Prcv=sub4Prc.get()
        sub4Av=sub4A.get()
        sub4Pv=sub4P.get()

        sub5Tv=sub5T.get()
        sub5Prcv=sub5Prc.get()
        sub5Av=sub5A.get()
        sub5Pv=sub5P.get()

        #validation for subjects
        
        if (len(sub1Tv)==0 or len(sub1Tv)>=4) or (len(sub2Tv)==0 or len(sub2Tv)>=4) or(len(sub3Tv)==0 or len(sub3Tv)>=4) or (len(sub4Tv)==0 or len(sub4Tv)>=4) or (len(sub5Tv)==0 or len(sub5Tv)>=4) :
            nik.config(text="Please Enter valid Theory marks!")
            return 
        elif (len(sub1Prcv)==0 or len(sub1Prcv)>=3)or(len(sub2Prcv)==0 or len(sub2Prcv)>=3)or(len(sub3Prcv)==0 or len(sub3Prcv)>=3)or(len(sub4Prcv)==0 or len(sub4Prcv)>=3)or(len(sub5Prcv)==0 or len(sub5Prcv)>=3):
            nik.config(text="Please Enter valid  Practical marks!")
            return 
        elif (len(sub1Av)==0 or len(sub1Av)>=4) or(len(sub2Av)==0 or len(sub2Av)>=4)or(len(sub3Av)==0 or len(sub3Av)>=4)or(len(sub4Av)==0 or len(sub4Av)>=4)or(len(sub5Av)==0 or len(sub5Av)>=4):
            nik.config(text="Please Enter valid Attendance!")
            return
        elif (len(sub1Pv)==0 or len(sub1Pv)>=3) or (len(sub2Pv)==0 or len(sub2Pv)>=3) or (len(sub3Pv)==0 or len(sub3Pv)>=3) or (len(sub4Pv)==0 or len(sub4Pv)>=3) or (len(sub5Pv)==0 or len(sub5Pv)>=3):
            nik.config(text="Please Enter valid Project marks!")
            return     
        else:
            nik.config(text="click to continue")
            
        #checking
       
        print("final values")                     
        listS1=[]
        listS1.extend([sub1Tv,sub1Prcv,sub1Av,sub1Pv])
        listS2=[]
        listS2.extend([sub2Tv,sub2Prcv,sub2Av,sub2Pv])
        listS3=[]
        listS3.extend([sub3Tv,sub3Prcv,sub3Av,sub3Pv])
        listS4=[]
        listS4.extend([sub4Tv,sub4Prcv,sub4Av,sub4Pv])
        listS5=[]
        listS5.extend([sub5Tv,sub5Prcv,sub5Av,sub5Pv])
        
        print(listS1)
        print(listS2)
        print(listS3)
        print(listS4)
        print(listS5)

        
        #DATABASECODE::

        global coc, cursor,flag,std_id
        coc = sqlite3.connect("databaseNK.db")
        cursor = coc.cursor()
        
        
        def get_var_value(filename="nikhilK.txt"):
            with open(filename,"a+") as f:
                f.seek(0)
                val=int(f.read() or 0) + 1
                f.seek(0)
                f.truncate()
                f.write(str(val))
                return val
        std_id=get_var_value()
        try:
            cursor.execute("CREATE TABLE guide (std_id INTEGER NOT NULL,theory INTEGER,practical INTEGER,attendance INTEGER,project INTEGER )")
        except:
            cursor.execute("INSERT INTO guide values(?,?,?,?,?) ",(std_id,sub1Tv,sub1Prcv,sub1Av,sub1Pv))
            cursor.execute("INSERT INTO guide values(?,?,?,?,?) ",(std_id,sub2Tv,sub2Prcv,sub2Av,sub2Pv))
            cursor.execute("INSERT INTO guide values(?,?,?,?,?) ",(std_id,sub3Tv,sub3Prcv,sub3Av,sub3Pv))
            cursor.execute("INSERT INTO guide values(?,?,?,?,?) ",(std_id,sub4Tv,sub4Prcv,sub4Av,sub4Pv))
            cursor.execute("INSERT INTO guide values(?,?,?,?,?) ",(std_id,sub5Tv,sub5Prcv,sub5Av,sub5Pv))
            
        coc.commit()
        cursor.close()
        coc.close()
        
        
        second.destroy()
        global lb

        lb = Toplevel()
        lb.wm_attributes("-fullscreen", "true")
        bg = PhotoImage(file="bg.png")
        listStr=[]
        Label(lb, image=bg).place(relwidth=1, relheight=1)
        close = PhotoImage(file="close.png")
        Button(lb, bd=0, image=close, bg="#eafde7", activebackground="#eafde7", command=lb.destroy).place(x=1320,y=10)    
        #Label(lb, text="Here are the details you have provided!",font=("Courier",20,"bold"),bg=lightBG).place(x=580,y=30)
        Button(lb, bd=0, image=close, bg="#eafde7", activebackground="#eafde7", command=lb.destroy).place(x=1320,y=10)
        if boardVal==1:
            boardtext="CBSE"
        elif boardVal==2:
            boardtext="SSC"
        else:
            boardtext="OTHERS"
            
        if genVal==1:
            gentext="Male"

        else:
            gentext="Female"
            
        if streamVal==1:
            streamtext="Science"
            listStr.extend(["maths","physics","chemistry"])
        elif streamVal==2:
            streamtext="Commerce"
            listStr.extend(["history","geography","political.sci"])

        else:
            streamtext="Humanities/Arts"
            listStr.extend(["accountancy","economics","business.std"])

            
            
        print(listStr)
        
        Label(lb, text="Hello", font=("Courier",20,"bold"),bg=lightBG, fg="#27292b").place(x=500,y=25)
        Label(lb, text=" "+nameVal+"!", font=("Courier",20,"bold"),bg=lightBG).place(x=585,y=25) 
        Label(lb, text="Here are the details you have provided!",font=("Courier",15,"bold"),bg=lightBG).place(x=430,y=80)

        Label(lb, text="Gender: "+ gentext, font=("Courier", 15,"bold"),bg=lightBG).place(x=300,y=140)          
        Label(lb, text="12th Board: "+ boardtext, font=("Courier",15,"bold"),bg=lightBG).place(x=300,y=180)

        Label(lb, text="DOB: "+str(dobVal), font=("Courier", 15,"bold"),bg=lightBG).place(x=300,y=220)
        edit = PhotoImage(file="edit.png")
        Button(lb, bd=0,image=edit,bg=darkBG,activebackground=darkBG,command=goBack).place(x=550,y=550)

       
        Label(lb, text="Stream: "+streamtext, font=("Courier",15,"bold"),bg=lightBG).place(x=300,y=260)
        test = PhotoImage(file="test.png")
        Button(lb, bd=0, image=test, bg=darkBG, activebackground=darkBG,command=take_test ).place(x=850,y=550)


        coc = sqlite3.connect("databaseNK.db")
        cursor = coc.cursor()
        
        cursor.execute("Select * from guide order by std_id desc LIMIT 5")

        Label(lb, text="Sub.",font=("Courier",15,"bold"),bg=lightBG).place(x=780,y=150)
        Label(lb, text="S_ID",font=("Courier",15,"bold"),bg=lightBG).place(x=850,y=150)
        Label(lb, text="Th.",font=("Courier",15,"bold"),bg=lightBG).place(x=915,y=150)
        Label(lb, text="Prc.",font=("Courier",15,"bold"),bg=lightBG).place(x=955,y=150)   
        Label(lb, text="Attd.",font=("Courier",15,"bold"),bg=lightBG).place(x=1015,y=150)
        Label(lb, text="Pro.",font=("Courier",15,"bold"),bg=lightBG).place(x=1060,y=150)
     
        finalData=cursor.fetchall()
        F1=Frame(lb,bg=lightBG)
        F1.place(x=750,y=180)
        for z in range(len(finalData)):
            Label(F1, text="subject "+str(z+1),font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=0,padx=10,pady=10)
            Label(F1, text=finalData[z][0],font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=1,padx=10,pady=10)
            Label(F1, text=finalData[z][1],font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=2,padx=10,pady=10)
            Label(F1, text=finalData[z][2],font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=3,padx=10,pady=10)
            Label(F1, text=finalData[z][3],font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=4,padx=10,pady=10)
            Label(F1, text=finalData[z][4],font=("Comic Sans MS",14), bg=lightBG, fg="#27292b").grid(row=z,column=5,padx=10,pady=10)
                                        
        lb.mainloop()
        return
    def goBack():
        lb.destroy()
        firstUI()
    Splash()
    print("came back to main")
 
       
def take_test():
    Recommendation_system()
def fuzzy_calculator(inputs):
    
    
    theory= ctrl.Antecedent(np.arange(0,101,1),'theory')
    practical=ctrl.Antecedent(np.arange(0,31,1,),'practical')
    attendance= ctrl.Antecedent(np.arange(0,101,1),'attendance')
    project= ctrl.Antecedent(np.arange(0,31,1),'project')
    grade=ctrl.Consequent(np.arange(0,101,1),'grade')



    practical['l']=fuzz.trimf(practical.universe,[0,10,15])
    practical['m']=fuzz.trimf(practical.universe,[12,15,24])
    practical['h']=fuzz.trimf(practical.universe,[22,26,30])

    theory['l']=fuzz.trimf(theory.universe,[0,40,50])
    theory['m']=fuzz.trimf(theory.universe,[45,65,80])
    theory['h']=fuzz.trimf(theory.universe,[75,85,100])

    attendance['l']=fuzz.trimf(attendance.universe,[0,40,50])
    attendance['m']=fuzz.trimf(attendance.universe,[45,65,80])
    attendance['h']=fuzz.trimf(attendance.universe,[75,85,100])

    project['l']=fuzz.trimf(project.universe,[0,10,15])
    project['m']=fuzz.trimf(project.universe,[13,15,24])
    project['h']=fuzz.trimf(project.universe,[22,26,30])

    grade['l']=fuzz.trimf(grade.universe,[0,40,50])
    grade['m']=fuzz.trimf(grade.universe,[45,65,80])
    grade['h']=fuzz.trimf(grade.universe,[75,85,100])

    practical.view()
    theory.view()
    project.view()


    rule1 = ctrl.Rule( theory['l'] & practical['l'] & attendance['l'] & project['l'] , grade['l'])
    rule2 = ctrl.Rule( theory['l'] & practical['l'] & attendance['l'] & project['m'] , grade['l'])
    rule3 = ctrl.Rule( theory['l'] & practical['l'] & attendance['l'] & project['h'] , grade['l'])
    rule4 = ctrl.Rule( theory['l'] & practical['l'] & attendance['m'] & project['l'] , grade['l'])
    rule5 = ctrl.Rule( theory['l'] & practical['l'] & attendance['m'] & project['m'] , grade['l'])
    rule6 = ctrl.Rule( theory['l'] & practical['l'] & attendance['m'] & project['h'] , grade['m'])
    rule7 = ctrl.Rule( theory['l'] & practical['l'] & attendance['h'] & project['l'] , grade['l'])
    rule8 = ctrl.Rule( theory['l'] & practical['l'] & attendance['h'] & project['m'] , grade['m'])
    rule9 = ctrl.Rule( theory['l'] & practical['l'] & attendance['h'] & project['h'] , grade['m'])
    rule10= ctrl.Rule( theory['l'] & practical['m'] & attendance['l'] & project['l'] , grade['l'])
    rule11= ctrl.Rule( theory['l'] & practical['m'] & attendance['l'] & project['m'] , grade['l'])
    rule12= ctrl.Rule( theory['l'] & practical['m'] & attendance['l'] & project['h'] , grade['l'])
    rule13= ctrl.Rule( theory['l'] & practical['m'] & attendance['m'] & project['l'] , grade['l'])
    rule14= ctrl.Rule( theory['l'] & practical['m'] & attendance['m'] & project['m'] , grade['l'])
    rule15= ctrl.Rule( theory['l'] & practical['m'] & attendance['m'] & project['h'] , grade['l'])
    rule16= ctrl.Rule( theory['l'] & practical['m'] & attendance['h'] & project['l'] , grade['l'])
    rule17= ctrl.Rule( theory['l'] & practical['m'] & attendance['h'] & project['m'] , grade['m'])
    rule18= ctrl.Rule( theory['l'] & practical['m'] & attendance['h'] & project['h'] , grade['m'])
    rule19= ctrl.Rule( theory['l'] & practical['h'] & attendance['l'] & project['l'] , grade['l'])
    rule20= ctrl.Rule( theory['l'] & practical['h'] & attendance['l'] & project['m'] , grade['l'])
    rule21= ctrl.Rule( theory['l'] & practical['h'] & attendance['l'] & project['h'] , grade['l'])
    rule22= ctrl.Rule( theory['l'] & practical['h'] & attendance['m'] & project['l'] , grade['l'])
    rule23= ctrl.Rule( theory['l'] & practical['h'] & attendance['m'] & project['m'] , grade['l'])
    rule24= ctrl.Rule( theory['l'] & practical['h'] & attendance['m'] & project['h'] , grade['m'])
    rule25= ctrl.Rule( theory['l'] & practical['h'] & attendance['h'] & project['l'] , grade['l'])
    rule26= ctrl.Rule( theory['l'] & practical['h'] & attendance['h'] & project['m'] , grade['m'])
    rule27= ctrl.Rule( theory['l'] & practical['h'] & attendance['h'] & project['h'] , grade['m'])

    rule28= ctrl.Rule( theory['m'] & practical['l'] & attendance['l'] & project['l'] , grade['l'])
    rule29= ctrl.Rule( theory['m'] & practical['l'] & attendance['l'] & project['m'] , grade['l'])
    rule30= ctrl.Rule( theory['m'] & practical['l'] & attendance['l'] & project['h'] , grade['m'])
    rule31= ctrl.Rule( theory['m'] & practical['l'] & attendance['m'] & project['l'] , grade['l'])
    rule32= ctrl.Rule( theory['m'] & practical['l'] & attendance['m'] & project['m'] , grade['m'])
    rule33= ctrl.Rule( theory['m'] & practical['l'] & attendance['m'] & project['h'] , grade['m'])
    rule34= ctrl.Rule( theory['m'] & practical['l'] & attendance['h'] & project['l'] , grade['l'])
    rule35= ctrl.Rule( theory['m'] & practical['l'] & attendance['h'] & project['m'] , grade['l'])
    rule36= ctrl.Rule( theory['m'] & practical['l'] & attendance['h'] & project['h'] , grade['m'])
    rule37= ctrl.Rule( theory['m'] & practical['m'] & attendance['l'] & project['l'] , grade['l'])
    rule38= ctrl.Rule( theory['m'] & practical['m'] & attendance['l'] & project['m'] , grade['l'])
    rule39= ctrl.Rule( theory['m'] & practical['m'] & attendance['l'] & project['h'] , grade['m'])
    rule40= ctrl.Rule( theory['m'] & practical['m'] & attendance['m'] & project['l'] , grade['m'])
    rule41= ctrl.Rule( theory['m'] & practical['m'] & attendance['m'] & project['m'] , grade['m'])
    rule42= ctrl.Rule( theory['m'] & practical['m'] & attendance['m'] & project['h'] , grade['m'])
    rule43= ctrl.Rule( theory['m'] & practical['m'] & attendance['h'] & project['l'] , grade['m'])
    rule44= ctrl.Rule( theory['m'] & practical['m'] & attendance['h'] & project['m'] , grade['m'])
    rule45= ctrl.Rule( theory['m'] & practical['m'] & attendance['h'] & project['h'] , grade['h'])
    rule46= ctrl.Rule( theory['m'] & practical['h'] & attendance['l'] & project['l'] , grade['l'])
    rule47= ctrl.Rule( theory['m'] & practical['h'] & attendance['l'] & project['m'] , grade['m'])
    rule48= ctrl.Rule( theory['m'] & practical['h'] & attendance['l'] & project['h'] , grade['m'])
    rule49= ctrl.Rule( theory['m'] & practical['h'] & attendance['m'] & project['l'] , grade['m'])
    rule50= ctrl.Rule( theory['m'] & practical['h'] & attendance['m'] & project['m'] , grade['m'])
    rule51= ctrl.Rule( theory['m'] & practical['h'] & attendance['m'] & project['h'] , grade['m'])
    rule52= ctrl.Rule( theory['m'] & practical['h'] & attendance['h'] & project['l'] , grade['m'])
    rule53= ctrl.Rule( theory['m'] & practical['h'] & attendance['h'] & project['m'] , grade['h'])
    rule54= ctrl.Rule( theory['m'] & practical['h'] & attendance['h'] & project['h'] , grade['h'])

    rule55= ctrl.Rule( theory['h'] & practical['l'] & attendance['l'] & project['l'] , grade['m'])
    rule56= ctrl.Rule( theory['h'] & practical['l'] & attendance['l'] & project['m'] , grade['m'])
    rule57= ctrl.Rule( theory['h'] & practical['l'] & attendance['l'] & project['h'] , grade['m'])
    rule58= ctrl.Rule( theory['h'] & practical['l'] & attendance['m'] & project['l'] , grade['m'])
    rule59= ctrl.Rule( theory['h'] & practical['l'] & attendance['m'] & project['m'] , grade['m'])
    rule60= ctrl.Rule( theory['h'] & practical['l'] & attendance['m'] & project['h'] , grade['m'])
    rule61= ctrl.Rule( theory['h'] & practical['l'] & attendance['h'] & project['l'] , grade['m'])
    rule62= ctrl.Rule( theory['h'] & practical['l'] & attendance['h'] & project['m'] , grade['m'])
    rule63= ctrl.Rule( theory['h'] & practical['l'] & attendance['h'] & project['h'] , grade['m'])
    rule64= ctrl.Rule( theory['h'] & practical['m'] & attendance['l'] & project['l'] , grade['m'])
    rule65= ctrl.Rule( theory['h'] & practical['m'] & attendance['l'] & project['m'] , grade['m'])
    rule66= ctrl.Rule( theory['h'] & practical['m'] & attendance['l'] & project['h'] , grade['m'])
    rule67= ctrl.Rule( theory['h'] & practical['m'] & attendance['m'] & project['l'] , grade['m'])
    rule68= ctrl.Rule( theory['h'] & practical['m'] & attendance['m'] & project['m'] , grade['m'])
    rule69= ctrl.Rule( theory['h'] & practical['m'] & attendance['m'] & project['h'] , grade['h'])
    rule70= ctrl.Rule( theory['h'] & practical['m'] & attendance['h'] & project['l'] , grade['h'])
    rule71= ctrl.Rule( theory['h'] & practical['m'] & attendance['h'] & project['m'] , grade['h'])
    rule72= ctrl.Rule( theory['h'] & practical['m'] & attendance['h'] & project['h'] , grade['h'])
    rule73= ctrl.Rule( theory['h'] & practical['h'] & attendance['l'] & project['l'] , grade['m'])
    rule74= ctrl.Rule( theory['h'] & practical['h'] & attendance['l'] & project['m'] , grade['h'])
    rule75= ctrl.Rule( theory['h'] & practical['h'] & attendance['l'] & project['h'] , grade['h'])
    rule76= ctrl.Rule( theory['h'] & practical['h'] & attendance['m'] & project['l'] , grade['h'])
    rule77= ctrl.Rule( theory['h'] & practical['h'] & attendance['m'] & project['m'] , grade['h'])
    rule78= ctrl.Rule( theory['h'] & practical['h'] & attendance['m'] & project['h'] , grade['h'])
    rule79= ctrl.Rule( theory['h'] & practical['h'] & attendance['h'] & project['l'] , grade['h'])
    rule80= ctrl.Rule( theory['h'] & practical['h'] & attendance['h'] & project['m'] , grade['h'])
    rule81= ctrl.Rule( theory['h'] & practical['h'] & attendance['h'] & project['h'] , grade['h'])



    wm_ctrl= ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36,rule37
                                ,rule38,rule39,rule40,rule41,rule42,rule43,rule44,rule45,rule46,rule47,rule48,rule49,rule50,rule51,rule52,rule53,rule54,rule55,rule56,rule57,rule58,rule59,rule60,rule61,rule62,rule63,rule64,rule65,rule66,rule67,rule68,rule69,rule70,rule71,rule72,rule73,rule74
                                ,rule75,rule76,rule77,rule78,rule79,rule80,rule81])
    wm= ctrl.ControlSystemSimulation(wm_ctrl)

    wm.input['theory']=inputs[0]
    wm.input['practical']=inputs[1]
    wm.input['attendance']=inputs[2]
    wm.input['project']=inputs[3]

    wm.compute()
    out=wm.output['grade']
    print(out)
    grade.view(sim=wm)
    return out

def Recommendation_system():
    
    subjects_science=['physics','chemistry','biology','mathematics','English']
    subjects_commerce=['Bussiness','Accounts','Economics','Mathematics','English']
    subjects_Humanities=['History','Geography','Political Science','Physical Education','English']
    test_scores=[9,9,9,9,9]
    lists1=[int(i) for i in listS1]
    lists2=[int(i) for i in listS2]
    lists3=[int(i) for i in listS3]
    lists4=[int(i) for i in listS4]
    lists5=[int(i) for i in listS5]
    final_marks=[lists1[0]+lists1[1],lists2[0]+lists2[1],lists3[0]+lists3[1],lists4[0]+lists4[1],lists5[0]+lists5[1]]
    
    sub1=fuzzy_calculator(lists1)
    sub2=fuzzy_calculator(lists2)
    sub3=fuzzy_calculator(lists3)
    sub4=fuzzy_calculator(lists4)
    sub5=fuzzy_calculator(lists5)
    lb.destroy()
    recommendation=dict()
    eligibility=sum(final_marks)/5
    
    if(streamVal==1):
        #test for Engineering

        if(eligibility>60 and final_marks[0]>60 and final_marks[1]>60 and final_marks[3]>60):
            fuzz_score=(sub1+sub2+sub3)/3
            recommendation['Engineering']=fuzz_score
        #test for Medical
        if(eligibility>60 and final_marks[2]>60):
            fuzz_score=(sub2+sub3)/2
            recommendation['Medical']=fuzz_score
        #test for Bsc
        if(eligibility>60 and final_marks[0]>60):
            recommendation['Bsc physics']=sub1
        if(eligibility>60 and final_marks[1]>60):
            recommendation['Bsc chemistry']=sub2
        if(eligibility>60 and final_marks[2]>60):
            recommendation['Bsc biology']=sub3
        if(eligibility>60 and final_marks[3]>60):
            recommendation['Bsc mathematics']=sub4
        if(eligibility>60 and final_marks[4]>60):
            recommendation['Bsc Computer Science']=sub4
    elif (streamVal==2):
         #test for BA

        if(eligibility>60 ):
            fuzz_score=(sub1+sub2+sub3+sub4)/4
            recommendation['BA']=fuzz_score
        #test for Journalism and Mass Communication
        if(eligibility>60 and final_marks[2]>60 ):
            recommendation['Journalism and Mass Communication']=sub3
        if(eligibility>60 ):
            recommendation['Fashion Design']=sub5

       
    else:
         #test for Bcom

        if(eligibility>60 ):
            fuzz_score=(sub1+sub2+sub3+sub4)/4
            recommendation['Bcom']=fuzz_score
        #test for BBA
        if(eligibility>60 and final_marks[0]>60):
            fuzz_score=(sub1+sub2)/2
            recommendation['BBA']=fuzz_score
        #test for Bachelor of Economics
        if(eligibility>60 and final_marks[2]>60):
            recommendation['Bachelor of Economics']=sub3
        #test for LLB
        if(eligibility>60 and final_marks[4]>60):
            fuzz_score=(sub3+sub5)/2
            recommendation['LLB']=fuzz_score
        #test for CA
        if(eligibility>60 and final_marks[1]>60):
            fuzz_score=(sub2+sub3)/2
            recommendation['CA']=fuzz_score
       

    if(eligibility>50 and (sum(test_scores)/5) > 5):
        fuzz_score=sub5
        recommendation['Animation and Graphics Design']=sub5


    if(eligibility>60 and (sum(test_scores)/5) > 5 and final_marks[0]>60 and final_marks[1]>60 and final_marks[3]>60 and final_marks[4]>60):
        fuzz_score=(sub1+sub2+sub3+sub4+sub5)/4
        recommendation['B.Ed']=sub5
       
    for i in recommendation:
       print(i,": ",recommendation[i])
    
    path_selection()
def path_selection():
    print(listS1)
    print(listS2)
    print(listS3)
    print(listS4)
    print(listS5)
    global top,window
    
    if window==1:
        top.withdraw()
    top=Toplevel()
    top.geometry("1400x700+0+0")
    top.title("Pathway Selection")
    image1 =PhotoImage(file="path.png")
    top.wm_attributes('-fullscreen', 'true')
    Form = Label(top, image=image1)
    Form.pack(side='top', fill='both', expand='yes')
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
    OptionList=["Animation/Graphics","BA","Bachelor of Education","Bachelor of Economics","BBA","B.Com","BSc Physics","BSc chemistry","BSc biology","BSc mathematics"
                              ,"BSc Computer","CA","Journalism and Communication",
                              "Engineering ",
                              "LLB",
                              "Medical"]
    variable = StringVar(top)
    variable.set(OptionList[0])

    opt = OptionMenu(top, variable, *OptionList)
    opt.config(width=20, font=('Helvetica', 12))
    opt.place(x=950,y=320)


    labelTest = Label(text="", font=('Helvetica', 12), fg='white')
    labelTest.place(x=920,y=320)

    def callback(*args):
        labelTest.configure(text="The selected item is {}".format(variable.get()))

    variable.trace("w", callback)

    
   
    btn_go = Button(Form, text="GO", width=25, command=show_colleges)
    btn_go.place(x=950, y=400)
    btn_go.bind('<Return>',show_colleges )
    top.mainloop()   
      
def show_colleges():
    global top,window
    
    if window==1:
        top.withdraw()
    top=Toplevel()
    top.geometry("1400x700+0+0")
    top.title("Colleges")
   
    top.mainloop()

root=Tk()
root.withdraw()
global window
window=0
Home()
   

