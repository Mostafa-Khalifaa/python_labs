import json # 
from employee import Employee

class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.change_emps_num(Office.employeesNum + 1)

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp != None:
            self.employees.remove(emp)
            Office.change_emps_num(Office.employeesNum - 1)

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp != None:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp != None:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp != None:
            is_late = Office.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity)
            if is_late:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            return True
        time_taken = distance / velocity
        arrive_hour = moveHour + time_taken
        return arrive_hour > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

    def save_office_data(self):
        office_data = []
        for emp in self.employees:
            emp_dict = {
                "id": emp.id,
                "name": emp.name,
                "email": emp.email,
                "salary": emp.salary,
                "distanceToWork": emp.distanceToWork,
                "money": emp.money,
                "healthRate": emp.healthRate
            }
            office_data.append(emp_dict)

        with open("office_data.json", "w") as json_file:
            json.dump(office_data, json_file)
            print("Data saved")