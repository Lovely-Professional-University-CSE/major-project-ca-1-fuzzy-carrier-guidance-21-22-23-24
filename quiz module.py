from tkinter import *
from tkinter import messagebox

def function1():
    first.destroy()
    sai()

def function2():
    second.destroy()
    sai()

def function3():
    third.destroy()
    sai()
    
def chai1():
    master.destroy()
    satya1()
def chai2():
    master.destroy()
    satya2()
def chai3():
    master.destroy()
    satya1()

def window():
    chai=Tk()
    count=0
    temp=0
    chai.title('Result')
    chai.geometry('3000x3000')
    f1=Frame(chai)
    '''
    result=PhotoImage(file='result.png')
    ck=Label(chai,image=result)
    ck.place(x=0,y=0,rewidth=1,relheight=1)
    ck.pack()
    '''
    f1.place()
    A=v6.get()
    B=v5.get()
    C=v4.get()
    D=v3.get()
    E=v2.get()
    F=v1.get()
    if(A==2):
        count=count+1
    if(B==4):
        count=count+1
    if(C==1):
        count=count+1
    if(D==2):
        count=count+1
    if(E==4):
        count=count+1
    if(F==2):
        count=count+1
        
    l1=Label(chai,text=count,borderwidth=10)
    l1.place(x=600,y=50)
    l1.configure(font=("Times New Roman",300,"bold"))
    l1=Label(chai,text="MARKS",borderwidth=10)
    l1.place(x=630,y=450)
    l1.configure(font=("Times New Roman",30,"bold"))
    if A==0:
        temp=temp+1
    if B==0:
        temp=temp+1
    if C==0:
        temp=temp+1
    if D==0:
        temp=temp+1
    if E==0:
        temp=temp+1
    if F==0:
        temp=temp+1
    Attempt=6-temp
    l1=Label(chai,text=temp,borderwidth=10)
    l1.place(x=550,y=600)
    l1.configure(font=("Times New Roman",20,"bold"))
    l2=Label(chai,text=Attempt,borderwidth=10)
    l2.place(x=1100,y=600)
    l2.configure(font=("Times New Roman",20,"bold"))
    l3=Label(chai,text="UNATTEMPTED",borderwidth=10)
    l3.place(x=300,y=600)
    l3.configure(font=("Times New Roman",20,"bold"))
    l4=Label(chai,text="ATTEMPTED",borderwidth=10)
    l4.place(x=900,y=600)
    l4.configure(font=("Times New Roman",20,"bold"))



def Window1():
    chai=Tk()
    count=0
    temp=0
    chai.title('Result')
    chai.geometry('3000x3000')
    f1=Frame(chai)
    '''
    result=PhotoImage(file='result.png')
    ck=Label(chai,image=result)
    ck.place(x=0,y=0,rewidth=1,relheight=1)
    ck.pack()
    '''
    f1.place()
    A=v6.get()
    B=v5.get()
    C=v4.get()
    D=v3.get()
    E=v2.get()
    F=v1.get()
    if(A==1):
        count=count+1
    if(B==3):
        count=count+1
    if(C==2):
        count=count+1
    if(D==3):
        count=count+1
    if(E==4):
        count=count+1
    if(F==1):
        count=count+1
        
    l1=Label(chai,text=count,borderwidth=10)
    l1.place(x=600,y=50)
    l1.configure(font=("Times New Roman",300,"bold"))
    l1=Label(chai,text="MARKS",borderwidth=10)
    l1.place(x=630,y=450)
    l1.configure(font=("Times New Roman",30,"bold"))
    if A==0:
        temp=temp+1
    if B==0:
        temp=temp+1
    if C==0:
        temp=temp+1
    if D==0:
        temp=temp+1
    if E==0:
        temp=temp+1
    if F==0:
        temp=temp+1
    Attempt=6-temp
    l1=Label(chai,text=temp,borderwidth=10)
    l1.place(x=550,y=600)
    l1.configure(font=("Times New Roman",20,"bold"))
    l2=Label(chai,text=Attempt,borderwidth=10)
    l2.place(x=1100,y=600)
    l2.configure(font=("Times New Roman",20,"bold"))
    l3=Label(chai,text="UNATTEMPTED",borderwidth=10)
    l3.place(x=300,y=600)
    l3.configure(font=("Times New Roman",20,"bold"))
    l4=Label(chai,text="ATTEMPTED",borderwidth=10)
    l4.place(x=900,y=600)
    l4.configure(font=("Times New Roman",20,"bold"))


