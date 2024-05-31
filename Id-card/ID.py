from tkinter import *
from tkinter import filedialog
from pymysql.constants import CLIENT
from PIL import ImageFont,ImageTk, Image,ImageDraw
import pymysql,re,time,yagmail,random,sys,pyautogui,cryptography
tit_font=ImageFont.truetype(r'D:/Id-card/Comfortaa-VariableFont_wght.ttf', 70)
connection = pymysql.connect(host="localhost",user="root",password="Sushu@0803",database="miniproject",client_flag=CLIENT.MULTI_STATEMENTS,autocommit=True)
a=re.compile('[\d]{1}[\w]{2}[\d]{2}[\w]{2}[\d]{3}')
em=re.compile('[\d]{1}[\w]{2}[\d]{2}[\w]{2}[\d]{3}[@bmsit.in]')
tm=re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$")
cur = connection.cursor()
yag = yagmail.SMTP("Tryingout64@gmail.com","raelgzgecldyogle")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
choice=''
no=''
otp=''
usnn=''
f=''
table=''
count=3
usnn1=''
pa=''
bran=''
otpp=''
chance=3
emaill=''
new=''
def goto(sen):
    if sen=='Welcome Student.....':
        starting1()
    elif sen=='Welcome Teacher.....':
        starting2()
    elif sen=='Loading Student Register Page.....':
        registering1()
    elif sen=='Loading Student Login Page.....':
        logging1()
    elif sen=='Loading Teacher Register Page.....':
        registering2()
    elif sen=='Loading Teacher Login Page.....':
        logging2()
    elif sen=='Student Registering.....':
        logging1()
    elif sen=='Teacher Registering.....':
        logging2()
    elif sen=='Student Logging in.....':
        start1(usnn)
    elif sen=='Teacher Logging in.....':
        start2(usnn)
    elif sen=='Enter USN.....':
        forgot("student","#02fac8","reg_student","usn")
    elif sen=='Enter ID.....':
        forgot("teacher",'#f0fc00',"reg_teacher","t_id")
    elif sen=='Student ID card created':
        one()
    elif sen=='Teacher ID card created':
        one()
    elif sen=='Enter OTP sent to mail!':
        valstud()
    elif sen=='Enter OTP sent to your mail!':
        valteach()
#--------------------------------------------------------------------------------------------------------------------------------------
def splash(sen,color):
    root=Tk()
    root.config(bg='black')
    root.overrideredirect(True)
    root.geometry('450x200')
    root.eval('tk::PlaceWindow . center')
    j=0
    l=[]
    fin=''
    for i in sen:
        fin+=i
        l.append(fin)
    def conti():
        global j
        if not j+1>len(l):
            l1.config(text=l[j])
            j+=1
            root.after(30,conti)
        else:
            root.after(1000)
            root.destroy()
            goto(sen)
    l1=Label(root,text='',bg='black',fg=color,font=(tit_font,15))
    l1.pack(ipady=80)
    root.after(300,conti)
    root.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------
def one():
    top = Tk()
    top.title("Welcome")
    top.attributes('-fullscreen', True)
    top.config(bg='black')
    frame1 = Frame(top)
    frame1.place(x=1045,y=260)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/education1.jpeg")).resize((200,200)),master=top)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(top)
    frame2.place(x=1025,y=450)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/teacher.jpeg")).resize((250,250)),master=top)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame3 = Frame(top)
    frame3.place(x=770,y=15)
    img3 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/id card ex.jpeg")).resize((350,280)),master=top)
    label3 = Label(frame3,bg='black', image = img3)
    label3.pack()
    frame4 = Frame(top)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=top)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(top)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=top)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    top.title("WELCOME")
    top.geometry('1200x600')
    l=Label(top,text="I-CARD GENERATION SYSTEM",bg='black',fg='#c3ff00',font=(tit_font,25), anchor='center')
    l.pack()
    def but(x,y,text,fcolor,bcolor,w,h):
        def submit():
            global choice
            choice=text
            if choice == 'Student':
                global j,l,fin
                j=0
                l=[]
                fin=''
                top.destroy()
                top.after(1000,splash('Welcome Student.....','#02cdfa'))
            elif choice == 'Teacher':
                j=0
                l=[]
                fin=''
                top.destroy()
                top.after(1000,splash('Welcome Teacher.....','#ffff80'))
            else:
                j=0
                l=[]
                fin=''
                top.destroy()
                top.after(1000,splash('Thank You!!','red'))
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=w, height =h,activeforeground=bcolor,activebackground=fcolor,command=lambda:submit())
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(725,290,'Student','black','#02fac8',20,4)
    but(725,510,"Teacher",'black','#c3ff00',20,4)
    but(1880,0,"X",'black','red',2,1)
    top.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------
