from tkinter import *
top=Tk()
top.geometry("1000x700+0+0")
top.title("QUIZ")
Form1=Label(top)
Form1.pack(side='top', fill='both', expand='yes')
Form1.config(background="light blue")

questions= [
    "QUES.1. The purest form of Iron is: ",
    "QUES.2. Peroxyacetyl nitrate is a",
    "QUES.3. Most commonly used bleaching agent is",
    "QUES.4. Combustion is a ",
    "QUES.5. Which of the following is not a form of carbon?",
    "QUES.6. The mercury and sodium street lamps light up because of",
    "QUES.7. When a helium atom loses an electron it becomes",
    "QUES.8. Asteroids revolve round the sun between which of the following two planets?",
    "QUES.9. Which of the following is used in pencils?",
    "QUES.10. Natural radioactivity was discovered by?"
]

options = [
    ["(1)Cast iron ","(2)Steel", "(3)Pig iron", "(4)Wrought iron "],
    ["(1)Secondary pollutant","(2)acidic dye ", "(3)plant harmone", "(4)vitamin"],
    ["(1)alchol","(2)chlorine ", "(3)sodium chloride", "(4)carbon dioxide"],
    ["(1)physical and chemical process  ","(2)biological process ", "(3)physical process", "(4)chemical process"],
    ["(1)Soot","(2)Hematite", "(3)Graphite", "(4)Charcoal    "],
    ["(1)a)atomic absorption ","(2)atomic emission", "(3)electron absorption", "(4)electron emission      "],
    ["(1)an alpha particle","(2)a proton ", "(3)a positive helium ion", "(4)a negative helium ion"],
    ["(1)Earth and Mars  ","(2)Mars and Jupiter ", "(3)Jupiter and saturn", "(4)Saturn and Uranus"],
    ["(1)Graphite   ","(2)Sulphur     ", "(3) Phosphorus         ", "(4)Charcoal   "],
    ["(1)Rutherford  ","(2)Marie curie ", "(3)Henri Becqurel    ", "(4)Enrico fermi "]
]

a       = [4, 1, 2, 4, 2, 2, 3, 3, 1, 3]
answers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
j=0

#def save():
 #   global j
  #  print(j)
   # k=int(v.get())
    #answers[j]=k
def previous():
    global j
    j=j-1
    if j<=0:
        top.destroy()
    else:
        display()
def next1():
    global j
    j=j+1
    if j>=10:
        end()
    else:
        display()
'''        
def end():
    p=0
    m=0
    print(answers)
    while(p!=10):
        if answers[p]==a[p]:
            m=m+1
            p=p+1
        else:
            p=p+1
    #print("you have got ",m,"/ 10 marks")
    #fp1=open("result.txt","w")
    #fp1.write(str(m))
    #fp1.close()
    top.destroy()
    #import result_of_quiz
 '''   
def end():
    chai=Tk()
    count=0
    temp=0
    j=0
    chai.title('Result')
    chai.geometry('1000x700+0+0')
    f1=Frame(chai)
    #result=PhotoImage('C:/Users/srika/Desktop/project/yu.png')
    #ck=Label(chai,image=result)
    #ck.place(x=0,y=0,rewidth=1,relheight=1)
    #ck.pack()
    f1.place()
    
    while(temp!=10):
        if answers[temp]==a[temp]:
            count=count+1
            temp=temp+1    
        else:
            temp=temp+1
    l15=Label(chai,text=count,borderwidth=10)
    l15.place(x=600,y=50)
    l15.configure(font=("Times New Roman",300,"bold"))
    l14=Label(chai,text="MARKS",borderwidth=10)
    l14.place(x=630,y=450)
    l14.configure(font=("Times New Roman",30,"bold"))

    Attempt=10-temp
    l10=Label(chai,text=temp,borderwidth=10)
    l10.place(x=550,y=600)
    l10.configure(font=("Times New Roman",20,"bold"))
    l11=Label(chai,text=Attempt,borderwidth=10)
    l11.place(x=1100,y=600)
    l11.configure(font=("Times New Roman",20,"bold"))
    l12=Label(chai,text="UNATTEMPTED",borderwidth=10)
    l12.place(x=300,y=600)
    l12.configure(font=("Times New Roman",20,"bold"))
    l13=Label(chai,text="ATTEMPTED",borderwidth=10)
    l13.place(x=900,y=600)
    l13.configure(font=("Times New Roman",20,"bold"))

def display():
    print(j)
    l2=Label(top,text=questions[j])
    l2.place(x=30,y=40)
    l2.configure(font=("Times New Roman",15,"bold"))

    r1=Radiobutton(top,text=options[j][0],variable=v,value=1)
    r1.place(x=30,y=70)
    r1.configure(font=("Times New Roman",15,"bold"))

    r2=Radiobutton(top,text=options[j][1],variable=v,value=2)
    r2.place(x=30,y=100)
    r2.configure(font=("Times New Roman",15,"bold"))
    r3=Radiobutton(top,text=options[j][2],variable=v,value=3)
    r3.place(x=30,y=130)
    r3.configure(font=("Times New Roman",15,"bold"))
    r4=Radiobutton(top,text=options[j][3],variable=v,value=4)
    r4.place(x=30,y=160)
    r4.configure(font=("Times New Roman",15,"bold"))

    
#c=Canvas(top,bg="blue",height=250,width=300)
#c.pack()
#coord=10,50,240,300
v=IntVar()
l=Label(top,text="welcome")
l.place(x=10,y=0)
l.configure(font=("Times New Roman",15,"bold"))

#l3=Label(top,text=name)
#l3.place(x=20,y=30)
display()
#b1=Button(top,text="Save",width=45,height=1,command=save,bg="red")
#b1.place(x=30,y=200)
b2=Button(top,text="Previous",width=45,height=1,command=previous,bg="red")
b2.place(x=30,y=230)
b2.configure(font=("Times New Roman",15,"bold"))
b3=Button(top,text="Next",width=45,height=1,command=next1,bg="red")
b3.place(x=30,y=270)
b3.configure(font=("Times New Roman",15,"bold"))
b4=Button(top,text="End",width=45,height=1,command=end,bg="red")
b4.place(x=30,y=310)
b4.configure(font=("Times New Roman",15,"bold"))

top.mainloop()