def Window2():
    chai=Tk()
    count=0
    temp=0
    chai.title('Result')
    chai.geometry('3000x3000')
    f1=Frame(chai)
    '''
    result=PhotoImage(file='result.png')
    ck=Label(chai,image=result)
    ck.place(x=0,y=0,rewidth=1,relheight=1)
    ck.pack()
    '''
    f1.place()
    A=v6.get()
    B=v5.get()
    C=v4.get()
    D=v3.get()
    E=v2.get()
    F=v1.get()
    if(A==2):
        count=count+1
    if(B==4):
        count=count+1
    if(C==1):
        count=count+1
    if(D==2):
        count=count+1
    if(E==4):
        count=count+1
    if(F==2):
        count=count+1
        
    l1=Label(chai,text=count,borderwidth=10)
    l1.place(x=600,y=50)
    l1.configure(font=("Times New Roman",300,"bold"))
    l1=Label(chai,text="MARKS",borderwidth=10)
    l1.place(x=630,y=450)
    l1.configure(font=("Times New Roman",30,"bold"))
    if A==0:
        temp=temp+1
    if B==0:
        temp=temp+1
    if C==0:
        temp=temp+1
    if D==0:
        temp=temp+1
    if E==0:
        temp=temp+1
    if F==0:
        temp=temp+1
    Attempt=6-temp
    l1=Label(chai,text=temp,borderwidth=10)
    l1.place(x=550,y=600)
    l1.configure(font=("Times New Roman",20,"bold"))
    l2=Label(chai,text=Attempt,borderwidth=10)
    l2.place(x=1100,y=600)
    l2.configure(font=("Times New Roman",20,"bold"))
    l3=Label(chai,text="UNATTEMPTED",borderwidth=10)
    l3.place(x=300,y=600)
    l3.configure(font=("Times New Roman",20,"bold"))
    l4=Label(chai,text="ATTEMPTED",borderwidth=10)
    l4.place(x=900,y=600)
    l4.configure(font=("Times New Roman",20,"bold"))


        

