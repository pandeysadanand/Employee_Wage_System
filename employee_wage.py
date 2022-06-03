"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-02 19:15:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-02 19:20:00
    @Title : Calculate Daily Employee Wage
"""
import random


class Employee:
    @staticmethod
    def check_attendance():
        wage_per_hr = 20
        total_hrs = 8

        is_present = random.randint(0, 1)
        if is_present == 1:
            print("Employee is present")
            daily_wage = wage_per_hr * total_hrs
            print("Daily wage :", daily_wage)
        else:
            print("Employee is Absent")
            daily_wage= 0
            print("Daily wage :", daily_wage)


if __name__ == '__main__':
    print("Welcome To Employee Wage Management System !!\n")
    Employee.check_attendance()
