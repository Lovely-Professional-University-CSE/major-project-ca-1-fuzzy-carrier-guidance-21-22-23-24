from tkinter import *
from tkinter import messagebox

def message():
    messagebox.showinfo("Thankyou","Thankyou for your valuable feedback")
    
def function():
    top.destroy()
    developers_image()

def function2():
    top.destroy()
    feedback()

def function3():
    image1.destroy()
    back()

def function4():
    feed.destroy()
    back()

def back():
    global top
    top=Tk()
    top.wm_attributes("-fullscreen","true")
    back=PhotoImage(file="thankyou.png")
    bk=Label(top,image=back)
    bk.place(x=0,y=0,relwidth=1,relheight=1)

    exit = Button(top, justify=LEFT,bg="#005367",activebackground="#005367")
    ex = PhotoImage(file="icon.png")
    exit.config(image=ex, width="30", height="30", bd=0, command=top.destroy)
    exit.place(x=1300,y=30)

    back1=Button(top,justify=LEFT)
    developer=PhotoImage(file="develop.png")
    back1.config(image=developer,width="150",height="150",command=function)
    back1.place(x=30,y=463)

    back2=Button(top,justify=LEFT)
    feedback=PhotoImage(file="feedback.png")
    back2.config(image=feedback,width="150",height="150",command=function2)
    back2.place(x=1100,y=463)
    top.mainloop()


def feedback():
    global feed
    feed=Tk()
    feed.wm_attributes("-fullscreen","true")
   # Label(text="",justify=CENTER,relief="flat",width=400,height=100,bg="orange").place(x=0,y=0)

    back23=PhotoImage(file="feedbackbackgroundfinal.png")
    bk23=Label(feed,image=back23)
    bk23.place(x=350,y=100,relwidth=1,relheight=1)

    b121=Button(feed,justify = LEFT)
    photo12=PhotoImage(file="backbutton.png")
    b121.config(image=photo12,width="200",height="55",activebackground="#f15922",bg="#005367",bd=0,command=function4)
    b121.place(x=300,y=570)


    b33=Button(feed,justify = LEFT)
    photo2=PhotoImage(file="sub2.png")
    b33.config(image=photo2,width="200",height="40",bd=0,activebackground="#f15922",command=message)
    b33.place(x=510,y=330)
    
    exit1 = Button(feed, justify=LEFT,bg="#005367",activebackground="#005367")
    ex1 = PhotoImage(file="icon.png")
    exit1.config(image=ex1, width="30", height="30", bd=0, command=feed.destroy)
    exit1.place(x=1300,y=30)
    
    Label(feed,text="ENTER YOUR RESPONCE",font=("Times New Roman",25)).place(x=250,y=250)
    e1=Entry(feed,bd=5,width=50).place(x=660,y=260)
    feed.mainloop()



    
def developers_image():
    global image1
    image1=Tk()
    image1.wm_attributes("-fullscreen","true")
    '''
    back1=PhotoImage(file="backgroundplain.png")
    bk2=Label(image1,image=back1)
    bk2.place(x=0,y=0,relwidth=1,relheight=1)
    '''
    Label(text="",justify=CENTER,relief="flat",width=400,height=100,bg="skyblue").place(x=0,y=0)
    b1=Button(image1,justify = LEFT)
    photo1=PhotoImage(file="backbutton.png")
    b1.config(image=photo1,width="200",height="55",activebackground="#f15922",bg="#005367",bd=0,command=function3)
    b1.place(x=900,y=600)

    exit = Button(image1, justify=LEFT,bg="#005367",activebackground="#005367")
    ex = PhotoImage(file="icon.png")
    exit.config(image=ex, width="30", height="30", bd=0, command=image1.destroy)
    exit.place(x=1300,y=30)

    MOHIT='''    Name:MOHIT SRIKHAKOLLU
             Email-id:srikakollamohith9@gmail.com
             Reg no: 11707426
             Phone No:9182902965 '''
    CHAITANYA='''   Name: Chaitanya Kishore Singaraju
                 Email-id:chaitanya9780@gmail.com
                 Reg no:  11706282
                 Phone No:9603112410'''
    Nikhil='''    Name:Nikhil Raju Kataru
              Email-id:nikhilkataru07@gmail.com
              Reg no:  11707830
              Phone No:7893945033'''
    Sandeep='''    Name:Sandeep Kumar
               Email-id:sandeep123@gmail.com
               Reg no  : 11754565
               Phone No:8621910294'''

    
    
    image_mohit=PhotoImage(file='mohith_image.png')
    ck=Label(image1,image=image_mohit)
    ck.place(x=0,y=200)
    Label(image1,justify=CENTER,text=MOHIT,relief="flat",width=34,height=10,font=("Times New Roman",15),bg="skyblue").place(x=130,y=150)

    
    image_chaitanya=PhotoImage(file='chaitanya1.png')
    ck1=Label(image1,image=image_chaitanya)
    ck1.place(x=0,y=0)
    Label(image1,justify=CENTER,text=CHAITANYA,relief="flat",width=34,height=10,font=("Times New Roman",15),bg="skyblue").place(x=130,y=-20)
    
    image_nikhil=PhotoImage(file='nikhil_image.png')
    ck2=Label(image1,image=image_nikhil)
    ck2.place(x=0,y=580)
    Label(image1,justify=CENTER,text=Nikhil,relief="flat",width=34,height=10,font=("Times New Roman",15),bg="skyblue").place(x=130,y=505)
    
    image_sandeep=PhotoImage(file='sandeep_image.png')
    ck3=Label(image1,image=image_sandeep)
    ck3.place(x=0,y=380)
    Label(image1,justify=CENTER,text=Sandeep,relief="flat",width=34,height=10,font=("Times New Roman",15),bg="skyblue").place(x=130,y=325)
    
    image1.mainloop()


back()

