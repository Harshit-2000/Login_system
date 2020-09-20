import tkinter 
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'login_db'
)

mycursor = connection.cursor()

root = Tk()
root.geometry('702x502')
root.maxsize(702,502)
root.title("login system")
root.iconbitmap('Images/Icon.ico')

frame1 = Frame(root)
frame1.pack( fill= BOTH, expand = 1)

# setting background image
def background_img():
    load = Image.open('images/scaled-python.jpeg')
    filename = ImageTk.PhotoImage(load)
    background_label = Label(frame1, image = filename)
    background_label.place(x = 0 , y = 0 , relwidth = 1 , relheight = 1)
    background_label.image = filename

background_img()

def back_button(func):
    back_image = PhotoImage(file='images/back.png')
    back_button = Button(frame1, image = back_image,  bd=0, command=func)
    back_button.image = back_image
    back_button.place(x = 40, y = 30)

def login():
    for i in frame1.winfo_children():
        i.destroy()
    background_img()

    # setting image on top
    load1 = Image.open('images/form-wizard-login.jpg')
    file = ImageTk.PhotoImage(load1)
    login_label = Label(frame1, image=file)
    login_label.grid(row = 0, column = 0)
    login_label.image = file

    # back button
    back_button(create_account)

    def log():
        sql = "SELECT username, pass FROM users WHERE username = %s"
        user = (username.get(),)
        mycursor.execute(sql,user)
        result = mycursor.fetchall()
        print(result)

        try:
            if result[0][1] == password.get():
                login_successfull_label = Label(frame1, text = ('Welcome', user), bg = "#7ee68e")
                login_successfull_label.grid(row=3,column = 0, ipadx = 32)
            else:
                invalid_pass_label = Label(frame1, text = ("Invalid Password"), bg = "#c93247").grid(row=3,column = 0, ipadx = 30)

        except:
            error_label = Label(frame1, text=("Invalid Username"), bg="#c93247").grid(row=3, column=0, ipadx=30)

    username = StringVar()
    username_entry = Entry(frame1, bd = 0, textvariable = username)
    username_entry.grid(row=0, column=0, padx=490, pady=(200, 20), ipadx = 31, ipady = 4)


    password = StringVar()
    password_entry = Entry(frame1, bd = 0, textvariable = password, show = '*')
    password_entry.grid(row=1, column=0, padx=490, pady=(0, 40), ipadx=30, ipady=4)


    login_image = PhotoImage(file='images/button.png')
    login_button = Button(frame1, image = login_image,  bd=0, command=log)
    login_button.image = login_image
    login_button.grid(row=2, column=0, padx=490, pady=(0, 40))


def create_account():
    for i in frame1.winfo_children():
        i.destroy()
    background_img()

    # setting image on top
    load1 = Image.open('images/images.jpg')
    file = ImageTk.PhotoImage(load1)
    login_label = Label(frame1, image=file)
    login_label.grid(row = 0, column = 0)
    login_label.image = file

    back_button(login)
    def create():
        try:
            sql = "INSERT INTO users (username, pass) VALUES (%s, %s)"
            val = (username.get(), password.get())
            mycursor.execute(sql,val)
            user_created_label = Label(frame1, text = (mycursor.rowcount, "user added."), bg = "#7ee68e").grid(row=3,column = 0)
            connection.commit()
        except:
            error_label = Label(frame1, text=("** Username already exists **"), bg="#c93247").grid(row=3, column=0, ipadx=30)

        username_entry.delete(0,END)
        password_entry.delete(0,END)


    username = StringVar()
    username_entry = Entry(frame1, bd = 0, textvariable = username)
    username_entry.grid(row=0, column=0, padx=490, pady=(200, 20), ipadx = 30, ipady = 4)


    password = StringVar()
    password_entry = Entry(frame1, bd = 0, textvariable = password, show = '*')
    password_entry.grid(row=1, column=0, padx=490, pady=(0, 30), ipadx=30, ipady=4)


    create_image = PhotoImage(file='images/create_button.png')
    create_button = Button(frame1, image = create_image,  bd=0, command=create)
    create_button.image = create_image
    create_button.grid(row=2, column=0, padx=490, pady=(0, 40))



login_image = PhotoImage(file = 'images/button.png')
login_button = Button(frame1, image = login_image,bd = 0, command=login)
login_button.grid(row = 0, column = 0, padx=490, pady= (180,40))

create_image = PhotoImage(file = 'images/create_button.png')
create_button = Button(frame1, image = create_image,bd = 0, command=create_account)
create_button.grid(row = 1, column = 0)



root.mainloop()