def satya1():
    global v6,v5,v4,v3,v2,v1,first
    first=Tk()
    first.wm_attributes('-fullscreen','true')
    first.title('MATHS QUIZ')
    back=PhotoImage(file="back6.png")
    bk=Label(first,image=back)
    bk.place(x=0,y=0,relwidth=1,relheight=1)


    v6=IntVar()
    q6=Label(first,text='1.While catching a ball, a player pulls down his hands to lower the' ,bg="#f15922")
    q6.place(x=10,y=0)
    q6.configure(font=("Times New Roman",15,"bold"))
    r21=Radiobutton(first,text='a) force',variable=v6,value=1,bg="#f15922")
    r21.place(x=10,y=30)
    r21.configure(font=("Times New Roman",15,"bold"))
    r22=Radiobutton(first,text='b) moment',variable=v6,value=2,bg="#f15922")   ### answer
    r22.place(x=10,y=60)
    r22.configure(font=("Times New Roman",15,"bold"))
    r23=Radiobutton(first,text='c) impulse',variable=v6,value=3,bg="#f15922")
    r23.place(x=10,y=90)
    r23.configure(font=("Times New Roman",15,"bold"))
    r24=Radiobutton(first,text='d) catching time',variable=v6,value=4,bg="#f15922")
    r24.place(x=10,y=120)
    r24.configure(font=("Times New Roman",15,"bold"))

    
    v5=IntVar()
    q5=Label(first,text='2.The different colors of different starts are due to the variation of',bg="#f15922")
    q5.place(x=10,y=180)
    q5.configure(font=("Times New Roman",15,"bold"))
    r17=Radiobutton(first,text='a) temperature',variable=v5,value=1,bg="#f15922")
    r17.place(x=10,y=210)
    r17.configure(font=("Times New Roman",15,"bold"))
    r18=Radiobutton(first,text='b) pressure',variable=v5,value=2,bg="#f15922")
    r18.place(x=10,y=240)
    r18.configure(font=("Times New Roman",15,"bold"))
    r19=Radiobutton(first,text='c) density',variable=v5,value=3,bg="#f15922")
    r19.place(x=10,y=270)
    r19.configure(font=("Times New Roman",15,"bold"))
    r20=Radiobutton(first,text='d) radiation ',variable=v5,value=4,bg="#f15922") ### answer
    r20.place(x=10,y=300)
    r20.configure(font=("Times New Roman",15,"bold"))


    v4=IntVar()
    q4=Label(first,text='3.Woolen clothes keep the body warm because ?',bg="#f15922")
    q4.place(x=10,y=360)
    q4.configure(font=("Times New Roman",15,"bold"))
    #q4=Label(first,text='interest .What is the rate of interest?',bg="#f15922")
    #q4.place(x=10,y=390)
    #q4.configure(font=("Times New Roman",15,"bold"))
    r13=Radiobutton(first,text='a) Wool increases the temperature of the body ',variable=v4,value=1,bg="#f15922") ### answer
    r13.place(x=10,y=390)
    r13.configure(font=("Times New Roman",15,"bold"))
    r14=Radiobutton(first,text='b) Wool is a bad conductor',variable=v4,value=2,bg="#f15922")
    r14.place(x=10,y=420)
    r14.configure(font=("Times New Roman",15,"bold"))
    r15=Radiobutton(first,text='c) Wool absorbs radiant heat from outer objects',variable=v4,value=3,bg="#f15922")
    r15.place(x=10,y=450)
    r15.configure(font=("Times New Roman",15,"bold"))
    r16=Radiobutton(first,text='d) none of the above',variable=v4,value=4,bg="#f15922")
    r16.place(x=10,y=480)
    r16.configure(font=("Times New Roman",15,"bold"))

    exit = Button(first, justify=LEFT,bg="#005367",activebackground="#005367")
    ex = PhotoImage(file="icon.png")
    exit.config(image=ex, width="30", height="30", bd=0, command=first.destroy)
    exit.place(x=1300,y=30)


    v3=IntVar()
    q3=Label(first,text='4.The shape of our milky way galaxy is ?',bg="#005367")
    q3.place(x=700,y=0)
    q3.configure(font=("Times New Roman",15,"bold"),foreground="white")
    r9=Radiobutton(first,text='a) circular',variable=v3,value=1,bg="#005367")
    r9.place(x=700,y=30)
    r9.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r10 = Radiobutton(first, text='b) ellipitical ', variable=v3, value=2,bg="#005367")   ###answer
    r10.place(x=700,y=60)
    r10.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r11 = Radiobutton(first, text="c) sprial", variable=v3, value=3,bg="#005367")
    r11.place(x=700,y=90)
    r11.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r12 = Radiobutton(first, text="d) none of the above ", variable=v3, value=4,bg="#005367")
    r12.place(x=700,y=120)
    r12.configure(font=("Times New Roman",15,"bold"),foreground="orange")

    b=Button(first,justify = LEFT)
    photo=PhotoImage(file="sub2.png")
    b.config(image=photo,width="200",height="40",bd=0,activebackground="#f15922",command=window)
    b.place(x=400,y=600)

    b1=Button(first,justify = LEFT)
    photo1=PhotoImage(file="backbutton.png")
    b1.config(image=photo1,width="200",height="55",activebackground="#f15922",bg="#005367",bd=0,command=function1)
    b1.place(x=900,y=600)

    v2=IntVar()
    q2=Label(first,text='5. If the length of a simple pendulum is halved then its period of oscillation is ',bg="#005367")
    q2.place(x=700,y=180)
    q2.configure(font=("Times New Roman",15,"bold"),foreground="white")
    r5 = Radiobutton(first, text="a) doubled", variable=v2, value=1,bg="#005367")
    r5.place(x=700,y=210)
    r5.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r6 = Radiobutton(first, text="b) halved", variable=v2, value=2,bg="#005367")
    r6.place(x=700,y=240)
    r6.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r7 = Radiobutton(first, text="c)increased by a factor", variable=v2, value=3,bg="#005367")
    r7.place(x=700,y=270)
    r7.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r8 = Radiobutton(first, text="d) decreased by a factor", variable=v2, value=4,bg="#005367")  ##answer
    r8.place(x=700,y=300)
    r8.configure(font=("Times New Roman",15,"bold"),foreground="orange")


    v1=IntVar()
    q=Label(first,text='6.Instrument used to measure the force and velocity  ?',bg="#005367")
    q.place(x=700,y=360)
    q.configure(font=("Times New Roman",15,"bold"),foreground="white")
    r1=Radiobutton(first,text='a) Ammeter',variable=v1,value=1,bg="#005367")
    r1.place(x=700,y=390)
    r1.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r2=Radiobutton(first,text='b) Anemometer ',variable=v1,value=2,bg="#005367")  ##answer
    r2.place(x=700,y=420)
    r2.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r3=Radiobutton(first,text='c) Altimeter',variable=v1,value=3,bg="#005367")
    r3.place(x=700,y=450)
    r3.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r4=Radiobutton(first,text='d) Audiometer',variable=v1,value=4,bg="#005367")
    r4.place(x=700,y=480)
    r4.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    first.mainloop()



    
