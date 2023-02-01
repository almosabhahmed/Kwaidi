from tkinter import *
import os
import sys
from tkinter import messagebox
import webbrowser
pro=Tk()
pro.geometry('800x450+280+50')
pro.resizable(False,False)
pro.title('Kwaidi.com')
pro.iconbitmap("C:\\Users\\WN\\Desktop")
title=Label(pro,text='KWAIDI COMPANY',width=90,height=2,fg='turquoise',bg='#0B2F3A',font=('tajawal',16,'bold'))
title.place(x=-300,y=0)
u1='https://www.facebook.com/profile.php?id=100063618753746'
u2='https://www.youtube.com/@KWAIDI'
u3='https://www.youtube.com/channel/UCa-jdtsBc_X7X7NHoi1_Ovg'
u4='https://twitter.com/KWAIDI_COM'
u5='https://www.instagram.com/kwaidi/'
u6=''

def Open1():
    webbrowser.open_new(u1)
def Open2():
    webbrowser.open_new(u2)
def Open3():
    webbrowser.open_new(u3)
def Open4():
    webbrowser.open_new(u4)
def Open5():
    webbrowser.open_new(u5)


def log():
        user = En1.get()
        passw=En2.get()
        if user =='Kwaidi' and passw == '123456':
            messagebox.showinfo('Welcome','اهلا وسهلا بك')
        else:
            messagebox.showinfo('Error','عفوا.البيانات المدخلة غير صحيحه')



F1=Frame(pro,width=230,height=420,bg='#0B2F3A')
F1.place(x=570,y=37)
title1=Label (F1,text='كوايـــــــدي مـــــول',fg='turquoise',width=18,bg='#0B2F3A',font=('tajawal',20,'bold'))
title1.place(x=-40,y=0)
title2=Button(F1,text='عن المؤسس حيدر النجار',width=18,fg='black',bg='turquoise3',font=('tajawal',16,'bold'),command=Open3)
title2.place(x=0,y=60)
title3=Button(F1,text='عن شركة كوايدي',width=18,fg='black',bg='turquoise3',font=('tajawal',16,'bold'),command=Open2)
title3.place(x=0,y=105)
title3=Button(F1,text='حسابنا على تــويتر',width=18,fg='black',bg='turquoise3',font=('tajawal',16,'bold'),command=Open4)
title3.place(x=0,y=150)
title3=Button(F1,text='حسابنا على انستقرام',width=18,fg='black',bg='turquoise3',font=('tajawal',16,'bold'),command=Open5)
title3.place(x=0,y=195)
title3=Button(F1,text='حسابنا على فيس بوك',width=18,fg='black',bg='turquoise3',font=('tajawal',16,'bold'),command=Open1)
title3.place(x=0,y=240)
title3=Button(F1,text='حسابنا على تـيـلقـرام',width=18,fg='black',bg='turquoise3',font=('tajawal',16,'bold'))
title3.place(x=0,y=285)
title3=Button(F1,text='لتواصل على الواتساب',width=18,fg='black',bg='turquoise3',font=('tajawal',16,'bold'))
title3.place(x=0,y=330)
title3=Button(F1,text='اغـــلاق',width=18,fg='black',bg='turquoise4',font=('tajawal',16,'bold'))
title3.place(x=0,y=375)
photo = PhotoImage(file="C:\\Users\\WN\\Desktop\\na.png")
imo = Label(pro,image=photo)
imo.place(x=-10,y=55,width=580,height=300)
F2=Frame(pro,width=570,height=200,bg="#0B2F3A")
F2.place(x=0,y=350)
user= Label (F2,text='اسم المستخدم',width=16,fg="white",bg="#0B2F3A",font=('tajawal',16,'bold'))
user.place(x=400,y=10)
user= Label (F2,text='كلمة المرور',width=16,fg="white",bg="#0B2F3A",font=('tajawal',16,'bold'))
user.place(x=400,y=50)
photo2=PhotoImage(file="C:\\Users\\WN\\Desktop\\login.png")
imo2=Label(F2,image=photo2)
imo2.place(x=0,y=0,width=100,height=100)
En1=Entry(F2,font=('tajawal',12),justify='center')
En1.place(x=250,y=15)
En2=Entry(F2,font=('tajawal',12,),justify='center')
En2.place(x=250,y=55)
B1=Button(F2,text='تــــسجيــــــل الـــــدخــــول',width=65,fg='black',bg='#DBA901',font=('tajawal',8,'bold'),command=log)
B1.place(x=105,y=80)


pro.mainloop()