#  Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways

from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"The ticket is booked in train number {self.trainNo} from {fro} to {to}.")

    def status(self):
        print(f"The train number {self.trainNo} is running on time.")

    def fare(self, fro, to):
        print(f"The fare of train number {self.trainNo} running from {fro} to {to} is {randint(1000, 1500)}.")

t = Train(12345)
t.book("Ranchi", "Bokaro")
t.status()
t.fare("Ranchi", "Bokaro")