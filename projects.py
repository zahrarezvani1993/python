# number= int(input("please give me your number"))

# print("binary your numbers is %s"%(bin(number)))

# print("octal your numbers is %s"%(oct(number)))

# print("hexadecimal your numbers is %s"%(hex(number)))

# horof=("a","e","o","u","i")
# message=input("give me your message")
# newMassage =''
# for letters in message:
#     if letters not in horof:
#         newMassage+=letters

# print(newMassage)


# mydict={"A":"D","B":"Q","C":"Z","1":"9","2":"8","3":"7"}
# message= input("give me your massage here").upper()
# messageencrypted  =""

# for letters in message:
#     if letters in mydict:
#         messageencrypted += mydict[letters]
#     else:
#         messageencrypted += letters

# print(messageencrypted.lower())



# mydict2={"D":"A","Q":"B","Z":"C","9":"1","8":"2","7":"3"}
# message2= input("give me your message encypted").upper()
# messagedecrypted=""

# for letters in message2:
#     if letters in mydict2:
#         messagedecrypted+=mydict2[letters]
#     else:
#         messagedecrypted+=letters

# print(messagedecrypted.lower())


# def add(a,b):
#     return(a+b)
# def substract(a,b):
#     return(a-b)
# def multiply(a,b):
#     return(a*b)
# def divide(a,b):
#     return(a/b)

# print("select opration ==>  1:add   or   2:substract  or   3:multiply  or   4:divide")
# choice= input("choice 1/2/3/4 : ")
# num_1=int(input("enter first number: "))
# num_2=int(input("enter second number: "))

# if choice=="1":
#     print(num_1," + " , num_2," = ",add(num_1,num_2))
# elif choice=="2":
#     print(num_1," - " , num_2," = ",substract(num_1,num_2))
# elif choice=="3":
#     print(num_1," * " , num_2," = ",multiply(num_1,num_2))
# elif choice=="4":
#     print(num_1," / " , num_2," = ",divide(num_1,num_2))
# else:
#     print("vorodiha namotabar ast!!!")



# import re
# p= input("enter your password: ")
# x=True

# while x:
#     if (len(p)<8 or len(p)>16):
#         break
#     elif not re.search("[a-z]",p):
#         break
#     elif not re.search("[1-9]",p):
#         break
#     else:
#         x=False
#         print("password is valid")

# if x==True:
#     print("password is invalid")


# class person():
#     def __init__(self,name,family):
#         self.name=name
#         self.family=family
#     def person_info(self):
#         print(self.name)
#         print(self.family)

# class teacher(person):
#     def __init__(self,name,family,id):
#         person. __init__(self,name,family)
#         self.id=id
#     def teacher_info(self):
#         print(self.id)

# teacher1=teacher("zahra","rezvani",123)
# teacher1.person_info()
# teacher1.teacher_info()


# def calc():
#     number1=int(input("please enter your first number: "))
#     number2=int(input("please enter your second number: "))
#     operator=input('''
# please enter opeator: 
#                    + or - or * or /     
# ''')
#     if operator=="+":
#         output=number1 + number2
#         print("{} + {} = {}".format(number1,number2,output))
#     elif operator=="-":
#         output=number1 - number2
#         print("{} - {} = {}".format(number1,number2,output))
#     elif operator=="*":
#         output=number1 * number2
#         print("{} * {} = {}".format(number1,number2,output))
#     elif operator=="/":
#         output=number1 / number2
#         print("{} / {} = {}".format(number1,number2,output))
#     else:
#         print("vorodiha namotabar")
#     again()

# def again():
#     again=input("do you want to run again?")
#     if again.upper()=="Y":
#         calc()
#     elif again.upper()=="N":
#         print("see you letter...")
#     else:
#         again()

# calc()



# words=["rr","aa","ss"]
# values=[18,8,13]
# dicta={i:j for i,j in zip(words,values)}
# dictb={i:j for i,j in zip(words,values) if j>10}
# dictc={i.upper():j**2 for i,j in zip(words,values)}
# print(dicta)
# print(dictb)
# print(dictc)




# import random
# import tkinter as tk
# window = tk.Tk()
# window.geometry("500x500")
# window.title("sang kaghaz ghichi")

# user_score=0
# comp_score=0
# user_choice=""
# comp_choice=""

# def choice_to_number(choice):
#     rps={"sang":0,"kaghaz":1,"gheychi":2}
#     return rps[choice]
# def number_to_choice(number):
#     rps={0:"sang",1:"kaghaz",2:"gheychi"}
#     return rps[number]
# def random_comp_choice():
#     return random.choice(["sang","kaghaz","gheychi"])

# def result(user_choice,comp_choice):
#     global user_score
#     global comp_score
#     user=choice_to_number(user_choice)
#     comp=choice_to_number(comp_choice)
#     if (user==comp):
#         print("mosavi shodid")
#     elif (((user-comp)%3)==1):
#         print("user bord")
#         user_score+=1
#     else:
#         print("man bordam")
#         comp_score+=1
    
#     textarea=tk.Text(height=10,width=200,bg="#fffff5")
#     textarea.grid(column=3,row=1)
#     answer="entekhab shoma : {} \nentekhab computer : {} \nemtiyaz shoma : {} \nemtiyaz computer : {}".format(user_choice,comp_choice,user_score,comp_score)
#     textarea.insert(tk.END,answer)

# def sang():
#     global user_choice
#     global comp_choice
#     user_choice="sang"
#     comp_choice=random_comp_choice()
#     result(user_choice,comp_choice)