def satya2():
    global v6,v5,v4,v3,v2,v1,second
    second=Tk()
    second.wm_attributes('-fullscreen','true')
    second.title('MATHS QUIZ')
    back=PhotoImage(file="back6.png")
    bk=Label(second,image=back)
    bk.place(x=0,y=0,relwidth=1,relheight=1)

    v6=IntVar()
    q6=Label(second,text='1.Slope of the line ax+by+c=0 is ',bg="#f15922")
    q6.place(x=10,y=0)
    q6.configure(font=("Times New Roman",15,"bold"))
    r21=Radiobutton(second,text='a) -b/a',variable=v6,value=1,bg="#f15922")
    r21.place(x=10,y=30)
    r21.configure(font=("Times New Roman",15,"bold"))
    r22=Radiobutton(second,text='b) -c/a',variable=v6,value=2,bg="#f15922")
    r22.place(x=10,y=60)
    r22.configure(font=("Times New Roman",15,"bold"))
    r23=Radiobutton(second,text='c) -a/b',variable=v6,value=3,bg="#f15922")
    r23.place(x=10,y=90)
    r23.configure(font=("Times New Roman",15,"bold"))
    r24=Radiobutton(second,text='d) none of the above',variable=v6,value=4,bg="#f15922")
    r24.place(x=10,y=120)
    r24.configure(font=("Times New Roman",15,"bold"))


    v5=IntVar()
    q5=Label(second,text='2.What is the probabiity of getting a sum of 9 from two trows of dies ?',bg="#f15922")
    q5.place(x=10,y=180)
    q5.configure(font=("Times New Roman",15,"bold"))
    r17=Radiobutton(second,text='a) 1/6 ',variable=v5,value=1,bg="#f15922")
    r17.place(x=10,y=210)
    r17.configure(font=("Times New Roman",15,"bold"))
    r18=Radiobutton(second,text='b) 1/8',variable=v5,value=2,bg="#f15922")
    r18.place(x=10,y=240)
    r18.configure(font=("Times New Roman",15,"bold"))
    r19=Radiobutton(second,text='c) 1/9',variable=v5,value=3,bg="#f15922")
    r19.place(x=10,y=270)
    r19.configure(font=("Times New Roman",15,"bold"))
    r20=Radiobutton(second,text='d) 1/12',variable=v5,value=4,bg="#f15922")
    r20.place(x=10,y=300)
    r20.configure(font=("Times New Roman",15,"bold"))


    v4=IntVar()
    q4=Label(second,text='3.A sum of Rs. 12,500 amounts to Rs. 15,500 in 4 years at the rate of simple',bg="#f15922")
    q4.place(x=10,y=360)
    q4.configure(font=("Times New Roman",15,"bold"))
    q4=Label(second,text='interest .What is the rate of interest?',bg="#f15922")
    q4.place(x=10,y=390)
    q4.configure(font=("Times New Roman",15,"bold"))
    r13=Radiobutton(second,text='a) 650',variable=v4,value=1,bg="#f15922")
    r13.place(x=10,y=420)
    r13.configure(font=("Times New Roman",15,"bold"))
    r14=Radiobutton(second,text='b) 690',variable=v4,value=2,bg="#f15922")
    r14.place(x=10,y=450)
    r14.configure(font=("Times New Roman",15,"bold"))
    r15=Radiobutton(second,text='c) 698',variable=v4,value=3,bg="#f15922")
    r15.place(x=10,y=480)
    r15.configure(font=("Times New Roman",15,"bold"))
    r16=Radiobutton(second,text='d) 770',variable=v4,value=4,bg="#f15922")
    r16.place(x=10,y=510)
    r16.configure(font=("Times New Roman",15,"bold"))

    exit = Button(second, justify=LEFT,bg="#005367",activebackground="#005367")
    ex = PhotoImage(file="icon.png")
    exit.config(image=ex, width="30", height="30", bd=0, command=second.destroy)
    exit.place(x=1300,y=30)

    v3=IntVar()
    q3=Label(second,text='4.In how many ways can the etters of the world LEADER can be arranged ?',bg="#005367")
    q3.place(x=700,y=0)
    q3.configure(font=("Times New Roman",15,"bold"),foreground="white")
    r9=Radiobutton(second,text='a) 72',variable=v3,value=1,bg="#005367")
    r9.place(x=700,y=30)
    r9.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r10 = Radiobutton(second, text='b) 144 ', variable=v3, value=2,bg="#005367")
    r10.place(x=700,y=60)
    r10.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r11 = Radiobutton(second, text="c) 360", variable=v3, value=3,bg="#005367")
    r11.place(x=700,y=90)
    r11.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r12 = Radiobutton(second, text="d) 720 ", variable=v3, value=4,bg="#005367")
    r12.place(x=700,y=120)
    r12.configure(font=("Times New Roman",15,"bold"),foreground="orange")

    b=Button(second,justify = LEFT)
    photo=PhotoImage(file="sub2.png")
    b.config(image=photo,width="200",height="40",bd=0,activebackground="#f15922",command=Window1)
    b.place(x=400,y=600)

    b2=Button(second,justify = LEFT)
    photo2=PhotoImage(file="backbutton.png")
    b2.config(image=photo2,width="200",height="55",activebackground="#f15922",bg="#005367",bd=0,command=function2)
    b2.place(x=900,y=600)


    v2=IntVar()
    q2=Label(second,text='5.A sum fetched a total simple interest of Rs. 4016.25 at the rate',bg="#005367")
    q2.place(x=700,y=180)
    q2.configure(font=("Times New Roman",15,"bold"),foreground="white")
    q18=Label(second,text=' of 9 p.c.p.a. in 5 years. What is the sum?',bg="#005367")
    q18.place(x=700,y=210)
    q18.configure(font=("Times New Roman",15,"bold"),foreground="white")
    r5 = Radiobutton(second, text="a)4462.50", variable=v2, value=1,bg="#005367")
    r5.place(x=700,y=240)
    r5.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r6 = Radiobutton(second, text="b)8032.50", variable=v2, value=2,bg="#005367")
    r6.place(x=700,y=270)
    r6.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r7 = Radiobutton(second, text="c)8900", variable=v2, value=3,bg="#005367")
    r7.place(x=700,y=300)
    r7.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r8 = Radiobutton(second, text="d)8925", variable=v2, value=4,bg="#005367")
    r8.place(x=700,y=330)
    r8.configure(font=("Times New Roman",15,"bold"),foreground="orange")


    v1=IntVar()
    q=Label(second,text='6.Log(1/8) to the base x =-3/2',bg="#005367")
    q.place(x=700,y=390)
    q.configure(font=("Times New Roman",15,"bold"),foreground="white")
    r1=Radiobutton(second,text='a)-4',variable=v1,value=1,bg="#005367")
    r1.place(x=700,y=420)
    r1.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r2=Radiobutton(second,text='b)4',variable=v1,value=2,bg="#005367")
    r2.place(x=700,y=450)
    r2.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r3=Radiobutton(second,text='c)1/4',variable=v1,value=3,bg="#005367")
    r3.place(x=700,y=480)
    r3.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r4=Radiobutton(second,text='d)10',variable=v1,value=4,bg="#005367")
    r4.place(x=700,y=510)
    r4.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    second.mainloop()

        
