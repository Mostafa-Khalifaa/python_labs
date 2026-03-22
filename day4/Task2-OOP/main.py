from car import Car
from employee import Employee
from office import Office

my_car = Car(name="ford", fuelRate=100, velocity=0)

mostafa = Employee(name="mostafa", money=1000, mood="happy", healthRate=100, 
                id=1, car=my_car, email="mostafa@gmail.com", salary=5000, distanceToWork=20)

myOffice = Office(name="mostafa kh office")

myOffice.hire(mostafa)

myOffice.save_office_data()