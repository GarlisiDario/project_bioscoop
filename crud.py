import mysql.connector
from tkinter import *
from tkinter import messagebox

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Menu for employees
        employeeMenu = Menu(menu)
        employeeMenu.add_command(label="Add employee", command=self.add_employee)
        employeeMenu.add_command(label="Delete employee", command=self.delete_employee)
        employeeMenu.add_command(label="Update employee", command=self.update_employee)
        menu.add_cascade(label="Employees", menu=employeeMenu)

        # Menu for rooms
        roomMenu = Menu(menu)
        roomMenu.add_command(label="Add room", command=self.add_room)
        roomMenu.add_command(label="Delete room", command=self.delete_room)
        roomMenu.add_command(label="Update room", command=self.update_room)
        menu.add_cascade(label="Rooms", menu=roomMenu)

        # Menu for customers
        customerMenu = Menu(menu)
        customerMenu.add_command(label="Add customer", command=self.add_customer)
        customerMenu.add_command(label="Delete customer", command=self.delete_customer)
        customerMenu.add_command(label="Update customer", command=self.update_customer)
        menu.add_cascade(label="Customers", menu=customerMenu)

        # Menu for movies
        movieMenu = Menu(menu)
        movieMenu.add_command(label="Add movie", command=self.add_movie)
        movieMenu.add_command(label="Delete movie", command=self.delete_movie)
        movieMenu.add_command(label="Update movie", command=self.update_movie)
        menu.add_cascade(label="Movies", menu=movieMenu)

        # Menu for exit
        menu.add_command(label="Exit", command=self.exit_program)

        self.master.config(menu=menu)

        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="db_test"
        )
        self.db_cursor = self.db_connection.cursor()

    def exit_program(self):
        self.db_cursor.close()
        self.db_connection.close()
        self.master.destroy()

    def execute_query(self, query, values=None):
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

    def add_employee(self):
        employee_name = input("Enter employee name: ")
        employee_position = input("Enter employee position: ")

        query = "INSERT INTO employees (name, position) VALUES (%s, %s)"
        values = (employee_name, employee_position)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Employee added successfully.")

    def delete_employee(self):
        employee_id = input("Enter employee ID to delete: ")

        query = "DELETE FROM employees WHERE id = %s"
        values = (employee_id,)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Employee deleted successfully.")

    def update_employee(self):
        employee_id = input("Enter employee ID to update: ")
        new_name = input("Enter new name for the employee: ")
        new_position = input("Enter new position for the employee: ")

        query = "UPDATE employees SET name = %s, position = %s WHERE id = %s"
        values = (new_name, new_position, employee_id)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Employee updated successfully.")

    def add_room(self):
        room_number = input("Enter room number: ")
        room_type = input("Enter room type: ")
        room_capacity = input("Enter room capacity: ")

        query = "INSERT INTO rooms (room_number, room_type, room_capacity) VALUES (%s, %s, %s)"
        values = (room_number, room_type, room_capacity)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Room added successfully.")

    def delete_room(self):
        room_id = input("Enter room ID to delete: ")

        query = "DELETE FROM rooms WHERE id = %s"
        values = (room_id,)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Room deleted successfully.")

    def update_room(self):
        room_id = input("Enter room ID to update: ")
        new_room_number = input("Enter new room number: ")
        new_room_type = input("Enter new room type: ")
        new_room_capacity = input("Enter new room capacity: ")

        query = "UPDATE rooms SET room_number = %s, room_type = %s, room_capacity = %s WHERE id = %s"
        values = (new_room_number, new_room_type, new_room_capacity, room_id)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Room updated successfully.")

    def add_customer(self):
        customer_name = input("Enter customer name: ")
        customer_email = input("Enter customer email: ")
        customer_phone = input("Enter customer phone number: ")

        query = "INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)"
        values = (customer_name, customer_email, customer_phone)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Customer added successfully.")

    def delete_customer(self):
        customer_id = input("Enter customer ID to delete: ")

        query = "DELETE FROM customers WHERE id = %s"
        values = (customer_id,)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Customer deleted successfully.")

    def update_customer(self):
        customer_id = input("Enter customer ID to update: ")
        new_name = input("Enter new name for the customer: ")
        new_email = input("Enter new email for the customer: ")
        new_phone = input("Enter new phone number for the customer: ")

        query = "UPDATE customers SET name = %s, email = %s, phone = %s WHERE id = %s"
        values = (new_name, new_email, new_phone, customer_id)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Customer updated successfully.")

    def add_movie(self):
        movie_title = input("Enter movie title: ")
        movie_genre = input("Enter movie genre: ")
        movie_release_date = input("Enter movie release date: ")

        query = "INSERT INTO movies (title, genre, release_date) VALUES (%s, %s, %s)"
        values = (movie_title, movie_genre, movie_release_date)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Movie added successfully.")

    def delete_movie(self):
        movie_id = input("Enter movie ID to delete: ")

        query = "DELETE FROM movies WHERE id = %s"
        values = (movie_id,)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Movie deleted successfully.")

    def update_movie(self):
        movie_id = input("Enter movie ID to update: ")
        new_title = input("Enter new title for the movie: ")
        new_genre = input("Enter new genre for the movie: ")
        new_release_date = input("Enter new release date for the movie: ")

        query = "UPDATE movies SET title = %s, genre = %s, release_date = %s WHERE id = %s"
        values = (new_title, new_genre, new_release_date, movie_id)
        self.execute_query(query, values)

        messagebox.showinfo("Success", "Movie updated successfully.")

    def execute_query(self, query, values=None):
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

    def exitProgram(self):
        self.db_connection.close()
        exit()
if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.wm_title("Tkinter window")
    root.mainloop()
