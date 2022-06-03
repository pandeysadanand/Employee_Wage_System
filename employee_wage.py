"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-02 19:25:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-02 19:30:00
    @Title : Add Part time Employee & calculate Wage
"""
import random


class Employee:
    @staticmethod
    def check_attendance():
        wage_per_hr = 20
        emp_Hrs = 0

        is_present = (random.randint(0, 2))
        if is_present == 2:
            print("Employee is present Part Time")
            emp_Hrs = 4
        elif is_present == 1:
            print("Employee is present Full Time")
            emp_Hrs = 8
        else:
            print("Employee is Absent")

        daily_wage = wage_per_hr * emp_Hrs
        print("Daily Wage :", daily_wage)


if __name__ == '__main__':
    print("Welcome To Employee Wage Management System !!\n")
    print()
    Employee.check_attendance()
