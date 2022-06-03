"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-02 19:00:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-02 19:10:00
    @Title : Check Employee is Present or Absent

"""
import random


class Employee:
    @staticmethod
    def check_attendance():
        is_present = (random.randint(0, 1))
        if is_present == 1:
            print("Employee is present")
        else:
            print("Employee is Absent")


if __name__ == '__main__':
    print("Welcome To Employee Wage Management System !!\n")
    Employee.check_attendance()
