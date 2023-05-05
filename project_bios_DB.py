from tkinter import *
import tkinter as tk
import mysql.connector
from PIL import ImageTk

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu")
        self.master.geometry("300x300")

        # Create a label
        self.label = tk.Label(self.master, text="Select an option:")
        self.label.pack()

        # Create a button for adding data
        self.add_button = tk.Button(self.master, text="Customer", command=self.add_data)
        self.add_button.pack()

        # Create a button for displaying data
        self.display_button = tk.Button(self.master, text="log in staff", command=self.log_in_staff)
        self.display_button.pack()

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

        self.login_label = tk.Label(self.login_window, text="USER LOGIN", font=("nr", 30), bg="white", fg="red4")
        self.login_label.place(x=350,y=114)

        self.name_entry = tk.Entry(self.login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold')
                                   , bd=0, fg='red4')
        self.name_entry.place(x=400,y=170)
        self.name_entry.insert(0,"Username")
        self.name_entry.bind('<FocusIn>',self.on_enter)
        self.frame1 = Frame(self.login_window,width=180,height=2,bg='red4').place(x=400,y=190)


        self.psw_entry = tk.Entry(self.login_window, show="*", width=25, font=('Microsoft Yahei UI Light', 11, 'bold')
                                  , bd=0, fg='red4')
        self.psw_entry.place(x=400,y=220)
        self.psw_entry.insert(0,"Password")
        self.psw_entry.bind('<FocusIn>',self.psw_enter)
        self.frame2 = Frame(self.login_window, width=180, height=2, bg='red4').place(x=400, y=240)


        self.submit_button = tk.Button(self.login_window, text="Log In", command=self.submit_data,font=('Open Sans',16,'bold')
                                        ,bg="red4", fg='white',activeforeground='red4')
        self.submit_button.place(x=400,y=280)


    def add_data(self):
        # Create a new window for adding data
        self.login_window = tk.Toplevel(self.master)
        self.login_window.title("Add Data")
        self.login_window.geometry("300x300")

        # Create labels and entries for data input
        self.username_label = tk.Label(self.login_window, text="Name:")
        self.username_label.pack()
        self.name_entry = tk.Entry(self.login_window)
        self.name_entry.pack()

        self.age_label = tk.Label(self.login_window, text="Age:")
        self.age_label.pack()
        self.psw_entry = tk.Entry(self.login_window)
        self.psw_entry.pack()

        # Create a button for adding the data to the database
        self.submit_button = tk.Button(self.login_window, text="Submit", command=self.submit_data)
        self.submit_button.pack()

    def display_data(self):
        # Create a new window for displaying data
        self.display_window = tk.Toplevel(self.master)
        self.display_window.title("Display Data")
        self.display_window.geometry("300x300")

        # Connect to the database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="db_test"
        )

        # Create a cursor
        self.cursor = self.db.cursor()

        # Execute a SELECT statement
        self.cursor.execute("SELECT * FROM persoon")

        # Display the results
        for result in self.cursor:
            self.result_label = tk.Label(self.display_window, text=result)
            self.result_label.pack()

    def submit_data(self):
        # Connect to the database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="db_test"
        )

        # Create a cursor
        self.cursor = self.db.cursor()

        # Get the data from the entries
        name = self.name_entry.get()
        age = self.psw_entry.get()

        # Execute an INSERT statement
        self.cursor.execute("INSERT INTO persoon  VALUES (%s, %s)", (name, age))

        # Commit the changes
        self.db.commit()

        # Close the connection
        self.db.close()

        # Destroy the add window
        self.login_window.destroy()

# Create a Tkinter instance and run the mainloop
root = tk.Tk()
menu = Menu(root)
root.mainloop()

