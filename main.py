from datetime import datetime
from decimal import Decimal


class Ticket:
    def __init__(self, id, departure_zone, arrival_zone, route_number, departure_time, arrival_time, buyer_id, is_used,
                 price, place):
        self.id = id
        self.departure_zone = departure_zone
        self.arrival_zone = arrival_zone
        self.route_number = route_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.buyer_id = buyer_id
        self.is_used = is_used
        self.price = price
        self.place = place
        self.owner = None

    def set_owner(self, user):
        self.owner = user

    def purchase_ticket(self, user, user_account):
        if user_account.balance >= self.price:
            user_account.balance -= self.price
            self.buyer_id = user.id
            self.owner = user
            user.add_ticket(self)
            print(f"Билет на маршрут {self.route_number} куплен успешно!")
        else:
            print("Недостаточно средств для покупки билета.")


class Account:
    def __init__(self, user_account_id, balance):
        self.user_account_id = user_account_id
        self.balance = balance


class User:
    def __init__(self, id, name, login, pass_hash_code, account_id):
        self.id = id
        self.name = name
        self.tickets = []
        self.login = login
        self.pass_hash_code = pass_hash_code
        self.account_id = account_id

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def remove_ticket(self, ticket):
        self.tickets.remove(ticket)