def starting1():
    start = Tk()
    start.attributes('-fullscreen', True)
    start.config(bg='black')
    start.title("WELCOME")
    start.geometry('1200x600')
    frame1 = Frame(start)
    frame1.place(x=630,y=190)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/register3.jpg")).resize((300,200)),master=start)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(start)
    frame2.place(x=625,y=365)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/login3.jpg")).resize((300,200)),master=start)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame3 = Frame(start)
    frame3.place(x=560,y=540)
    img3 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/left arrow.jpg")).resize((400,200)),master=start)
    label3 = Label(frame3,bg='black', image = img3)
    label3.pack()
    frame4 = Frame(start)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=start)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(start)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=start)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    l=Label(start,text="NEW USERS PLEASE REGISTER FIRST!!",bg='black',fg='#c3ff00',font=(tit_font,25), anchor='center')
    l.pack()

    def but(x,y,text,fcolor,bcolor):
        def check():
            if choice=='Register':
                global j,l,fin
                j=0
                l=[]
                fin=''
                start.after(1000,splash('Loading Student Register Page.....','#02cdfa'))
            elif choice=='Login':
                j=0
                l=[]
                fin=''
                start.after(1000,splash('Loading Student Login Page.....','#02cdfa'))
            else:
                start.destroy
                one()
        def submit():
            global choice
            choice=text
            start.destroy()
            check()
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(start,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:submit())
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(920,230,'Register','black','#02fac8')
    but(920,400,'Login','black','#00ffff')
    but(920,570,'Back','black','#02cdfa')
    start.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------    
def starting2():
    start = Tk()
    start.attributes('-fullscreen', True)
    start.config(bg='black')
    start.title("WELCOME")
    start.geometry('1200x600')
    frame1 = Frame(start)
    frame1.place(x=630,y=220)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/register4.jpeg")).resize((250,100)),master=start)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(start)
    frame2.place(x=605,y=365)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/login3.jpg")).resize((300,200)),master=start)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame3 = Frame(start)
    frame3.place(x=560,y=540)
    img3 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/back.jpeg")).resize((370,200)),master=start)
    label3 = Label(frame3,bg='black', image = img3)
    label3.pack()
    frame4 = Frame(start)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=start)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(start)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=start)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    l=Label(start,text="NEW USERS PLEASE REGISTER FIRST!!",bg='black',fg='#40e0d0',font=(tit_font,25), anchor='center')
    l.pack()
    def but(x,y,text,fcolor,bcolor):
        def check():
            if choice=='Register':
                global j,l,fin
                j=0
                l=[]
                fin=''
                start.after(1000,splash('Loading Teacher Register Page.....','#ffff80'))
            elif choice=='Login':
                j=0
                l=[]
                fin=''
                start.after(1000,splash('Loading Teacher Login Page.....','#ffff80'))
            else:
                start.destroy
                one()
        def submit():
            global choice
            choice=text
            start.destroy()
            check()
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(start,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:submit())
        butt.bind('<Enter>',on_enter)   
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(920,230,'Register','black','#c3ff00')
    but(920,400,'Login','black','#f2f261')
    but(920,570,'Back','black','#facd02')
    start.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------