# def kaghaz():
#     global user_choice
#     global comp_choice
#     user_choice="kaghaz"
#     comp_choice=random_comp_choice()
#     result(user_choice,comp_choice)

# def gheychi():
#     global user_choice
#     global comp_choice
#     user_choice="gheychi"
#     comp_choice=random_comp_choice()
#     result(user_choice,comp_choice)

# button1=tk.Button(text="sang",bg="skyblue",command=sang)
# button1.grid(column=0,row=0)
# button2=tk.Button(text="kaghaz",bg="#ffffff",command=kaghaz)
# button2.grid(column=1,row=0)
# button3=tk.Button(text="gheychi",bg="red",command=gheychi)
# button3.grid(column=2,row=0)
# window.mainloop()




# import os

# print("1,shutdown 0s")
# print("2,shutdown xs")
# print("3,restart 0s")
# print("4,restart xs")
# print("5,exit")
# choice=int(input("entekhabtan ra vared khonid : "))

# if choice==1:
#     os.system("shutdown /s /t 0")
# elif choice==2:
#     sec=input("zaman morede nazar ra vared konid : ")
#     os.system("shutdown /s /t "+sec)
# elif choice==3:
#     os.system("shutdown /r /t 0")
# elif choice==4:
#     sec=input("zaman morede nazar ra vared konid : ")
#     os.system("shutdown /r /t "+sec)
# elif choice==5:
#     exit()
# else:
#     print("vorodi eshtebah ast !!!")




# def repeted(x):
#     size=len(x)
#     repeted=[]
#     for i in range(size):
#         k=i+1
#         for j in range(k,size):
#             if x[i]==x[j] and x[i] not in repeted:
#                 repeted.append(x[i])
#     return repeted


# list1=[1,14,3,1,14,20,50,20]
# print(repeted(list1))




# def binary_search(arr,low,high,x):
#     if high>=low:
#         mid=(high+low)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]>x:
#             return binary_search(arr,low,mid-1,x)
#         else:
#             return binary_search(arr,mid+1,high,x)
#     else:
#         return(-1)

# a=[1,3,5,6,34,50,78,90,120]  
# result=binary_search(a,0,len(a)-1,3)
# if result != -1:
#     print(result)
# else:
#     print("adade shoma dakhele list nist.")



# from tkinter import *
# from functools import partial

# def validatelogin(username,password):
#     print("username Enter: ",username.get())
#     print("password Enter: ",password.get())
#     return

# tkwindow=Tk()
# tkwindow.geometry("400x500")
# tkwindow.title("login form")

# usernamelabel=Label(tkwindow,text="username").grid(row=0,column=0)
# username=StringVar()
# usernameentry=Entry(tkwindow,textvariable=username).grid(row=0,column=1)

# passwordlabel=Label(tkwindow,text="password").grid(row=1,column=0)
# password=StringVar()
# passwordentry=Entry(tkwindow,textvariable=password,show='*').grid(row=1,column=1)

# validatelogin=partial(validatelogin,username,password)

# loginbutton=Button(tkwindow,text="login",command=validatelogin).grid(row=4,column=0)
# tkwindow.mainloop()



# calculator
from tkinter import *

WindowsTk=Tk()
WindowsTk.title("calaulator")
WindowsTk.resizable(False,False)

operator=""
input=StringVar()

def btnClick(number):
    global operator
    operator=operator+str(number)
    input.set(operator)

def clear():
    global operator
    operator=""
    input.set("")

def answer():
    try:
        global operator
        answer=str(eval(operator))
        input.set(answer)
        operator=answer
    except:
        operator=""
        input.set("Error")

# showanswer
TextDisplay = Entry(WindowsTk,font=("arial",20,"bold"),textvariable=input,bd=30,insertwidth=4,bg="gray",justify="right").grid(row=0,columnspan=4)

#button
btn7 = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "7", command = lambda:btnClick(7)).grid(row = 1, column = 0)

btn8=Button(WindowsTk,padx=16,bd=8,fg="black",bg="gray",font=("arial",20,"bold"),text="8",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(WindowsTk,padx=16,bd=8,fg="black",bg="gray",font=("arial",20,"bold"),text="9",command=lambda:btnClick(9)).grid(row=1,column=2)

btnadd=Button(WindowsTk,padx=16,bd=8,fg="black",bg="gray",font=("arial",20,"bold"),text="+",command=lambda:btnClick("+")).grid(row=1,column=3)

btn4 = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "4", command = lambda:btnClick(4)).grid(row = 2, column = 0)

btn5 = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "5", command = lambda:btnClick(5)).grid(row = 2, column = 1)

btn6 = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "6", command = lambda:btnClick(6)).grid(row = 2, column = 2)

Sub = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "-", command = lambda:btnClick("-")).grid(row = 2, column = 3)

btn1 = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "1", command = lambda:btnClick(1)).grid(row = 3, column = 0)

btn2 = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "2", command = lambda:btnClick(2)).grid(row = 3, column = 1)

btn3 = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "3", command = lambda:btnClick(3)).grid(row = 3, column = 2)

Multiply = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "*", command = lambda:btnClick("*")).grid(row = 3, column = 3)

tn0 = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "0", command = lambda:btnClick(0)).grid(row = 4, column = 0)

equal = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "=", command = answer).grid(row = 4, column = 1)

divide = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "/", command = lambda:btnClick("/")).grid(row = 4, column = 2)

clear = Button(WindowsTk, padx = 16, bd = 8, fg = "black", bg = "gray", font = ('arial', 20, 'bold'), text = "c", command = clear).grid(row = 4, column = 3)


WindowsTk.mainloop()