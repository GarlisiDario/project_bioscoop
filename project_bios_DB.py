import mysql.connector
from tkinter import ttk
import tkinter as tk

db = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd ="root",
    database ="bioscoop"

)
def toon_menu():
    print("1:new persoon toevoegen")


def new_person():
    first_name = input("Geef u naam in:")
    last_name = input("Geef u achternaam in:")
    phone = input("Geef u telefoonnummer in:")
    email = input("Geef u email in:")
    cursor = db.cursor()
    sql = "INSERT INTO customer (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)"
    val = (first_name, last_name, phone, email)
    cursor.execute(sql, val)
    print("record toegevoegd.")
    db.commit()
###################################
#hoofdprogramma
##############################
keuze = ""
toon_menu()
while not keuze == "stop":
    keuze = input("wat wil je doen?")
    if keuze == "1":
        new_person()
        toon_menu()
        keuze = input("wat wil je doen?")
