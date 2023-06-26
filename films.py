from PIL import Image, ImageTk
from datetime import datetime
import pytz
from tkinter import Label, StringVar, OptionMenu, Spinbox, Button

import Seat_selection
from Seat_selection import *


class FilmsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Movies")
        self.geometry("990x660+50+50")
        self.resizable(False, False)
        self.config(bg="#FF914D")

        self.create_widgets()

    def create_widgets(self):
        # Achtergrond
        self.bg2Image = tk.PhotoImage(file="afbeeldingen/main_achtergrond.png")
        self.bg2Label = tk.Label(self, image=self.bg2Image)
        self.bg2Label.place(x=0, y=0)

        # Titel
        label = tk.Label(self, text="|Current film offer in the cinema|", background="#FFBD59",
                         foreground="#fcffff", font=("Arial", 32, "bold"))
        label.place(x=160, y=75)

        # Films
        film1Image = Image.open("afbeeldingen/film1.png")  # Opent het beeldbestand "afbeeldingen/film1.png"
        resized_film1Image = film1Image.resize((179, 254))  # Verkleint de afbeelding
        self.film1Photo = ImageTk.PhotoImage(resized_film1Image)  # Maakt een PhotoImage-object van de verkleinde afbeelding
        film1Label = tk.Label(self, image=self.film1Photo)  # Maakt een Label-widget met de afbeelding
        film1Label.config(borderwidth=0)  # Stelt de randbreedte van het label in op 0
        film1Label.place(x=165, y=180)  # Plaatst het label op de gewenste positie

        film2Image = Image.open("afbeeldingen/film2.png")
        resized_film2Image = film2Image.resize((179, 254))
        self.film2Photo = ImageTk.PhotoImage(resized_film2Image)
        film2Label = tk.Label(self, image=self.film2Photo)
        film2Label.config(borderwidth=0)
        film2Label.place(x=410, y=180)

        film3Image = Image.open("afbeeldingen/film3.png")
        resized_film3Image = film3Image.resize((179, 254))
        self.film3Photo = ImageTk.PhotoImage(resized_film3Image)
        film3Label = tk.Label(self, image=self.film3Photo)
        film3Label.config(borderwidth=0)
        film3Label.place(x=650, y=180)

        # Filmtekst
        label = tk.Label(self, text="The little mermaid", background="#FFBD59", foreground="#fcffff",
                         font=("Arial", 12, "bold"))
        label.place(x=185, y=440)

        label = tk.Label(self, text="Guardians of the galaxy vol. 3", background="#FFBD59", foreground="#fcffff",
                         font=("Arial", 12, "bold"))
        label.place(x=385, y=440)

        label = tk.Label(self, text="Fast X", background="#FFBD59", foreground="#fcffff",
                         font=("Arial", 12, "bold"))
        label.place(x=710, y=440)

        # Buttons
        button_style = {
            "font": ("Arial", 14),
            "bg": "#FF914D",
            "fg": "black",
            "relief": tk.RAISED, # Style van de button
            "bd": 3, # Border width
            "width": 10,
            "height": 2,
        }

        button1 = tk.Button(self, text="Info", command=self.button1_click, **button_style)
        button1.place(x=255, y=520, anchor=tk.CENTER)

        button2 = tk.Button(self, text="Info", command=self.button2_click, **button_style)
        button2.place(x=495, y=520, anchor=tk.CENTER)

        button3 = tk.Button(self, text="Info", command=self.button3_click, **button_style)
        button3.place(x=740, y=520, anchor=tk.CENTER)

    def button1_click(self):
        self.destroy()
        app = Films1App()
        app.mainloop()

    def button2_click(self):
        self.destroy()
        app = Films2App()
        app.mainloop()

    def button3_click(self):
        self.destroy()
        app = Films3App()
        app.mainloop()


