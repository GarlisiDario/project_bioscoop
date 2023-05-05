import mysql.connector
from tkinter import ttk
import tkinter as tk

class MainScreen:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="bioscoop"
        )

        self.my_w = tk.Tk()
        self.my_w.geometry("400x280")
        self.my_w.title("Home Log In Bios")

        self.create_menu()




    def create_menu(self):
        menu_bar = tk.Menu(self.my_w)

        #maak hier de menu aan.
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Gebruiker/Klant",command= self.add_movies)
        file_menu.add_command(label="Personeel",command= self.add_seats)
        file_menu.add_command(label="Quit", command= self.quit)
        menu_bar.add_cascade(label="Menu", menu=file_menu)

        self.my_w.config(menu=menu_bar)

    def add_movies(self):
        pass

    def add_employee(selfs):
        pass

    def add_seats(self):
        pass

    def add_zaal(self):
        pass

    def quit(self):
        self.my_w.quit()

    def run(self):
        self.my_w.mainloop()

if __name__ == "__main__":
    app = MainScreen()
    app.run()

