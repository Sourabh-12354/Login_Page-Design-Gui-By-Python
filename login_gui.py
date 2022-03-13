from tkinter import *
from PIL import Image, ImageTk
import hashlib
import pymysql as mysql
from tkinter import messagebox
window = Tk()
window.geometry("800x500+300+100")
window.minsize(800, 500)
window.maxsize(800, 500)
window.title("SOUHARDO")
window.iconbitmap("C:\Python\login_icons.ico")
image = Image.open("C:\Python\Computer.jpg")
pic = ImageTk.PhotoImage(image)
label0 = Label(image = pic)
label0.pack(fill = BOTH, expand = 'yes')
#global valu
def register_GUI():
    win=Toplevel(window)
    win.geometry("700x500+0+0")
    win.title("Register")
    lebel1=Label(win,text="User_Name:",font=("arial",16,"bold"))
    lebel1.place(x=0,y=10)
    userName=StringVar
    global entry1,entry2,entry3,entry4,entry5,entry6
    entry1=Entry(win, textvar = userName,width = 30, font = ("arial", 16, "bold"),bg="blue")
    entry1.place(x=140,y=10)
    lebel2=Label(win,text="Password:",font=("arial",16,"bold"))
    lebel2.place(x=0,y=50)
    password=StringVar
    entry2=Entry(win, textvar = password,width = 30, font = ("arial", 16, "bold"),bg="blue")
    entry2.place(x=140,y=50)
    lebel3=Label(win,text="Email:",font=("arial",16,"bold"))
    lebel3.place(x=0,y=90)
    email=StringVar
    entry3=Entry(win, textvar = email,width = 30, font = ("arial", 16, "bold"),bg="blue")
    entry3.place(x=140,y=90)
    lebel4=Label(win,text="Gender:",font=("arial",16,"bold"))
    lebel4.place(x=0,y=130)
    gender=StringVar
    entry4=Entry(win, textvar = gender,width = 30, font = ("arial", 16, "bold"),bg="blue")
    entry4.place(x=140,y=130)
    lebel5=Label(win,text="Age:",font=("arial",16,"bold"))
    lebel5.place(x=0,y=170)
    age=StringVar
    entry5=Entry(win, textvar = age,width = 30, font = ("arial", 16, "bold"),bg="blue")
    entry5.place(x=140,y=170)
    lebel6=Label(win,text="Occupation:",font=("arial",16,"bold"))
    lebel6.place(x=0,y=210)
    occupation=StringVar
    entry6=Entry(win, textvar = occupation,width = 30, font = ("arial", 16, "bold"),bg="blue")
    entry6.place(x=140,y=210)

    register1=Button(win,text="Register",bg="blue",relief = "raised",command=register,width=10,font = ("arial", 16, "bold"))
    register1.place(x=230,y=250)
    return
def reset_GUI():
    win=Toplevel(window)
    win.geometry("500x500+0+0")
    win.title("Reset")
    global ent1,ent2
    lebel1=Label(win,text="User_Name:",font=("arial",16,"bold"))
    lebel1.place(x=0,y=10)
    userName=StringVar
    ent1=Entry(win, textvar = userName,width = 20, font = ("arial", 16, "bold"),bg="blue")
    ent1.place(x=140,y=10)
    reset1=Button(win,text="Reset",bg="blue",relief = "raised",command=reset,width=10,font = ("arial", 16, "bold"))
    reset1.place(x=170,y=60)
    return
def pass_change():
    mydb = mysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'login')
    cur = mydb.cursor()
    password=ent3.get()
    has=hash_map(password)
    val=[has,name]
    sql = 'UPDATE user_details SET password = %s WHERE name = %s'
    cur.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("Success","Password has Changed Successfully.")
def new_password_GUI():
    win=Toplevel(window)
    win.geometry("500x500+0+0")
    win.title("New Password")
    lebel1=Label(win,text="New Password:",font=("arial",16,"bold"))
    lebel1.place(x=0,y=10)
    userName=StringVar
    global ent3
    ent3=Entry(win, textvar = userName,width = 20, font = ("arial", 16, "bold"),bg="blue")
    ent3.place(x=160,y=10)
    submit=Button(win,text="Submit",bg="blue",relief = "raised",command=pass_change,width=10,font = ("arial", 16, "bold"))
    submit.place(x=170,y=60)
    return