class Films1App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Little Mermaid")
        self.geometry("990x660+50+50")
        self.resizable(False, False)
        self.config(bg="#00368c")

        self.create_widgets()

    def create_widgets(self):
        # Achtergrond
        self.bgImage = tk.PhotoImage(file="afbeeldingen/film_achtergrond1.png")
        self.bgLabel = tk.Label(self, image=self.bgImage)
        self.bgLabel.place(x=0, y=0)

        # Titel
        label = tk.Label(self, text="The Little Mermaid", background="#4942E4", foreground="#fcffff",
                         font=("Arial", 25, "bold"))
        label.place(x=110, y=95)

        # Afbeelding film
        film1Image = Image.open("afbeeldingen/film1.png")  # Opent het beeldbestand "afbeeldingen/film1.png"
        resized_film1Image = film1Image.resize((200, 300))  # Verkleint de afbeelding
        self.film1Photo = ImageTk.PhotoImage(resized_film1Image)  # Maakt een PhotoImage-object van de verkleinde afbeelding
        film1Label = tk.Label(self, image=self.film1Photo)  # Maakt een Label-widget met de afbeelding
        film1Label.config(borderwidth=0)  # Stelt de randbreedte van het label in op 0
        film1Label.place(x=150, y=160)  # Plaatst het label op de gewenste positie

        # Tekst
        label = tk.Label(self, text="Duration: 135 Minutes", background="#4942E4", foreground="#fcffff",
                         font=("Arial", 15, "bold"))
        label.place(x=145, y=480)

        label = tk.Label(self, text="Director: Rob Marshall", background="#4942E4", foreground="#fcffff",
                         font=("Arial", 15, "bold"))
        label.place(x=145, y=530)

        label = tk.Label(self, text="Description:\n\nA young mermaid makes a deal\nwith a sea witch to trade her beautiful voice for\nhuman legs so she can discover the world\nabove water and impress a prince.",
                         background="#4942E4", foreground="#fcffff", font=("Arial", 15, "bold"))
        label.place(x=410, y=150)

        label = tk.Label(self, text="Cast:\n\nHalle Bailey, Jonah Hauer-King,\nMelissa McCarthy, Javier Bardem,\nNoma Dumezweni",
                         background="#4942E4", foreground="#fcffff", font=("Arial", 15, "bold"))
        label.place(x=470, y=325)

        # Button
        button_style = {
            "font": ("Arial", 14),
            "bg": "#00368c",
            "fg": "#fcffff",
            "relief": tk.RAISED, # Style van de button
            "bd": 3, # Border width
            "width": 15,
            "height": 2,
        }

        button = tk.Button(self, text="Reserveren", command=self.button, **button_style)
        button.place(x=635, y=525, anchor=tk.CENTER)
    def button(self):
        Films1App.destroy(self)
        FilmsReservationApp()
class Films2App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Guardians of the galaxy vol. 3")
        self.geometry("990x660+50+50")
        self.resizable(False, False)
        self.config(bg="#00368c")

        self.create_widgets()

    def create_widgets(self):
        # Achtergrond
        self.bgImage = tk.PhotoImage(file="afbeeldingen/film_achtergrond2.png")
        self.bgLabel = tk.Label(self, image=self.bgImage)
        self.bgLabel.place(x=0, y=0)

        # Titel
        label = tk.Label(self, text="Guardians of the galaxy vol. 3", background="#E7B0F8", foreground="#fcffff",
                         font=("Arial", 22, "bold"))
        label.place(x=80, y=100)

        # Afbeelding film
        film1Image = Image.open("afbeeldingen/film2.png")  # Opent het beeldbestand "afbeeldingen/film2.png"
        resized_film1Image = film1Image.resize((200, 300))  # Verkleint de afbeelding
        self.film1Photo = ImageTk.PhotoImage(resized_film1Image)  # Maakt een PhotoImage-object van de verkleinde afbeelding
        film1Label = tk.Label(self, image=self.film1Photo)  # Maakt een Label-widget met de afbeelding
        film1Label.config(borderwidth=0)  # Stelt de randbreedte van het label in op 0
        film1Label.place(x=150, y=160)  # Plaatst het label op de gewenste positie

        # Tekst
        label = tk.Label(self, text="Duration: 150 Minutes", background="#E7B0F8", foreground="#fcffff",
                         font=("Arial", 15, "bold"))
        label.place(x=145, y=480)

        label = tk.Label(self, text="Director: James Gunn", background="#E7B0F8", foreground="#fcffff",
                         font=("Arial", 15, "bold"))
        label.place(x=145, y=530)

        label = tk.Label(self,
                         text="Description:\n\n Still reeling from the loss of Gamora,\n Peter Quill rallies his team to defend\n the universe and one of their own.\n a mission that could mean the end of\n the Guardians if not successful.",
                         background="#E7B0F8", foreground="#fcffff", font=("Arial", 15, "bold"))
        label.place(x=460, y=150)

        label = tk.Label(self, text="Cast:\n\n Chris Pratt, Zoë Saldana, Will Poulter,\n Dace Bautista,Vin Diesel, Pom Klementieff",
                         background="#E7B0F8", foreground="#fcffff", font=("Arial", 15, "bold"))
        label.place(x=440, y=340)

        # Button
        button_style = {
            "font": ("Arial", 14),
            "bg": "#800080",
            "fg": "#fcffff",
            "relief": tk.RAISED, # Style van de button
            "bd": 3, # Border width
            "width": 15,
            "height": 2,
        }

        def button():
            Films2App.destroy(self)
            FilmsReservationApp()

        button = tk.Button(self, text="Reserveren", command=button, **button_style)
        button.place(x=645, y=525, anchor=tk.CENTER)

