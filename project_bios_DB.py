from PIL import Image, ImageTk
from PIL import *
from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import messagebox

import crud
from films import FilmsApp
from crud import *



class Menu():
    def back_button(self):
        self.master.destroy()
        root = tk.Tk()
        menu = Menu(root)
        root.mainloop()


    def button1_click(self):
        self.master.destroy()
        app = FilmsApp()
        app.mainloop()
    def button2_click(self):
        self.master.destroy()
        root = Tk()
        app = Window(root)
        root.wm_title("Tkinter window")
        root.mainloop()
    def __init__(self,master):
        self.master = master
        self.master.title("Menu")
        self.master.geometry("600x304")

        self.bgImage = ImageTk.PhotoImage(file="start.jpg")
        self.bglabel = tk.Label(self.master, image=self.bgImage)
        self.bglabel.place(x=0, y=0)


        # Create a label
        self.label = tk.Label(self.master, text="Select an option:",bd=0,fg="white",bg="red4"
                              ,font=('Microsoft Yahei UI Light', 15, 'bold'))
        self.label.place(x=75,y=65)

        # Create a button for adding data
        self.customer_button = tk.Button(self.master, text="Customer", command=self.button1_click
                                       , font=('Open Sans', 16, 'bold'), bg="red4", fg='white', activeforeground='red4')
        self.customer_button.place(x=100,y=100)

        # Create a button for displaying data
        self.staff_button = tk.Button(self.master, text="Login Staff", command=self.log_in_staff
                                         , font=('Open Sans', 16, 'bold'), bg="red4", fg='white',
                                         activeforeground='red4')
        self.staff_button.place(x=100,y=150)

    def on_enter(self,event):
        if self.name_entry.get() =="Username":
            self.name_entry.delete(0,END)


    def psw_enter(self,event):
        if self.psw_entry.get() =="Password":
            self.psw_entry.delete(0,END)



    def log_in_staff(self):



        self.login_window = tk.Toplevel(self.master, bg="red4")
        self.login_window.title("log in")
        self.login_window.geometry("960x660+50+50")

        #background images aanmaken
        self.bgImage = ImageTk.PhotoImage(file="bg.jpg")
        self.bglabel = tk.Label(self.login_window, image=self.bgImage)
        self.bglabel.place(x=0,y=0)

        #login label
        self.login_label = tk.Label(self.login_window, text="STAFF LOGIN", font=("nr", 30), bg="white", fg="red4")
        self.login_label.place(x=350,y=114)

        #username label + entry
        self.name_entry = tk.Entry(self.login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold')
                                   , bd=0, fg='red4')
        self.name_entry.place(x=400,y=170)
        self.name_entry.insert(0,"Username")
        self.name_entry.bind('<FocusIn>',self.on_enter)
        self.frame1 = Frame(self.login_window,width=180,height=2,bg='red4').place(x=400,y=190)

        #password entry + label
        self.psw_entry = tk.Entry(self.login_window, show="*", width=25, font=('Microsoft Yahei UI Light', 11, 'bold')
                                  , bd=0, fg='red4')
        self.psw_entry.place(x=400,y=220)
        self.psw_entry.insert(0,"Password")
        self.psw_entry.bind('<FocusIn>',self.psw_enter)
        self.frame2 = Frame(self.login_window, width=180, height=2, bg='red4').place(x=400, y=240)

        # button confirm your ready
        self.submit_button = tk.Button(self.login_window, text="Log In", command=self.login_user
                                       ,font=('Open Sans',16,'bold'),bg="red4", fg='white',activeforeground='red4')
        self.submit_button.place(x=500,y=280)

        #button for going back to mainmenu

        self.back_button= tk.Button(self.login_window,text="Back",command=self.back_button,
                                    font=('Open Sans',16,'bold'),bg="red4", fg='white',activeforeground='red4')
        self.back_button.place(x=400,y=280)

    def login_user(self):

        if self.name_entry.get() =="" or self.psw_entry.get()=="":
            messagebox.showerror("Error","All Field Are Reguired")

        else:
            try:
                self.db = mysql.connector.connect(host='localhost',
                                                  user='root',
                                                  password='root')
                self.mycursor = self.db.cursor()
            except:
                messagebox.showerror("Error","Connection is not established try again")
                return
            query = 'use db_test'
            self.mycursor.execute(query)
            query = 'select * from log_in where username=%s and password=%s'
            self.mycursor.execute(query,(self.name_entry.get(),self.psw_entry.get()))
            row = self.mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error","invalid username or password")
            else:
                messagebox.showinfo("Welcome","Login is Sucessful")
                self.button2_click()














# Create a Tkinter instance and run the mainloop
if __name__ == "__main__":
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()

