import re
from person import Person 

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super(Employee, self).__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 1000:
            self._salary = 1000
        else:
            self._salary = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, value):
            self._email = value
        else:
            self._email = "invalid@mail.com"

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance, velocity):
        self.car.run(velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        f1 = open("email.txt", 'w')
        f1.write(f"From: {self.email}\nTo: {to}\nHi, {receiver_name}\n{msg}\n{subject}\n")
        f1.close()