class Films3App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fast X")
        self.geometry("990x660+50+50")
        self.resizable(False, False)
        self.config(bg="#BC1823")

        self.create_widgets()

    def create_widgets(self):
        # Achtergrond
        self.bgImage = Image.open("afbeeldingen/film_achtergrond3.png")
        self.bgPhoto = ImageTk.PhotoImage(self.bgImage)
        self.bgLabel = tk.Label(self, image=self.bgPhoto)
        self.bgLabel.place(x=0, y=0)

        # Titel
        label = tk.Label(self, text="Fast X", background="#2E2C2B", foreground="#fcffff",
                         font=("Ariel", 22, "bold"))
        label.place(x=200, y=100)

        # Afbeelding film
        filmImage = Image.open("afbeeldingen/film3.png")  # Opent het beeldbestand "afbeeldingen/film3.png"
        resizedFilmImage = filmImage.resize((200, 300))  # Verkleint de afbeelding
        self.filmPhoto = ImageTk.PhotoImage(resizedFilmImage)  # Maakt een PhotoImage-object van de verkleinde afbeelding
        filmLabel = tk.Label(self, image=self.filmPhoto)  # Maakt een Label-widget met de afbeelding
        filmLabel.config(borderwidth=0)  # Stelt de randbreedte van het label in op 0
        filmLabel.place(x=150, y=160)  # Plaatst het label op de gewenste positie

        # Tekst
        label = tk.Label(self, text="Duration: 141 Minutes", background="#2E2C2B", foreground="#fcffff",
                         font=("Ariel", 15, "bold"))
        label.place(x=145, y=480)

        label = tk.Label(self, text="Director: Louis Leterrier", background="#2E2C2B", foreground="#fcffff",
                         font=("Ariel", 15, "bold"))
        label.place(x=145, y=530)

        label = tk.Label(self, text="Description:\n\nDom Toretto and his family\nare targeted by Dante Reyes,\nwho seeks revenge for his father's death\nand loss of his family's fortune.",
                         background="#2E2C2B", foreground="#fcffff", font=("Ariel", 15, "bold"))
        label.place(x=460, y=150)

        label = tk.Label(self, text="Cast:\n\nVin Diesel, Jason Statham, Michelle Rodrigues,\nLudacris, Jason Momoa, Brie Larson",
                         background="#2E2C2B", foreground="#fcffff", font=("Ariel", 15, "bold"))
        label.place(x=430, y=340)

        # Button
        button_style = {
            "font": ("Arial", 14),
            "bg": "#BC1823",
            "fg": "#fcffff",
            "relief": tk.RAISED, # Style van de button
            "bd": 3, # Border width
            "width": 15,
            "height": 2,
        }

        def button():
            Films3App.destroy(self)
            FilmsReservationApp()

        self.button = tk.Button(self, text="Reserveren", command=button, **button_style)
        self.button.place(x=655, y=525, anchor=tk.CENTER)

class FilmsReservationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reservation")
        self.geometry("990x660+50+50")
        self.resizable(False, False)
        self.config(bg="#ED5EAB")

        self.create_widgets()

    def create_widgets(self):
        # Achtergrond
        self.bgImage = tk.PhotoImage(file="afbeeldingen/reserveren_achtergrond.png")
        self.bgLabel = tk.Label(self, image=self.bgImage)
        self.bgLabel.place(x=0, y=0)

        # Titel
        label = tk.Label(self, text="|Reserve|", background="#FFAEE2", foreground="#fcffff", font=("Ariel", 32, "bold"))
        label.place(x=390, y=75)

        # Film_keuzes
        dropdown_label = Label(self, text="Movies", font=("Ariel", 15, "bold"), bg="#FFAEE2", fg="#fcffff")
        dropdown_label.place(x=440, y=165)

        choices = ["The little mermaid", "Guardians of the galaxy vol. 3", "Fast X"]
        self.selected_option = StringVar()
        self.selected_option.set(choices[0])

        dropdown = OptionMenu(self, self.selected_option, *choices)
        dropdown.config(width=25, highlightbackground="#FFAEE2")
        dropdown.place(x=385, y=200)

        # Aanwezigen
        attendees_label = Label(self, text="Number of People", font=("Ariel", 15, "bold"), bg="#FFAEE2", fg="#fcffff")
        attendees_label.place(x=395, y=270)

        self.selected_attendees = StringVar()
        self.selected_attendees.set("1")

        attendees_spinbox = Spinbox(self, textvariable=self.selected_attendees, from_=1, to=10, font=("Arial", 12), width=5)
        attendees_spinbox.place(x=450, y=310)

        # Tijd keuze
        time_label = Label(self, text="Time Selection", font=("Arial", 15, "bold"), bg="#FFAEE2", fg="#fcffff")
        time_label.place(x=410, y=360)

        self.selected_time = tk.StringVar()

        amsterdam_tz = pytz.timezone("Europe/Amsterdam") # Hier word de actuele tijd van amsterdam gehaald
        current_time = datetime.now(amsterdam_tz).time()

        time1 = datetime.strptime("10:06", "%H:%M").time() # Hier word gekeken welke tijd beschikbaar is om te laten zien
        time2 = datetime.strptime("12:06", "%H:%M").time() # Hier word gekeken welke tijd beschikbaar is om te laten zien
        time3 = datetime.strptime("20:06", "%H:%M").time() # Hier word gekeken welke tijd beschikbaar is om te laten zien
        time4 = datetime.strptime("22:06", "%H:%M").time() # Hier word gekeken welke tijd beschikbaar is om te laten zien

        time_choices = []
        if current_time <= time1:
            time_choices.append("10:00")
        if current_time <= time2:
            time_choices.append("12:00")
        if current_time <= time3:
            time_choices.append("20:00")
        if current_time <= time4:
            time_choices.append("22:00")

        if time_choices:
            self.selected_time.set(time_choices[0]) # Hier kiest je de eerst tijd die beschikbaar is
            time_dropdown = OptionMenu(self, self.selected_time, *time_choices) # Hier maakt die de dropdown
        else:
            self.selected_time.set("No available time") # Hier geeft die aan dat er geen tijd beschikbaar is
            time_dropdown = OptionMenu(self, self.selected_time, "No available time") # Hier maakt die een dropdown met "geen beschikbare tijd"
            time_dropdown.configure(state='disabled') # Hier schakelt die de dropdown uit

        time_dropdown.config(width=25, highlightbackground="#FFAEE2")
        time_dropdown.place(x=385, y=395)

        # Zitplekken_button
        def validate_attendees_input():
            value = self.selected_attendees.get()

            if not value.isdigit():
                return "Please enter a valid number."

            if int(value) < 1 or int(value) > 10:
                return "Number of attendees should be between 1 and 10."

            return None

        def reserve_seats():
            selected_time = self.selected_time.get()
            attendees_error = validate_attendees_input()

            if selected_time == "No available time":
                messagebox.showinfo("Error", "No time available. Please come back later.")
            elif attendees_error:
                messagebox.showinfo("Error", attendees_error)
                self.selected_attendees.set("1") #om de box te resetten naar 1
            else:
                self.destroy()
                reservation_gui = SeatReservationGUI(10, 10)
                reservation_gui.run()


        seats_button = Button(self, text="Reserve Seats", font=("Arial", 20, "bold"), bg="#ED5EAB", fg="#fcffff", command=reserve_seats)
        seats_button.place(x=378, y=500)



if __name__ == "__main__":
    app = FilmsApp()
    app.mainloop()