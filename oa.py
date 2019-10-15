from tkinter import*
def Homewindow():
    global Home

def Sel():
     global top,window
     if window==1:
        top.withdraw()
        
     window=1
    

     selection="you selected option"+str(var.get())
     label.config(text=selection)
root = Tk()
var = IntVar()
#v.set(1)  # initializing the choice, i.e. Python
root.geometry("1000x700+0+0")
    
    
Form1 = Label(root)
Form1.pack(side='top', fill='both', expand='yes')
Form1.config(background="light blue")
    
def next():
    global top,window
    if window==1:
        top.withdraw()
    window=1
        
    
    top=Tk()
    

    top.geometry("1000x700+0+0")
    top.config(background="light blue")
    f2=Label(top, text="""2.A sum fetched a total simple interest of Rs. 4016.25 at the rate of 9 p.c.p.a. in 5 years. What is the sum?""",fg="red",font=(14),bd=10)
    f2.place(x=10,y=0)
    R5 = Radiobutton(top, text="4462.50", variable=var, value=1, command=Sel)
    R5.place(x=10,y=30)
    R6 = Radiobutton(top, text="8032.50", variable=var, value=2, command=Sel)
    R6.place(x=10,y=60)
    R7 = Radiobutton(top, text="8900", variable=var, value=3, command=Sel)
    R7.place(x=10,y=90)
    R8 = Radiobutton(top, text="8925", variable=var, value=4, command=Sel)
    R8.place(x=10,y=120)
    next1=Button(top,text="Next",width=45,command=next2,height=2,bg="red")
    next1.place(x=50,y=600)
    previous1=Button(top,text="Previous",width=45,height=2,command=previous,bg="red")
    previous1.place(x=600,y=600)

def next2():
    global top,wndow
    if window==1:
        top.withdraw()
    window=1
        
    
    
    
    t2=Tk()
    t2.geometry("1000x700+0+0")
    t2.config(background="light blue")
   
    f3=Label(t3, text="""4.A sum of Rs. 12,500 amounts to Rs. 15,500 in 4 years at the rate of simple interest. What is the rate of interest?""",fg="red",font=(14),bd=10)
    f3.place(x=10,y=0)

    R9 = Radiobutton(t2, text="650", variable=var, value=1, command=Sel)
    R9.place(x=10,y=30)
    R10 = Radiobutton(t2, text="690", variable=var, value=2, command=Sel)
    R10.place(x=10,y=60)
    R11 = Radiobutton(t2, text="698", variable=var, value=3, command=Sel)
    R11.place(x=10,y=90)
    R12= Radiobutton(t2, text="700", variable=var, value=4, command=Sel)
    R12.place(x=10,y=120)
    next2=Button(t2,text="Next",width=45,command=next3,height=2,bg="red")
    next2.place(x=50,y=600)
    previous2=Button(t2,text="Previous",width=45,height=2,command=previous,bg="red")
    previous2.place(x=600,y=600)

def next3():
    global top,window
    if window==1:
        top.withdraw()
    window=1
        
    
    
    
    t3=Tk()
    t3.geometry("1000x700+0+0")
    t3.config(background="light blue")
    f4=Label(t3, text="""4.A sum of Rs. 12,500 amounts to Rs. 15,500 in 4 years at the rate of simple interest. What is the rate of interest?""",fg="red",font=(14),bd=10)
    f4.place(x=10,y=0)
    R13 = Radiobutton(t3, text="650", variable=var, value=1, command=Sel)
    R13.place(x=10,y=30)
    R14 = Radiobutton(t3, text="690", variable=var, value=2, command=Sel)
    R14.place(x=10,y=60)
    R15 = Radiobutton(t3, text="698", variable=var, value=3, command=Sel)
    R15.place(x=10,y=90)
    R16= Radiobutton(t3, text="700", variable=var, value=4, command=Sel)
    R16.place(x=10,y=120)
    next3=Button(t3,text="Next",width=45,command=next4,height=2,bg="red")
    next3.place(x=50,y=600)
    previous3=Button(t3,text="Previous",width=45,height=2,command=previous,bg="red")
    previous3.place(x=600,y=600)

    
def next4():
    t4=Tk()
    t4.geometry("1000x700+0+0")
    t4.config(background="light blue")
    f5=Label(t4, text="""4.A sum of Rs. 12,500 amounts to Rs. 15,500 in 4 years at the rate of simple interest. What is the rate of interest?""",fg="red",font=(14),bd=10)
    f5.place(x=10,y=0)
    R17 = Radiobutton(t4, text="650", variable=var, value=1, command=Sel)
    R17.place(x=10,y=30)
    R18 = Radiobutton(t4, text="690", variable=var, value=2, command=Sel)
    R18.place(x=10,y=60)
    R19 = Radiobutton(t4, text="698", variable=var, value=3, command=Sel)
    R19.place(x=10,y=90)
    R20= Radiobutton(t4, text="700", variable=var, value=4, command=Sel)
    R20.place(x=10,y=120)
    next4=Button(t4,text="Next",width=45,command=next5,height=2,bg="red")
    next4.place(x=50,y=600)
    previous3=Button(t4,text="Previous",width=45,height=2,command=previous,bg="red")
    previous3.place(x=600,y=600)

    


def previous():
    f1=Label(root, text="""1.Behavior:Psycology::plant:?""",fg="red",font=(14),bd=10)
    f1.place(x=10,y=0)
    R1 = Radiobutton(root, text="plant", variable=var, value=1, command=Sel)
    R1.place(x=10,y=40)
#R1.pack( anchor = W )
    R2 = Radiobutton(root, text="Botany", variable=var, value=2, command=Sel)
    R2.place(x=10,y=70)
#R2.pack( anchor = W )
    R3 = Radiobutton(root, text="zoology", variable=var, value=3, command=Sel)
    R3.place(x=10,y=100)
#R3.pack( anchor = W )
    R4 = Radiobutton(root, text="physology", variable=var, value=4, command=Sel)
#R4.pack( anchor = W )
    R4.place(x=10,y=130)

    






f1=Label(root, text="""1.Behavior:Psycology::plant:?""",fg="red",font=(14),bd=10)
f1.place(x=10,y=10)

#f1.pack()
R1 = Radiobutton(root, text="plant", variable=var, value=1, command=Sel)
R1.place(x=80,y=80)
#R1.pack( anchor = W )
R2 = Radiobutton(root, text="Botany", variable=var, value=2, command=Sel)
R2.place(x=80,y=120)
#R2.pack( anchor = W )
R3 = Radiobutton(root, text="zoology", variable=var, value=3, command=Sel)
R3.place(x=80,y=160)
#R3.pack( anchor = W )
R4 = Radiobutton(root, text="physology", variable=var, value=4, command=Sel)
#R4.pack( anchor = W )
R4.place(x=80,y=200)
next=Button(root,text="Next",width=45,height=2,command=next,bg="red")
next.place(x=50,y=600)

    
previous=Button(root,text="Previous",width=45,height=2,command=previous,bg="red")
previous.place(x=600,y=600)

label=Label(root)
label.pack()
root.mainloop()