def registering1():
    top = Tk()
    top.config(bg='black')
    top.attributes('-fullscreen', True)
    top.title("Register")
    l1=Label(top,text="USN:",bg='black',fg='#02fac8', font=(tit_font,15), anchor = 'center')
    usn = Entry(top,font=(tit_font,15),width=30)
    l2=Label(top,text="Password: ",bg='black',fg='#02fac8', font=(tit_font,15), anchor = 'center')
    pas = Entry(top,show='*',font=(tit_font,15), width=30)
    l4=Label(top,text=None,bg='black',fg='red', font=(tit_font,15), anchor = 'center') 
    l=Label(top,text="REGISTER HERE!!",bg='black',fg='#c3ff00',font=(tit_font,25), anchor='center')
    l.pack()
    frame1 = Frame(top)
    frame1.place(x=680,y=260)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/reg.jpeg")).resize((170,170)),master=top)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(top)
    frame2.place(x=680,y=420)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/login4.jpg")).resize((170,170)),master=top)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame3 = Frame(top)
    frame3.place(x=600,y=595)
    img3 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/back.jpeg")).resize((300,170)),master=top)
    label3 = Label(frame3,bg='black', image = img3)
    label3.pack()
    frame4 = Frame(top)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=top)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(top)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=top)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    def but(x,y,text,fcolor,bcolor,cmd):
        global val
        val=cmd
        def submit():
            usn_val = usn.get()
            pass_val = pas.get()
            email_val = usn_val+'@bmsit.in'
            if re.findall(a,usn_val)==[]:
                l4.config(text="Enter USN properly")
                l4.place(x=930,y=230)
            elif len(pass_val)<8:
                l4.config(text="Minimum password length is 8")
                l4.place(x=860,y=230)
            else:
                global new,emaill
                emaill=email_val
                new=(usn_val.upper(),email_val,pass_val)
                try:
                    global j,l,fin,otpp
                    j=0
                    l=[]
                    fin=''
                    otpp=random.randint(1000,9999)
                    if cur.execute("select * from reg_student where usn={}".format("\"{}\"".format(usn_val.upper())))!=0:
                         l4.config(text="Account already exists")
                         l4.place(x=910,y=230)
                    else:
                        yag.send(email_val,"Authenticate",str(otpp)+" is your otp for creating account")
                        top.destroy()
                        top.after(3000,splash('Enter OTP sent to mail!','#02cdfa'))
                except:
                    l4.config(text="Check if your USN exists")
                    l4.place(x=900,y=230)
        def nothing(val):
            if val=='submit':
                submit()
            elif val=='log':
                top.destroy()
                global j,l,fin
                j=0
                l=[]
                fin=''
                top.after(1000,splash('Loading Student Login Page.....','#02cdfa'))
            else:
                top.destroy()
                starting1()
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:nothing(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(880,280,'Register','black','#02fac8','submit')
    but(880,450,'Login','black','#00ffff','log')
    but(880,620,'Back','black','#02cdfa','back')
    l1.place(x=620,y=100)
    usn.place(x=820,y=100)
    l2.place(x=620,y=150)
    pas.place(x=820,y=150)
    top.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------
def valstud():
    top=Tk()
    top.attributes('-fullscreen',True)
    top.config(bg='black')
    top.title("Confirming")
    l1 = Label(top,text="Enter OTP:",bg='black',fg='#02fac8', font=(tit_font,15), anchor = 'center')
    values = Entry(top,font=(tit_font,15),width=30)
    l6=Label(top,text=None,bg='black',fg='red',font=(tit_font,15),anchor='center')
    l=Label(top,text="ENTER OTP SENT TO YOUR MAIL!!",bg='black',fg='#c3ff00',font=(tit_font,25), anchor='center')
    l.pack()
    frame1 = Frame(top)
    frame1.place(x=670,y=260)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/submit.jpg")).resize((200,180)),master=top)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(top)
    frame2.place(x=600,y=465)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/back.jpeg")).resize((300,170)),master=top)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame4 = Frame(top)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=top)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(top)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=top)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    global chance
    chance=3
    def checks(some):
        val_val = values.get()
        if some=='submit':
            if val_val==str(otpp):
                cur.execute("insert into reg_student(usn,email,password) values {}".format(new))
                top.destroy()
                global j,l,fin
                j=0
                l=[]
                fin=''
                top.after(1000,splash('Student Registering.....','#02cdfa'))
            else:
                global chance
                if chance>0:
                    l6.config(text="{} more chances left".format(chance))
                    chance-=1
                else:
                    top.destroy()
                    starting1()
        else:
            top.destroy()
            registering1()
    def but(x,y,text,fcolor,bcolor,cmd):
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:checks(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(880,290,"Submit",'black','#02fac8','submit')
    but(880,490,"Back",'black','#00ffff','back')
    l1.place(x=620,y=150)
    values.place(x=820,y=150)
    l6.place(x=920,y=240)
    top.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------
def registering2():
    top = Tk()
    top.config(bg='black')
    top.attributes('-fullscreen',True)
    top.title("Register")
    l1=Label(top,text="ID:",bg='black',fg='#c3ff00',font=(tit_font,15), anchor = 'center')
    usn = Entry(top,font=(tit_font,15),width=30)
    l2=Label(top,text="Password: ",bg='black',fg='#c3ff00', font=(tit_font,15), anchor = 'center')
    pas = Entry(top,font=(tit_font,15),show='*', width=30)
    l3=Label(top,text="Email-id: ",bg='black',fg='#c3ff00', font=(tit_font,15), anchor = 'center')
    email = Entry(top,font=(tit_font,15), width=30)
    l4=Label(top,text=None,bg='black',fg='red', font=(tit_font,15), anchor = 'center')
    l=Label(top,text="REGISTER HERE!!",bg='black',fg='#40e0d0',font=(tit_font,25), anchor='center')
    l.pack()
    frame1 = Frame(top)
    frame1.place(x=680,y=290)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/reg.jpeg")).resize((170,170)),master=top)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(top)
    frame2.place(x=680,y=455)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/login5.jpg")).resize((170,170)),master=top)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame3 = Frame(top)
    frame3.place(x=600,y=625)
    img3 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/back.jpeg")).resize((300,170)),master=top)
    label3 = Label(frame3,bg='black', image = img3)
    label3.pack()
    frame4 = Frame(top)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=top)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(top)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=top)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    def but(x,y,text,fcolor,bcolor,cmd):
        def submit():
            usn_val = usn.get()
            pass_val = pas.get()
            email_val = email.get()
            if usn_val=='':
                l4.config(text="Enter ID properly")
                l4.place(x=930,y=260)
            elif len(pass_val)<8:
                l4.config(text="Minimum password length is 8")
                l4.place(x=860,y=260)
            elif re.findall(tm,email_val)==[]:
                l4.config(text="Enter valid email-id")
                l4.place(x=925,y=260)
            else:
                global new,emaill
                emaill=email_val
                new=(usn_val.upper(),email_val,pass_val)
                try:
                    global j,l,fin,otpp
                    j=0
                    l=[]
                    fin=''
                    otpp=random.randint(1000,9999)
                    if cur.execute("select * from reg_teacher where t_id={}".format("\"{}\"".format(usn_val.upper())))!=0:
                         l4.config(text="Account already exists")
                         l4.place(x=900,y=260)
                    else:
                        yag.send(email_val,"Authenticate",str(otpp)+" is your otp for creating account")
                        top.destroy()
                        top.after(3000,splash('Enter OTP sent to your mail!','#ffff80'))
                except:
                    l4.config(text="Check if your ID exists")
                    l4.place(x=905,y=260)
        def nothing(val):
            if val=='submit':
                submit()
            elif val=='log':
                top.destroy()
                global j,l,fin
                j=0
                l=[]
                fin=''
                top.after(1000,splash('Loading Teacher Login Page.....','#ffff80'))
            else:
                top.destroy()
                starting2()
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:nothing(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(880,310,'Register','black','#c3ff00','submit')
    but(880,480,'Login','black','#f2f261','log')
    but(880,650,'Back','black','#facd02','back')
    l1.place(x=620,y=100)
    usn.place(x=820,y=100)
    l2.place(x=620,y=150)
    pas.place(x=820,y=150)
    l3.place(x=620,y=200)
    email.place(x=820,y=200)
    top.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------
def valteach():
    top=Tk()
    top.attributes('-fullscreen',True)
    top.config(bg='black')
    top.title("Confirming")
    l1 = Label(top,text="Enter OTP:",bg='black',fg='#c3ff00', font=(tit_font,15), anchor = 'center')
    values = Entry(top,font=(tit_font,15),width=30)
    l6=Label(top,text=None,bg='black',fg='red',font=(tit_font,15),anchor='center')
    l=Label(top,text="ENTER OTP SENT TO YOUR MAIL!!",bg='black',fg='#40e0d0',font=(tit_font,25), anchor='center')
    l.pack()
    frame1 = Frame(top)
    frame1.place(x=670,y=260)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/submit.jpg")).resize((200,180)),master=top)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(top)
    frame2.place(x=600,y=465)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/back.jpeg")).resize((300,170)),master=top)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame4 = Frame(top)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=top)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(top)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=top)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    global chance
    chance=3
    def checks(some):
        val_val = values.get()
        if some=='submit':
            if val_val==str(otpp):
                cur.execute("insert into reg_teacher(t_id,email,password) values {}".format(new))
                top.destroy()
                global j,l,fin
                j=0
                l=[]
                fin=''
                top.after(1000,splash('Teacher Registering.....','#ffff80'))
            else:
                global chance
                if chance>0:
                    l6.config(text="{} more chances left".format(chance))
                    chance-=1
                else:
                    top.destroy()
                    starting2()
        else:
            top.destroy()
            registering2()
    def but(x,y,text,fcolor,bcolor,cmd):
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:checks(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(880,290,"Submit",'black','#f0fc00','submit')
    but(880,490,"Back",'black','#facd02','back')
    l1.place(x=620,y=150)
    values.place(x=820,y=150)
    l6.place(x=920,y=240)
    top.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------
def logging1():
    log = Tk()
    log.config(bg='black')
    log.attributes('-fullscreen', True)
    log.title("Login Here")
    l=Label(log,text="LOG IN HERE!!",bg='black',fg='#c3ff00',font=(tit_font,25), anchor='center')
    l.pack()
    l1=Label(log,text="USN:", bg='black',fg='#00ffea',font=(tit_font,15), anchor = 'center')
    l1.place(x=620,y=100)
    usn = Entry(log,font=(tit_font,15),width=30)
    usn.place(x=820,y=100)
    l2=Label(log,text="Password: ",bg='black',fg='#00ffea',font=(tit_font,15), anchor = 'center')
    l2.place(x=620,y=160)
    pas = Entry(log,show='*',font=(tit_font,15),width=30)
    pas.place(x=820,y=160)
    l3=Label(log,text=None,bg='black',fg='red', font=(tit_font,15), anchor = 'center')
    frame1 = Frame(log)
    frame1.place(x=680,y=290)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/login6.jpg")).resize((170,170)),master=log)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(log)
    frame2.place(x=625,y=460)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/fpass.jpg")).resize((280,150)),master=log)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame3 = Frame(log)
    frame3.place(x=600,y=615)
    img3 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/back.jpeg")).resize((300,170)),master=log)
    label3 = Label(frame3,bg='black', image = img3)
    label3.pack()
    frame4 = Frame(log)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=log)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(log)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=log)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    def forg():
        global j,l,fin
        j=0
        l=[]
        fin=''
        log.after(1000,splash('Enter USN.....','#02cdfa'))
    def something():
        usn_val = usn.get()
        pass_val = pas.get()
        new=(usn_val.upper(),pass_val)
        global usnn
        usnn=usn_val.upper()
        try:
            cur.execute("select password from reg_student where usn={};".format("\"{}\"".format(usn_val)))
            a=cur.fetchall()
            if a[0][0]==pass_val:
                log.destroy()
                global j,l,fin
                j=0
                l=[]
                fin=''
                log.after(1000,splash('Student Logging in.....','#02cdfa'))
            else:
                l3.config(text="Enter password correctly")
                l3.place(x=895,y=250)
        except:
            l3.config(text='Enter valid credentials')
            l3.place(x=905,y=250)
    def another(val):
        if val=='submit':
            something()
        elif val=='forg':
            log.destroy()
            forg()
        else:
            log.destroy()
            starting1()
    def but(x,y,text,fcolor,bcolor,cmd):
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(log,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:another(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(880,300,'Login','black','#02fac8','submit')
    but(880,470,'Forgot Password','black','#00ffff','forg')
    but(880,640,'Back','black','#02cdfa','back')
    log.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------
def logging2():
    log = Tk()
    log.config(bg='black')
    log.attributes('-fullscreen', True)
    log.title("Login Here")
    l=Label(log,text="LOG IN HERE!!",bg='black',fg='#40e0d0',font=(tit_font,25), anchor='center')
    l1=Label(log,text="ID:",bg='black',fg='#c3ff00', font=(tit_font,15), anchor = 'center')
    usn = Entry(log, font=(tit_font,15),width=30)
    l2=Label(log,text="Password: ",bg='black',fg='#c3ff00', font=(tit_font,15), anchor = 'center')
    pas = Entry(log, font=(tit_font,15),show='*', width=30)
    l3=Label(log,text=None,bg='black',fg='red', font=(tit_font,15), anchor = 'center')
    frame1 = Frame(log)
    frame1.place(x=680,y=280)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/login7.jpg")).resize((170,170)),master=log)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(log)
    frame2.place(x=625,y=460)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/fpass.jpg")).resize((280,150)),master=log)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame3 = Frame(log)
    frame3.place(x=600,y=615)
    img3 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/back.jpeg")).resize((300,170)),master=log)
    label3 = Label(frame3,bg='black', image = img3)
    label3.pack()
    frame4 = Frame(log)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=log)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(log)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=log)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    def forg():
        global j,l,fin
        j=0
        l=[]
        fin=''
        log.after(1000,splash('Enter ID.....','#ffff80'))
    def something():
        usn_val = usn.get()
        pass_val = pas.get()
        new=(usn_val.upper(),pass_val)
        global usnn
        usnn=usn_val.upper()
        try:
            cur.execute("select password from reg_teacher where t_id={};".format("\"{}\"".format(usn_val)))
            a=cur.fetchall()
            if a[0][0]==pass_val:
                l3.config(text="Successfully logged in")
                log.destroy()
                global j,l,fin
                j=0
                l=[]
                fin=''
                log.after(1000,splash('Teacher Logging in.....','#ffff80'))
            else:
                l3.config(text="Enter password correctly")
                l3.place(x=892,y=250)
        except:
            l3.config(text='Enter valid credentials')
            l3.place(x=910,y=250)
    def another(val):
            if val=='submit':
                something()
            elif val=='forg':
                log.destroy()
                forg()
            else:
                log.destroy()
                starting2()
    def but(x,y,text,fcolor,bcolor,cmd):
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(log,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:another(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(880,300,'Login','black','#c3ff00','submit')
    but(880,470,'Forgot Password','black','#f2f261','forg')
    but(880,640,'Back','black','#facd02','back')
    l.pack()
    l1.place(x=620,y=100)
    usn.place(x=820,y=100)
    l2.place(x=620,y=160)
    pas.place(x=820,y=160)
    log.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------
def start1(value):
    global no
    no=value
    top = Tk()
    top.config(bg='black')
    top.attributes('-fullscreen',True)
    k=''
    l=Label(top,text="ENTER YOUR DETAILS!!",bg='black',fg='#c3ff00',font=(tit_font,25), anchor='center')
    l.pack()
    l6=Label(top,text=None,bg='black',fg='red', font=(tit_font,15), anchor = 'center')
    frame1 = Frame(top)
    frame1.place(x=670,y=380)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/submit.jpg")).resize((200,180)),master=top)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(top)
    frame2.place(x=600,y=580)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/back.jpeg")).resize((300,170)),master=top)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame4 = Frame(top)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=top)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(top)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=top)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    def but(x,y,text,fcolor,bcolor,cmd):
        def chec(val):
            if val=='submit':
                submit()
            else:
                top.destroy()
                logging1()
        def submit():
            name_val = name.get()
            sem_val = sem.get()
            branch_val = branch.get()
            phone_val = Phone.get()
            cur.execute("select email from reg_student where usn={}".format("\"{}\"".format(no)))
            some=cur.fetchall()
            email_val = some[0][0]
            new=(no.upper(),name_val,sem_val,branch_val.upper(),phone_val,email_val)
            if name_val=='':
                l6.config(text='Please enter the Name')
                l6.place(x=900,y=350)
            elif branch_val=='':
                l6.config(text='Please enter the Branch')
                l6.place(x=895,y=350)
            elif phone_val=='' or len(phone_val)<10 or len(phone_val)>10:
                l6.config(text='Phone number must be 10 digits')
                l6.place(x=850,y=350)
            elif sem_val=='' or sem_val not in '12345678':
                if sem_val!='' and sem_val not in '12345678':
                    l6.config(text='Enter a valid Semester')
                    l6.place(x=905,y=350)
                elif sem_val=='':
                    l6.config(text='Please enter your Semester')
                    l6.place(x=875,y=350)
            else:
                try:
                    if branch_val=='CSE' or branch_val=='ISE' or branch_val=='ECE' or branch_val=='EEE' or branch_val=='MECH' or branch_val=='AIML' or branch_val=='CIVIL' or branch_val=='ETE':
                        cur.execute("insert into info_student(usn, name,sem, branch, phone, email) values {}".format(new))
                        try:
                            top.filename = filedialog.askopenfilename(initialdir=r'D:/Id-card/student pictures',title='select your photo',filetypes=(("jpg files","*.jpg"),("png files","*.png"),("jpeg files","*.jpeg")))
                            card(name_val,no.upper(),branch_val,phone_val,'student',top.filename,'usn')
                            top.destroy()
                            global j,l,fin
                            j=0
                            l=[]
                            fin=''
                            try:
                                top.after(1000,splash('Student ID card created','#02cdfa'))
                            except:
                                pass
                        except:
                            l6.config(text="Check if your photo exists")
                            l6.place(x=890,y=350)
                    else:
                        l6.config(text="Enter a valid branch")
                        l6.place(x=920,y=350)        
                except:
                    try:
                        cur.execute("update info_student set name={}, branch={}, phone={}, email={} where usn={}".format("\"{}\"".format(name_val),"\"{}\"".format(branch_val),"\"{}\"".format(phone_val),"\"{}\"".format(email_val),"\"{}\"".format(no)))
                        try:
                            top.filename = filedialog.askopenfilename(initialdir=r'D:/Id-card/student pictures',title='select your photo',filetypes=(("jpg files","*.jpg"),("png files","*.png"),("jpeg files","*.jpeg")))
                            card(name_val,no.upper(),branch_val,phone_val,'student',top.filename,'usn')
                            top.destroy()
                            j=0
                            l=[]
                            fin=''
                            try:
                                top.after(1000,splash('Student ID card created','#02cdfa'))
                            except:
                                pass
                        except:
                            l6.config(text="Check if your photo exists")
                            l6.place(x=890,y=350)
                    except:
                        l6.config(text="Enter a valid branch")
                        l6.place(x=920,y=350)
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:chec(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    top.title("Id card Generator")
    l1=Label(top,text="Name:",bg='black',fg='#66ffd9',font=(tit_font,15), anchor = 'center')
    name=Entry(top, font=(tit_font,15), width=30)
    l3=Label(top,text="Branch: ",bg='black',fg='#66ffd9', font=(tit_font,15), anchor = 'center')
    branch = Entry(top,font=(tit_font,15), width=30)
    l4=Label(top,text="Phone no: ",bg='black',fg='#66ffd9', font=(tit_font,15), anchor = 'center')
    Phone = Entry(top, font=(tit_font,15), width=30)
    l5=Label(top,text="Sem: ",bg='black',fg='#66ffd9', font=(tit_font,15), anchor = 'center')
    sem = Entry(top,font=(tit_font,15), width=30)
    but(880,400,'Submit','black','#66ffd9','submit')
    but(880,600,'Back','black','#00ffff','back')
    l1.place(x=620,y=100)
    name.place(x=820,y=100)
    l3.place(x=620,y=150)
    branch.place(x=820,y=150)
    l4.place(x=620,y=200)
    Phone.place(x=820,y=200)
    l5.place(x=620,y=250)
    sem.place(x=820,y=250)
    top.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------
def start2(value):
    global no
    no=value
    top = Tk()
    top.config(bg='black')
    top.attributes('-fullscreen',True)
    k=''
    l=Label(top,text="ENTER YOUR DETAILS!!",bg='black',fg='#40e0d0',font=(tit_font,25), anchor='center')
    l.pack()
    l6=Label(top,text=None,bg='black',fg='red', font=(tit_font,15), anchor = 'center')
    frame1 = Frame(top)
    frame1.place(x=670,y=380)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/submit.jpg")).resize((200,180)),master=top)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(top)
    frame2.place(x=600,y=580)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/back.jpeg")).resize((300,170)),master=top)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame4 = Frame(top)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=top)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(top)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=top)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    def but(x,y,text,fcolor,bcolor,cmd):
        def chec(val):
            if val=='submit':
                submit()
            else:
                top.destroy()
                logging2()
        def submit():
            name_val = name.get()
            branch_val = branch.get()
            phone_val = Phone.get()
            cur.execute("select email from reg_teacher where t_id={}".format("\"{}\"".format(no)))
            some=cur.fetchall()
            email_val = some[0][0]
            new=(no.upper(),name_val,branch_val,phone_val,email_val)
            if name_val=='':
                l6.config(text='Please enter the Name')
                l6.place(x=900,y=350)
            elif branch_val=='':
                l6.config(text='Please enter the Branch')
                l6.place(x=895,y=350)
            elif phone_val=='' or len(phone_val)<10 or len(phone_val)>10:
                l6.config(text='Phone number must be 10 digits')
                l6.place(x=850,y=350)
            else:
                try:
                    if branch_val=='CSE' or branch_val=='ISE' or branch_val=='ECE' or branch_val=='EEE' or branch_val=='MECH' or branch_val=='AIML' or branch_val=='CIVIL' or branch_val=='ETE':
                        cur.execute("insert into info_teacher(id, name, branch, phone, email) values {}".format(new))
                        try:
                            top.filename = filedialog.askopenfilename(initialdir=r'D:/Id-card/teacher pictures',title='select your photo',filetypes=(("jpg files","*.jpg"),("png files","*.png"),("jpeg files","*.jpeg")))
                            card(name_val,no.upper(),branch_val,phone_val,'teacher',top.filename,'t_id')
                            top.destroy()
                            global j,l,fin
                            j=0
                            l=[]
                            fin=''
                            try:
                                top.after(1000,splash('Teacher ID card created','#ffff80'))
                            except:
                                pass
                        except:
                            l6.config(text="Check if your photo exists")
                            l6.place(x=890,y=350)
                    else:
                        l6.config(text="Enter a valid branch")
                        l6.place(x=920,y=350)        
                except:
                    try:
                        cur.execute("update info_teacher set name={}, branch={}, phone={}, email={} where id={}".format("\"{}\"".format(name_val),"\"{}\"".format(branch_val),"\"{}\"".format(phone_val),"\"{}\"".format(email_val),"\"{}\"".format(no)))
                        try:
                            top.filename = filedialog.askopenfilename(initialdir=r'D:/Id-card/teacher pictures',title='select your photo',filetypes=(("jpg files","*.jpg"),("png files","*.png"),("jpeg files","*.jpeg")))
                            card(name_val,no.upper(),branch_val,phone_val,'teacher',top.filename,'t_id')
                            top.destroy()
                            j=0
                            l=[]
                            fin=''
                            try:
                                top.after(1000,splash('Teacher ID card created','#ffff80'))
                            except:
                                pass
                        except:
                            l6.config(text="Check if your photo exists")
                            l6.place(x=890,y=350)
                    except:
                        l6.config(text="Enter a valid branch")
                        l6.place(x=920,y=350)

        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:chec(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    top.title("Id card Generator")
    l1=Label(top,text="Name:",bg='black',fg='#c3ff00',font=(tit_font,15), anchor = 'center')
    name=Entry(top, font=(tit_font,15), width=30)
    l3=Label(top,text="Branch: ",bg='black',fg='#c3ff00', font=(tit_font,15), anchor = 'center')
    branch = Entry(top,font=(tit_font,15), width=30)
    l4=Label(top,text="Phone no: ",bg='black',fg='#c3ff00', font=(tit_font,15), anchor = 'center')
    Phone = Entry(top, font=(tit_font,15), width=30)
    but(880,400,'Submit','black','#c3ff00','submit')
    but(880,600,'Back','black','#facd02','back')
    l1.place(x=620,y=100)
    name.place(x=820,y=100)
    l3.place(x=620,y=150)
    branch.place(x=820,y=150)
    l4.place(x=620,y=200)
    Phone.place(x=820,y=200)
    top.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------
def forgot(cho,fg,an,some):
    def checks(val):
        if val=='submit':
            submit()
        else:
            if cho=='student':
                top.destroy()
                logging1()
            else:
                top.destroy()
                logging2()
    def submit():
        def new():
            def changepass():
                def setting():
                    pas_val = pas.get()
                    if len(pas_val)>=8:
                        cur.execute("update {} set password={} where {}={};".format(table,"\"{}\"".format(pas_val),some,"\"{}\"".format(usnn)))
                        top.destroy()
                        if choice=="student":
                            logging1()
                        else:
                            logging2()
                    else:
                        l2.config(text='Enter a 8 digit password')
                top=Tk()
                top.title("Changing Password")
                top.attributes('-fullscreen',True)
                top.config(bg='black')
                l=Label(top,text="ENTER YOUR NEW PASSWORD!!",bg='black',fg='violet',font=(tit_font,25), anchor='center')
                l.pack()
                l1 = Label(top,text="Enter new Password:",bg='black',fg=f, font=(tit_font,15), anchor = 'center')
                pas = Entry(top,font=(tit_font,15),width=30)
                l2 = Label(top,text=None,bg='black',fg='red', font=(tit_font,15), anchor = 'center')
                frame1 = Frame(top)
                frame1.place(x=680,y=380)
                img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/setp.jpeg")).resize((170,170)),master=top)
                label1 = Label(frame1,bg='black', image = img1)
                label1.pack()
                frame4 = Frame(top)
                frame4.place(x=0,y=200)
                img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=top)
                label4 = Label(frame4,bg='black', image = img4)
                label4.pack()
                frame5 = Frame(top)
                frame5.place(x=1320,y=200)
                img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=top)
                label5 = Label(frame5,bg='black', image = img5)
                label5.pack()
                def but(x,y,text,fcolor,bcolor):
                    def on_enter(e):
                        butt['background']=fcolor
                        butt['foreground']=bcolor
                    def on_leave(e):
                        butt['background']=bcolor
                        butt['foreground']=fcolor
                    butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:setting())
                    butt.bind('<Enter>',on_enter)
                    butt.bind('<Leave>',on_leave)
                    butt.place(x=x,y=y)
                but(880,390,"Set Password",'black',f)
                l1.place(x=530,y=170)
                pas.place(x=820,y=170)
                l2.place(x=895,y=340)
                top.mainloop()
            def confirming():
                otp_val = otpp.get()
                if otp_val==str(otp):
                    top.destroy()
                    changepass()
                else:
                    global count
                    if count>0:                        
                        l2.config(text='Wrong OTP, More {} chance left'.format(count))
                        count-=1
                    else:
                        if an=='reg_student':
                            top.destroy()
                            logging1()
                        else:
                            top.destroy()
                            logging2()
            global count
            count=3
            top=Tk()
            top.title("Entering OTP")
            top.attributes('-fullscreen',True)
            top.config(bg='black')
            l=Label(top,text="ENTER OTP SENT TO YOUR MAIL!!",bg='black',fg='violet',font=(tit_font,25), anchor='center')
            l.pack()
            l1 = Label(top,text="OTP:",bg='black',fg=f, font=(tit_font,15), anchor = 'center')
            otpp = Entry(top,font=(tit_font,15),width=30)
            l2 = Label(top,text=None,bg='black',fg='red', font=(tit_font,15), anchor = 'center')
            l2.place(x=855,y=340)
            frame1 = Frame(top)
            frame1.place(x=658,y=360)
            img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/confirm.jpg")).resize((200,200)),master=top)
            label1 = Label(frame1,bg='black', image = img1)
            label1.pack()
            frame4 = Frame(top)
            frame4.place(x=0,y=200)
            img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=top)
            label4 = Label(frame4,bg='black', image = img4)
            label4.pack()
            frame5 = Frame(top)
            frame5.place(x=1320,y=200)
            img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=top)
            label5 = Label(frame5,bg='black', image = img5)
            label5.pack()
            def but(x,y,text,fcolor,bcolor):
                def on_enter(e):
                    butt['background']=fcolor
                    butt['foreground']=bcolor
                def on_leave(e):
                    butt['background']=bcolor
                    butt['foreground']=fcolor
                butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:confirming())
                butt.bind('<Enter>',on_enter)
                butt.bind('<Leave>',on_leave)
                butt.place(x=x,y=y)
            but(880,390,"Confirm",'black',f)
            l1.place(x=680,y=180)
            otpp.place(x=820,y=180)
            top.mainloop()
        global otp
        global usnn
        otp=random.randint(1000,10000)
        x=usn.get()
        usnn=x.upper()
        try:
            cur.execute("select email from {} where {}={};".format(table,some,"\"{}\"".format(x)))
            m=cur.fetchall()
            yag.send(m[0][0],"Reset Password",str(otp)+" is your otp for new password")
            top.destroy()
            new()
        except:
            l6.config(text='Check if your account exists!')
            l6.place(x=870,y=230)
    global choice,f,table
    choice=cho
    f=fg
    table=an
    top=Tk()
    top.attributes('-fullscreen',True)
    top.config(bg='black')
    top.title("Forgot password")
    l=Label(top,text="ENTER YOUR UNIQUE NUMBER!!",bg='black',fg='violet',font=(tit_font,25), anchor='center')
    l.pack()
    l1 = Label(top,text="{}:".format(some.upper()),bg='black',fg=f, font=(tit_font,15), anchor = 'center')
    usn = Entry(top,font=(tit_font,15),width=30)
    l6=Label(top,text=None,bg='black',fg='red',font=(tit_font,15),anchor='center')
    frame1 = Frame(top)
    frame1.place(x=670,y=240)
    img1 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/send2.jpg")).resize((200,200)),master=top)
    label1 = Label(frame1,bg='black', image = img1)
    label1.pack()
    frame2 = Frame(top)
    frame2.place(x=610,y=460)
    img2 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/back.jpeg")).resize((300,170)),master=top)
    label2 = Label(frame2,bg='black', image = img2)
    label2.pack()
    frame4 = Frame(top)
    frame4.place(x=0,y=200)
    img4 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg3.jpg")).resize((600,540)),master=top)
    label4 = Label(frame4,bg='black', image = img4)
    label4.pack()
    frame5 = Frame(top)
    frame5.place(x=1320,y=200)
    img5 = ImageTk.PhotoImage((Image.open(r"D:/Id-card/bg4.jpg")).resize((600,540)),master=top)
    label5 = Label(frame5,bg='black', image = img5)
    label5.pack()
    def but(x,y,text,fcolor,bcolor,cmd):
        def on_enter(e):
            butt['background']=fcolor
            butt['foreground']=bcolor
        def on_leave(e):
            butt['background']=bcolor
            butt['foreground']=fcolor
        butt = Button(top,text=text,fg=fcolor,bg=bcolor,font=(tit_font,15),width=20, height =4,activeforeground=bcolor,activebackground=fcolor,command=lambda:checks(cmd))
        butt.bind('<Enter>',on_enter)
        butt.bind('<Leave>',on_leave)
        butt.place(x=x,y=y)
    but(880,280,"SEND",'black',f,'submit')
    but(880,480,"Back",'black',f,'back')
    l1.place(x=680,y=150)
    usn.place(x=820,y=150)
    top.mainloop()