def satya3():
    global v6,v5,v4,v3,v2,v1,third
    third=Tk()
    third.wm_attributes('-fullscreen','true')
    third.title('MATHS QUIZ')
    back=PhotoImage(file="back6.png")
    bk=Label(third,image=back)
    bk.place(x=0,y=0,relwidth=1,relheight=1)
    
    v6=IntVar()
    q6=Label(third,text='1.The green color seen in firework displays is due to the chloride salt of ',bg="#f15922")
    q6.place(x=10,y=0)
    q6.configure(font=("Times New Roman",15,"bold"))
    r21=Radiobutton(third,text='a) strontium',variable=v6,value=1,bg="#f15922")
    r21.place(x=10,y=30)
    r21.configure(font=("Times New Roman",15,"bold"))
    r22=Radiobutton(third,text='b) batrium',variable=v6,value=2,bg="#f15922")   ### answer
    r22.place(x=10,y=60)
    r22.configure(font=("Times New Roman",15,"bold"))
    r23=Radiobutton(third,text='c) sodium',variable=v6,value=3,bg="#f15922")
    r23.place(x=10,y=90)
    r23.configure(font=("Times New Roman",15,"bold"))
    r24=Radiobutton(third,text='d) calcium',variable=v6,value=4,bg="#f15922")
    r24.place(x=10,y=120)
    r24.configure(font=("Times New Roman",15,"bold"))


    v5=IntVar()
    q5=Label(third,text='2.The purest form of Iron',bg="#f15922")
    q5.place(x=10,y=180)
    q5.configure(font=("Times New Roman",15,"bold"))
    r17=Radiobutton(third,text='a) Cast iron',variable=v5,value=1,bg="#f15922")
    r17.place(x=10,y=210)
    r17.configure(font=("Times New Roman",15,"bold"))
    r18=Radiobutton(third,text='b) steel',variable=v5,value=2,bg="#f15922")
    r18.place(x=10,y=240)
    r18.configure(font=("Times New Roman",15,"bold"))
    r19=Radiobutton(third,text='c) pig iron',variable=v5,value=3,bg="#f15922")
    r19.place(x=10,y=270)
    r19.configure(font=("Times New Roman",15,"bold"))
    r20=Radiobutton(third,text='d) wrought iron',variable=v5,value=4,bg="#f15922") ### answer
    r20.place(x=10,y=300)
    r20.configure(font=("Times New Roman",15,"bold"))


    v4=IntVar()
    q4=Label(third,text='3.Peroxyacetly nitrate is a ',bg="#f15922")
    q4.place(x=10,y=360)
    q4.configure(font=("Times New Roman",15,"bold"))
    #q4=Label(third,text='interest .What is the rate of interest?',bg="#f15922")
    #q4.place(x=10,y=390)
    #q4.configure(font=("Times New Roman",15,"bold"))
    r13=Radiobutton(third,text='a) Secondary pollutant',variable=v4,value=1,bg="#f15922") ### answer
    r13.place(x=10,y=390)
    r13.configure(font=("Times New Roman",15,"bold"))
    r14=Radiobutton(third,text='b) acidic dye',variable=v4,value=2,bg="#f15922")
    r14.place(x=10,y=420)
    r14.configure(font=("Times New Roman",15,"bold"))
    r15=Radiobutton(third,text='c) plant hormone',variable=v4,value=3,bg="#f15922")
    r15.place(x=10,y=450)
    r15.configure(font=("Times New Roman",15,"bold"))
    r16=Radiobutton(third,text='d) vitamin',variable=v4,value=4,bg="#f15922")
    r16.place(x=10,y=480)
    r16.configure(font=("Times New Roman",15,"bold"))

    exit = Button(third, justify=LEFT,bg="#005367",activebackground="#005367")
    ex = PhotoImage(file="icon.png")
    exit.config(image=ex, width="30", height="30", bd=0, command=third.destroy)
    exit.place(x=1300,y=30)

    v3=IntVar()
    q3=Label(third,text='4.Most commonly used bleaching agent ?',bg="#005367")
    q3.place(x=700,y=0)
    q3.configure(font=("Times New Roman",15,"bold"),foreground="white")
    r9=Radiobutton(third,text='a) alcohol',variable=v3,value=1,bg="#005367")
    r9.place(x=700,y=30)
    r9.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r10 = Radiobutton(third, text='b) chlorine ', variable=v3, value=2,bg="#005367")   ###answer
    r10.place(x=700,y=60)
    r10.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r11 = Radiobutton(third, text="c) sodium chorine", variable=v3, value=3,bg="#005367")
    r11.place(x=700,y=90)
    r11.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r12 = Radiobutton(third, text="d) cardon dioxide ", variable=v3, value=4,bg="#005367")
    r12.place(x=700,y=120)
    r12.configure(font=("Times New Roman",15,"bold"),foreground="orange")

    b=Button(third,justify = LEFT)
    photo=PhotoImage(file="sub2.png")
    b.config(image=photo,width="200",height="40",bd=0,activebackground="#f15922",command=Window2)
    b.place(x=400,y=600)

    b3=Button(third,justify = LEFT)
    photo3=PhotoImage(file="backbutton.png")
    b3.config(image=photo3,width="200",height="55",activebackground="#f15922",bg="#005367",bd=0,command=function3)
    b3.place(x=900,y=600)



    v2=IntVar()
    q2=Label(third,text='5.Combustion is a ',bg="#005367")
    q2.place(x=700,y=180)
    q2.configure(font=("Times New Roman",15,"bold"),foreground="white")
    #q18=Label(third,text=' of 9 p.c.p.a. in 5 years. What is the sum?',bg="#005367")
    #q18.place(x=700,y=210)
    #q18.configure(font=("Times New Roman",15,"bold"),foreground="white")
    r5 = Radiobutton(third, text="a)Physical and chemical process", variable=v2, value=1,bg="#005367")
    r5.place(x=700,y=210)
    r5.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r6 = Radiobutton(third, text="b)bioogical process", variable=v2, value=2,bg="#005367")
    r6.place(x=700,y=240)
    r6.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r7 = Radiobutton(third, text="c)physical process", variable=v2, value=3,bg="#005367")
    r7.place(x=700,y=270)
    r7.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r8 = Radiobutton(third, text="d)chemical process", variable=v2, value=4,bg="#005367")  ##answer
    r8.place(x=700,y=300)
    r8.configure(font=("Times New Roman",15,"bold"),foreground="orange")


    v1=IntVar()
    q=Label(third,text='6.Which of the following is not a form of carbon ?',bg="#005367")
    q.place(x=700,y=360)
    q.configure(font=("Times New Roman",15,"bold"),foreground="white")
    r1=Radiobutton(third,text='a) soot ',variable=v1,value=1,bg="#005367")
    r1.place(x=700,y=390)
    r1.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r2=Radiobutton(third,text='b)hematite',variable=v1,value=2,bg="#005367")  ##answer
    r2.place(x=700,y=420)
    r2.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r3=Radiobutton(third,text='c) graphite',variable=v1,value=3,bg="#005367")
    r3.place(x=700,y=450)
    r3.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    r4=Radiobutton(third,text='d) charcoal',variable=v1,value=4,bg="#005367")
    r4.place(x=700,y=480)
    r4.configure(font=("Times New Roman",15,"bold"),foreground="orange")
    third.mainloop()

