"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-02 19:40:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-02 19:50:00
    @Title : Calculating Wages for a Month
"""
import random


class Employee:
    def __init__(self, wage_per_hr, full_time, part_time):
        self.wage_per_hr = wage_per_hr
        self.full_time = full_time
        self.part_time = part_time

    @staticmethod
    def employee_attendance():
        is_present = random.randint(0, 2)
        if is_present == 2:
            emp_hrs = 4
        elif is_present == 1:
            emp_hrs = 8
        else:
            emp_hrs = 0
        return emp_hrs

    def calculate_wage(self):
        monthly_wage = 0
        for day in range(1, 21):
            print("\nDay : ", day)
            emp_Hrs = Employee.employee_attendance()

            # calculating daily wage for an employee
            daily_wage = self.wage_per_hr * emp_Hrs

            # calculating monthly wage for an employee
            monthly_wage = monthly_wage + daily_wage
            print("Daily Wage :", daily_wage)
        return monthly_wage


if __name__ == '__main__':
    print("Welcome To Employee Wage Management System !!\n")
    employee = Employee(wage_per_hr=20, full_time=8, part_time=4)
    monthly_wage = employee.calculate_wage()
    print("\n------------------------------------")
    print("Monthly wage of an employee: ",monthly_wage)
    print("--------------------------------------")