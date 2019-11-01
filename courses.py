# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:39:07 2019

@author: srika
"""

import pandas as pd
from tkinter import *
top=Tk()
j=0
top.geometry("1000x700+0+0")
top.title("QUIZ")
image1 =PhotoImage(file='C:/Users/srika/Desktop/yu.png')    
Form1 = Label(top, image=image1)
Form1.pack(side='top', fill='both', expand='yes')
data=pd.read_csv('C:/Users/srika/Desktop/temp.csv')

def display():
    
    chai=Tk()
    chai.geometry("500x400+0+0")
    Label(chai,text="college id").grid(row=0,column=0)
    Label(chai,text="college Name").grid(row=0,column=1)
    Label(chai,text="NIRF Ranking").grid(row=0,column=2)
    Label(chai,text="Fees").grid(row=0,column=3)
                
    i=0
    
    while i<10:
        
        Label(chai,text=str(data['college id'][i])).grid(row = 1 +i, column = 0)
        Label(chai,text=str(data['Name'][i])).grid(row = 1 +i, column = 1)
        Label(chai,text=str(data['NIRF Ranking'][i])).grid(row = 1 +i, column = 2)
        Label(chai,text=str(data['Fees(in lakhs)'][i])).grid(row = 1 +i, column = 3)
        i+=1   
    
def show():
    cha=Tk()
    cha.geometry("600x400+0+0")
    Label(cha,text="college id").grid(row=0,column=0)
    Label(cha,text="college Name").grid(row=0,column=1)
    Label(cha,text="NIRF Ranking").grid(row=0,column=2)
    Label(cha,text="Fees").grid(row=0,column=3)

    i=11
    
    while i>10 and i<20:
        
        Label(cha,text=str(data['college id'][i])).grid(row = 1 +i, column = 0)
        Label(cha,text=str(data['Name'][i])).grid(row = 1 +i, column = 1)
        Label(cha,text=str(data['NIRF Ranking'][i])).grid(row = 1 +i, column = 2)
        Label(cha,text=str(data['Fees(in lakhs)'][i])).grid(row = 1 +i, column = 3)
        i+=1   
def show1():
    cha1=Tk()
    cha1.geometry("600x400+0+0")
    Label(cha1,text="college id").grid(row=0,column=0)
    Label(cha1,text="college Name").grid(row=0,column=1)
    Label(cha1,text="NIRF Ranking").grid(row=0,column=2)
    Label(cha1,text="Fees").grid(row=0,column=3)
    
    i=22
    
    while i>20 and i<32:
        Label(cha1,text=str(data['college id'][i])).grid(row = 1 +i, column = 0)
        Label(cha1,text=str(data['Name'][i])).grid(row = 1 +i, column = 1)
        Label(cha1,text=str(data['NIRF Ranking'][i])).grid(row = 1 +i, column = 2)
        Label(cha1,text=str(data['Fees(in lakhs)'][i])).grid(row = 1 +i, column = 3)
        i+=1   
    

def show2() :
    cha2=Tk()
    cha2.geometry("600x400+0+0")
    Label(cha2,text="college id").grid(row=0,column=0)
    Label(cha2,text="college Name").grid(row=0,column=1)
    Label(cha2,text="NIRF Ranking").grid(row=0,column=2)
    Label(cha2,text="Fees").grid(row=0,column=3)
                
    i=33
    
    while i>32 and i<43:
        
        Label(cha2,text=str(data['college id'][i])).grid(row = 1 +i, column = 0)
        Label(cha2,text=str(data['Name'][i])).grid(row = 1 +i, column = 1)
        Label(cha2,text=str(data['NIRF Ranking'][i])).grid(row = 1 +i, column = 2)
        Label(cha2,text=str(data['Fees(in lakhs)'][i])).grid(row = 1 +i, column = 3)
        i+=1   

def show3() :
    cha3=Tk()
    cha3.geometry("500x400+0+0")
    Label(cha3,text="college id").grid(row=0,column=0)
    Label(cha3,text="college Name").grid(row=0,column=1)
    Label(cha3,text="NIRF Ranking").grid(row=0,column=2)
    Label(cha3,text="Fees").grid(row=0,column=3)
            
    i=44
    
    while i>43 and i<53:
        
        Label(cha3,text=str(data['college id'][i])).grid(row = 1 +i, column = 0)
        Label(cha3,text=str(data['Name'][i])).grid(row = 1 +i, column = 1)
        Label(cha3,text=str(data['NIRF Ranking'][i])).grid(row = 1 +i, column = 2)
        Label(cha3,text=str(data['Fees(in lakhs)'][i])).grid(row = 1 +i, column = 3)
        i+=1   
    
def show4() :
    cha4=Tk()
    cha4.geometry("500x400+0+0")
    Label(cha4,text="college id").grid(row=0,column=0)
    Label(cha4,text="college Name").grid(row=0,column=1)
    Label(cha4,text="NIRF Ranking").grid(row=0,column=2)
    Label(cha4,text="Fees").grid(row=0,column=3)
            
    i=55
    
    while i>54 and i<64:
        
        Label(cha4,text=str(data['college id'][i])).grid(row = 1 +i, column = 0)
        Label(cha4,text=str(data['Name'][i])).grid(row = 1 +i, column = 1)
        Label(cha4,text=str(data['NIRF Ranking'][i])).grid(row = 1 +i, column = 2)
        Label(cha4,text=str(data['Fees(in lakhs)'][i])).grid(row = 1 +i, column = 3)
        i+=1   

    
def show5() :
    cha5=Tk()
    cha5.geometry("500x400+0+0")
    Label(cha5,text="college id").grid(row=0,column=0)
    Label(cha5,text="college Name").grid(row=0,column=1)
    Label(cha5,text="NIRF Ranking").grid(row=0,column=2)
    Label(cha5,text="Fees").grid(row=0,column=3)
            
    i=66
    
    while i>65 and i<76:
        
        Label(cha5,text=str(data['college id'][i])).grid(row = 1 +i, column = 0)
        Label(cha5,text=str(data['Name'][i])).grid(row = 1 +i, column = 1)
        Label(cha5,text=str(data['NIRF Ranking'][i])).grid(row = 1 +i, column = 2)
        Label(cha5,text=str(data['Fees(in lakhs)'][i])).grid(row = 1 +i, column = 3)
        i+=1   

def show6() :
    cha6=Tk()
    cha6.geometry("600x450+0+0")
    Label(cha6,text="college id").grid(row=0,column=0)
    Label(cha6,text="college Name").grid(row=0,column=1)
    Label(cha6,text="NIRF Ranking").grid(row=0,column=2)
    Label(cha6,text="Fees").grid(row=0,column=3)
    
    i=77
    
    while i>76 and i<87:
        
        Label(cha6,text=str(data['college id'][i])).grid(row = 1 +i, column = 0)
        Label(cha6,text=str(data['Name'][i])).grid(row = 1 +i, column = 1)
        Label(cha6,text=str(data['NIRF Ranking'][i])).grid(row = 1 +i, column = 2)
        Label(cha6,text=str(data['Fees(in lakhs)'][i])).grid(row = 1 +i, column = 3)
        i+=1   

    
b4=Button(top,text="Enginnering",width=25,height=1,bg="light green",command=display)
b4.place(x=30,y=310)
b4.config(font=("Times New Roman",15,"bold"))

b5=Button(top,text="B.com",width=25,height=1,bg="light green",command=show)
b5.place(x=30,y=410)
b5.config(font=("Times New Roman",15,"bold"))
b6=Button(top,text="Medical",width=25,height=1,bg="light green",command=show1)
b6.place(x=30,y=510)
b6.config(font=("Times New Roman",15,"bold"))
b7=Button(top,text="LLB",width=25,height=1,bg="light green",command=show2)
b7.place(x=30,y=610)
b7.config(font=("Times New Roman",15,"bold"))
b8=Button(top,text="Arts",width=25,height=1,bg="light green",command=show3)
b8.place(x=400,y=410)
b8.config(font=("Times New Roman",15,"bold"))
b9=Button(top,text="Design",width=25,height=1,bg="light green",command=show4)
b9.place(x=400,y=310)
b9.config(font=("Times New Roman",15,"bold"))
b10=Button(top,text="B.Sc",width=25,height=1,bg="light green",command=show5)
b10.place(x=400,y=510)
b10.config(font=("Times New Roman",15,"bold"))
b11=Button(top,text="BBA",width=25,height=1,bg="light green",command=show6)
b11.place(x=400,y=610)
b11.config(font=("Times New Roman",15,"bold"))

top.mainloop()