def sai():
    global master
    master=Tk()
    master.wm_attributes('-fullscreen','true')
    master.title('MAIN')
    back1=PhotoImage(file="education1.png")
    bk=Label(master,image=back1)
    bk.place(x=0,y=0,relwidth=1,relheight=1)
    l1=Label(master,text='WELCOME TO THE QUIZ')
    l1.place(x=540,y=100)
    l1.configure(font=("Impact",25,"bold italic"),background='red',foreground='white')

    exit = Button(master, justify=LEFT,bg="#005367",activebackground="#005367")
    ex = PhotoImage(file="icon.png")
    exit.config(image=ex, width="30", height="30", bd=0, command=master.destroy)
    exit.place(x=1300,y=30)

    l2=Button(master,text="Click here to enter PHYSICS QUIZ",command=chai3)
    l2.place(x=30,y=250)
    l2.configure(font=("Times New Roman",15,"bold"))

  
    
    '''    
    exit1 = Button(master, justify=LEFT)
    ex1 = PhotoImage(file="run.png")
    exit1.config(image=ex1, width="30", height="30", bd=0, command=chai1)
    exit1.place(x=370,y=240)
    '''
    
    l4=Button(master,text="Click here to enter MATHS QUIZ",command=chai2)
    l4.place(x=30,y=350)
    l4.configure(font=("Times New Roman",15,"bold"))    
    '''
    exit2 = Button(master, justify=LEFT,activebackground="#005367")
    ex2 = PhotoImage(file="run.png")
    exit2.config(image=ex2, width="30", height="30", bd=0, command=chai2)
    exit2.place(x=370,y=340)
    '''
    
    l3=Button(master,text="Click here to enter CHEMISTRY QUIZ",command=chai3)
    l3.place(x=30,y=450)
    l3.configure(font=("Times New Roman",15,"bold"))
    '''
    exit3 = Button(master, justify=LEFT,activebackground="#005367")
    ex3 = PhotoImage(file="run.png")
    exit3.config(image=ex3, width="30", height="30", bd=0, command=chai3)
    exit3.place(x=390,y=440)
    '''
    back2=PhotoImage(file="images143.png")
    bk=Label(master,image=back2)
    bk.place(x=1000,y=350)
    
    master.mainloop()
    
sai()
    