def hash_map(password):
    hash_object=hashlib.sha256(password.encode())
    hash_dig=hash_object.hexdigest()
    return hash_dig
def login():
    numme=textBox1.get()
    password1=textBox2.get()
    mydb = mysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'login')
    cur = mydb.cursor()
    command = "Select name,password FROM user_details WHERE name=%s"
    results=cur.execute(command,numme)
    data=cur.fetchone()
    if(data==None):
        messagebox.showinfo("Error","User-Name Or Password Icorrect!!")
    else:
        has=hash_map(password1)
        if has==data[1]:
            messagebox.showinfo("Success","Login Succesfully")
            win=Toplevel(window)
            win.geometry("500x500+0+0")
            win.title("login")
            
        else:
            messagebox.showinfo("Error","User-Name Or Password is Icorrect !!")
def register():
            lnth0=len(entry1.get())
            lnth1=len(entry2.get())
            lnth2=len(entry3.get())
            lnth3=len(entry4.get())
            lnth4=len(entry5.get())
            lnth5=len(entry6.get())
            if lnth0==0:
                messagebox.showinfo("Error","User-name Field cann't be empty.")
            elif lnth1==0:
                messagebox.showinfo("Error","Password Field cann't be empty.")
            elif lnth2==0:
                messagebox.showinfo("Error","Email Field cann't be empty.")
            elif lnth3==0:
                messagebox.showinfo("Error","Gender Field cann't be empty.")
            elif lnth4==0:
                messagebox.showinfo("Error","Age Field cann't be empty.")
            elif lnth5==0:
                messagebox.showinfo("Error","Occupation Field cann't be empty.")
            else:
                mydb = mysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'login')
                cur = mydb.cursor()
                userName=entry1.get()
                password=entry2.get()
                command = "Select name FROM user_details WHERE name=%s"
                results=cur.execute(command,userName)
                data=cur.fetchone()
                if data==None:
                    has=hash_map(password)
                    val=[entry1.get(),has,entry3.get(),entry4.get(),entry5.get(),entry6.get()]
                    sql = "Insert INTO user_details(name,password,email,gender,age,occupation)VALUES(%s,%s,%s,%s,%s,%s)"
                    cur.execute(sql,val)
                    mydb.commit()
                    size=cur.rowcount
                    messagebox.showinfo("Success","Register Successfull")
                    cur.close()
                else:
                    messagebox.showinfo("Error","This Name Already Registered!!Use Another Name")
def reset():
    mydb = mysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'login')
    cur = mydb.cursor()
    global name
    name=ent1.get()
    lnth1=len(ent1.get())
    if(lnth1==0):
        messagebox.showinfo("Error","Enter User-Name!!")
    else:
        command = "Select name FROM user_details WHERE name=%s"
        results=cur.execute(command,name)
        data=cur.fetchone()
        if data==None:
            messagebox.showinfo("Error","User-Name is Incorrect")
        elif data!=None:
                new_password_GUI()
label1 = Label(window, text = " Login System ",bg="black" ,fg = "blue", font = ("new times roman", 30, "bold"))
label1.place(x = 350, y = 70)

label2 = Label(window, text = "User Name :", font = ("arial", 16, "bold"),bg="red",width="9")
label2.place(x = 250, y = 200)

userName = StringVar()
textBox1 = Entry(window, textvar = userName,width = 18, font = ("arial", 16, "bold"),bg="blue")
textBox1.place(x = 385, y = 200)
label3 = Label(window, text = "Password :", font = ("arial", 16, "bold"),width="9",bg="red")
label3.place(x = 250, y = 260)

password = StringVar()
textBox2 = Entry(window, textvar = password, width = 18, font = ("arial", 16, "bold"),bg="blue")
textBox2.place(x = 385, y = 260)

button1 = Button(window, text = "   Login   ", fg = "black", bg = "blue", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 280, y = 300)

button2 = Button(window, text = "   Register   ", fg = "black", bg = "Yellow", relief = "raised", font = ("arial", 16, "bold"), command = register_GUI)
button2.place(x = 440, y = 300)

button3 = Button(window, text = "   Reset Password  ", width='15',fg = "black", bg = "red", relief = "raised", font = ("arial", 16, "bold"), command = reset_GUI)
button3.place(x = 330, y = 350)
#display window
window.mainloop()