def card(name,usn,branch,phone,part,vals,last):
    global usnn1,pa,bran
    usnn1=usn
    pa=part
    bran=branch
    print(1)
    img=Image.open(r"D:/Id-card/{}_template.png".format(part))
    img_edit = ImageDraw.Draw(img)
    img_edit.text((550,1165), name,font=tit_font,fill=0)
    img_edit.text((550,1338), usn,font=tit_font,fill=0)
    img_edit.text((550,1505), branch,font=tit_font,fill=0)
    img_edit.text((550,1675), phone,font=tit_font,fill=0)
    print(2)
    img.save(r'''D:/Id-card/id cards/{}/{}.png'''.format(pa,usnn1))
    print(3)
    img1 = Image.open(r'''D:/Id-card/id cards/{}/{}.png'''.format(pa,usnn1))
    img1copy = img1.copy()
    print(5)
    print(vals)
    img2 = Image.open(r"{}".format(vals))
    print(6)
    photo=img2.copy()
    photo=photo.resize((600,600))
    img1copy.paste(photo,(500,450))
    img3 = Image.open(r"D:/Id-card/qr_code.jpeg")
    img3=img3.resize((400,400))
    img1copy.paste(img3,(600,1800))
    print(8)
    img1copy.save(r"D:/Id-card/id cards/{}/{}.png".format(pa,usnn1))
    print(pa)
    print(last)
    print(usnn1)
    cur.execute("select email from reg_{} where {} = {};".format(pa,last,'\'{}\''.format(usnn1)))
    emaill = cur.fetchall()[0][0]
    print(6)
    yag.send(emaill,"ID card!!",attachments=r"D:/Id-card/id cards/{}/{}.png".format(pa,usnn1))
one()