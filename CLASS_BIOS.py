class Customers:
    def __init__(self, customer_id, phone, email, name, family_name, age):
        self.customer_id = customer_id
        self.phone = phone
        self.email = email
        self.name = name
        self.family_name = family_name
        self.age = age


class Staff:
    def __init__(self, staff_id, phone, age, name, family_name, email, card_nr):
        self.staff_id = staff_id
        self.phone = phone
        self.age = age
        self.name = name
        self.family_name = family_name
        self.email = email
        self.card_nr = card_nr


class Room:
    def __init__(self, room_id, name, seat_place, row, seat):
        self.room_id = room_id
        self.name = name
        self.seat_place = seat_place
        self.row = row
        self.seat = seat




class Tickets:
    def __init__(self, ticket_id, room_id, customer_id, movie_id, movie_name, price):
        self.ticket_id = ticket_id
        self.room_id = room_id
        self.customer_id = customer_id
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.price = price


class Movies:
    def __init__(self, movie_id, movie_name, actors, movie_time, movie_date):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.actors = actors
        self.movie_time = movie_time
        self.movie_date = movie_date


class Calendar:
    def __init__(self, calendar_id, movie_id, date, movie_name):
        self.calendar_id = calendar_id
        self.movie_id = movie_id
        self.date = date
        self.movie_name = movie_name
