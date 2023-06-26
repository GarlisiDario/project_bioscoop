from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk


class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("log in")
        self.menu = Menu(self)
        self.create_login_button()

    def create_login_button(self):
        login_button = Button(self, text="Log In", command=self.log_in_staff)
        login_button.pack()

    def on_enter(self, event):
        if self.name_entry.get() == "Username":
            self.name_entry.delete(0, tk.END)

    def psw_enter(self, event):
        if self.psw_entry.get() == "Password":
            self.psw_entry.delete(0, tk.END)

    def log_in_staff(self):
        self.login_window = tk.Toplevel(self, bg="red4")
        self.login_window.title("Log In")
        self.login_window.geometry("960x660+50+50")

        # Background image
        self.bgImage = ImageTk.PhotoImage(file="bg.jpg")
        self.bglabel = tk.Label(self.login_window, image=self.bgImage)
        self.bglabel.place(x=0, y=0)

        # Login label
        self.login_label = tk.Label(self.login_window, text="STAFF LOGIN", font=("nr", 30), bg="white", fg="red4")
        self.login_label.place(x=350, y=114)

        # Username label + entry
        self.name_entry = tk.Entry(self.login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                                   bd=0, fg='red4')
        self.name_entry.place(x=400, y=170)
        self.name_entry.insert(0, "Username")
        self.name_entry.bind('<FocusIn>', self.on_enter)
        self.frame1 = Frame(self.login_window, width=180, height=2, bg='red4').place(x=400, y=190)

        # Password entry + label
        self.psw_entry = tk.Entry(self.login_window, show="*", width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                                  bd=0, fg='red4')
        self.psw_entry.place(x=400, y=220)
        self.psw_entry.insert(0, "Password")
        self.psw_entry.bind('<FocusIn>', self.psw_enter)
        self.frame2 = Frame(self.login_window, width=180, height=2, bg='red4').place(x=400, y=240)

        # Button to confirm login
        self.submit_button = tk.Button(self.login_window, text="Log In", command=self.login_user,
                                       font=('Open Sans', 16, 'bold'), bg="red4", fg='white',
                                       activeforeground='red4')
        self.submit_button.place(x=500, y=280)

        # Button to go back to the main menu
        self.back_button = tk.Button(self.login_window, text="Back", command=self.back_to_main_menu,
                                     font=('Open Sans', 16, 'bold'), bg="red4", fg='white',
                                     activeforeground='red4')
        self.back_button.place(x=400, y=280)

    def login_user(self):
        if self.name_entry.get() == "" or self.psw_entry.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                self.db = mysql.connector.connect(host='localhost', user='root', password='root')
                self.mycursor = self.db.cursor()
            except:
                messagebox.showerror("Error", "Connection is not established. Please try again.")
                return

            query = 'use db_test'
            self.mycursor.execute(query)
            query = 'select * from log_in where username=%s and password=%s'
            self.mycursor.execute(query, (self.name_entry.get(), self.psw_entry.get()))
            row = self.mycursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                messagebox.showinfo("Welcome", "Login successful")

    def back_to_main_menu(self):
        self.login_window.destroy()


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
