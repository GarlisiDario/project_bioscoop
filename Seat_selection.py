import tkinter as tk
from tkinter import messagebox
import csv
from CLASS_BIOS import Room

class SeatReservationGUI:
    def __init__(self, seat_rows, seat_columns):
        self.seat_rows = seat_rows
        self.seat_columns = seat_columns
        self.seat_status = [["empty" for _ in range(seat_columns)] for _ in range(seat_rows)]
        self.seats = []
        self.reservations_file = "reservations_final.csv"

        self.seat_gui = tk.Tk()
        self.seat_gui.title("Cinema Seat Reservation")
        self.seat_gui.geometry("800x800")
        self.seat_gui.configure(bg="grey")

        self.seats_frame = tk.Frame(self.seat_gui, bg="gray")
        self.seats_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.header_frame = tk.Frame(self.seat_gui, bg="black", height=50)
        self.header_frame.pack(fill=tk.X)
        self.header_label = tk.Label(self.header_frame, text="Scherm", fg="white", bg="black")
        self.header_label.pack()

        self.checkout_button = tk.Button(self.seat_gui, text="Checkout", command=self.checkout)
        self.checkout_button.pack(side="right", padx=5, pady=10)

        self.back_button = tk.Button(self.seat_gui, text="Terug", command=self.go_back)
        self.back_button.pack(side="left", padx=5, pady=10)

        self.load_reservations()

    def seat_click(self, row, seat):
        if self.seat_status[row][seat] == "empty":
            self.seat_status[row][seat] = "selected"
            self.seats[row][seat].configure(bg="green")
        else:
            self.seat_status[row][seat] = "empty"
            self.seats[row][seat].configure(bg="white")
        self.seat_gui.update()

    def checkout(self):
        selected_seats = []
        for row in range(self.seat_rows):
            for seat in range(self.seat_columns):
                if self.seat_status[row][seat] == "selected":
                    selected_seats.append((row, seat))

        if len(selected_seats) > 0:
            self.show_overview(selected_seats)
        else:
            messagebox.showwarning("No Seats", "You haven't selected any seats.")

    def show_overview(self, selected_seats):
        overview_window = tk.Toplevel(self.seat_gui)
        overview_window.title("Order Overview")
        overview_window.geometry("400x400")

        seat_numbers = ", ".join([f"{chr(65+row)}{column + 1}" for row, column in selected_seats])
        total_price = (len(selected_seats) * 10)

        seats_label = tk.Label(overview_window, text="Selected Seats:")
        seats_label.pack()

        seats_text = tk.Text(overview_window, height=10, width=30)
        seats_text.insert(tk.END, seat_numbers)
        seats_text.config(state="disabled")
        seats_text.pack()

        price_label = tk.Label(overview_window, text="Total Price:")
        price_label.pack()

        price_text = tk.Text(overview_window, height=1, width=10)
        price_text.insert(tk.END, f"€{total_price}")
        price_text.config(state="disabled")
        price_text.pack()

        proceed_button = tk.Button(overview_window, text="Proceed to Payment", command=self.proceed_payment)
        proceed_button.pack()

        pay_counter_button = tk.Button(overview_window, text="Pay at the Counter", command=lambda: self.pay_counter(selected_seats))
        pay_counter_button.pack()

    def proceed_payment(self):
        messagebox.showinfo("Payment", "Payment currently not available. Please select 'Pay at the Counter'.")

    def pay_counter(self, selected_seats):
        for seat in selected_seats:
            row, col = seat
            self.seats[row][col]["bg"] = "red"
            self.seats[row][col]["state"] = "disabled"
        messagebox.showinfo("Reservation", "Reservation Confirmed. Please pay at the counter.")
        self.save_reservation(selected_seats)

    def go_back(self):
        self.seat_gui.quit()

    def load_reservations(self):
        with open(self.reservations_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            reservations = list(reader)

        for reservation in reservations:
            try:
                row = int(reservation[1])
                col = int(reservation[2])
                self.seats[row][col].configure(state="disabled", bg="red")
            except (IndexError, ValueError):
                pass
        return reservations

    def save_reservation(self, selected_seats):
        with open(self.reservations_file, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for seat in selected_seats:
                row, col = seat
                writer.writerow([self.seats[row][col].name, row, col])

    def create_seats(self):
        for row in range(self.seat_rows):
            seat_row = []
            for column in range(self.seat_columns):
                room = Room("Zaal 1", row, column, row, column)
                seat = tk.Button(self.seats_frame, text=f"{chr(65+row)}{column + 1}", bg="white", state="normal")
                seat.name = room.name
                seat.row = room.row
                seat.seat = room.seat
                seat["command"] = lambda btn=seat: self.seat_click(int(btn.row), int(btn.seat))
                seat.grid(row=row, column=column, padx=7, pady=7, ipadx=5, ipady=5)
                seat_row.append(seat)
            self.seats.append(seat_row)

    def run(self):
        self.create_seats()
        self.load_reservations()
        self.seat_gui.grid_rowconfigure(self.seat_rows, weight=1)
        self.seat_gui.grid_columnconfigure(self.seat_columns - 1, weight=1)
        self.seat_gui.mainloop()



if __name__ == "__main__":
    reservation_gui = SeatReservationGUI(10, 10)
    reservation_gui.run()
