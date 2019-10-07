from tkinter import *
import sqlite3

def HomeWindow():
    global Home
    
    Fill_details()
def Signup_window():
    global top,window
    
    if window==1:
        top.withdraw()
    window=1
    
    global flag,USERNAME,PASSWORD,lbl_text,contactno,firstname,middlename,lastname
    
    top=Toplevel()

    top.geometry("1400x700+0+0")
    top.title("SIGNUP")
    
    image1 =PhotoImage(file='C:\\Users\\srika\\Pictures\\Screenshots\\Screenshot (105).png')
    
    Form1 = Label(top, image=image1)
    Form1.pack(side='top', fill='both', expand='yes')
    
    USERNAME = StringVar()
    PASSWORD = StringVar()
    contactno=StringVar()
    firstname=StringVar()
    middlename=StringVar()
    lastname=StringVar()
    lb1=Label(text="Registraton")
    lb1.pack()
    lb1_firstname=Label(Form1, text="First Name:", font=(14), bd=10)
    lb1_firstname.place(x=450,y=80)
    lb1_middlename=Label(Form1, text="Middle Name:", font=(14), bd=10)
    lb1_middlename.place(x=450,y=180)
    lb1_lastname=Label(Form1, text="Last Name:", font=(14), bd=10)
    lb1_lastname.place(x=450,y=280)
    lbl_username = Label(Form1, text = "Email ID:", font=(14), bd=10)
    lbl_username.place(x=450,y=380)
    lbl_password = Label(Form1, text = "Password:", font=(14), bd=10)
    lbl_password.place(x=450,y=480 )
    lb1_contactno=Label(Form1, text="Contactno:", font=(14), bd=10)
    lb1_contactno.place(x=450,y=580)
    
    lbl_text = Label(Form1)
    lbl_text.grid(row=3, columnspan=2)

    
    firstname = Entry(Form1, textvariable=firstname, font=(14))
    firstname.place(x=570, y=80)
    middlename = Entry(Form1, textvariable=middlename, font=(14))
    middlename.place(x=570, y=180)
    lastname = Entry(Form1, textvariable=lastname, font=(14))
    lastname.place(x=570, y=280)
    username = Entry(Form1, textvariable=USERNAME, font=(14))
    username.place(x=570, y=380)
    password = Entry(Form1, textvariable=PASSWORD, show="*", font=(14))
    password.place(x=570, y=480)
    contactno=Entry(Form1, textvariable=contactno,font=(14))
    contactno.place(x=570, y=580)
    bt_signup = Button(Form1, text="Register", width=25, command=Signup_window)
    bt_signup.place(x=650, y=620)
    bt_signup.bind('<Return>', Signup_window)
    
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
    global conn, cursor,flag,USERNAME,PASSWORD,contactno,firstname,middlename,lastname
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("CREATE TABLE member (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT,contactno TEXT,firstname TEXT,middlename TEXT,lastname TEXT)")
        
    except:
        cursor.execute("INSERT INTO member (username, password,contactno,firstname,middlename,lastname) VALUES(?,?)",(USERNAME.get(), PASSWORD.get(),contactno.get(),firstname.get(),
                                                                                                                      middlename.get(),lastname.get()))
        
    conn.commit()
    cursor.close()
    conn.close()

    
def Fill_details():
    print("end")
def login_window():
    global top,window
    if window==1:
        top.withdraw()
    window=1
    global flag,USERNAME,PASSWORD,lbl_text
    top=Toplevel()
    top.geometry("1200x700+0+0")
    top.title("Login")
    form1=Label(top,text="Career Guidance Project",fg="dark green",font="Helvetica 36 bold italic")
    form1.pack()
    image1 =PhotoImage(file='C:\\Users\\srika\\Pictures\\Screenshots\\Screenshot (105).png')
    
    Form = Label(top, image=image1)
    Form.pack(side='top', fill='both', expand='yes')
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
    btn_signup.place(x=950, y=20)
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
    



root=Tk()
root.withdraw()
global window
window=0
login_window()
