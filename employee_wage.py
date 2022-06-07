"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-06 10:10:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-06 20:22:00
    @Title : Compute employee wage for multiple companies. Each company has its
            own wage, number of hours per month and number of working days.  And storing
            monthly wage and daily wage.

"""
import random


class Employee:

    def __init__(self, emp_name, emp_rate, number_of_days, max_hrs):
        """
            This is constructor taking having 5 parameters
        :param emp_name: employee name
        :param emp_rate: per hour rate
        :param number_of_days: total working days in a month
        :param max_hrs: total working hours in a month
        """
        self.emp_name = emp_name
        self.max_hrs = max_hrs
        self.emp_rate = emp_rate
        self.number_of_days = number_of_days
        self.monthly_wage = self.calculate_wage()

    @staticmethod
    def emp_attendance():
        """
            finding employee is present or not and also getting daily employee hours
        :return: employee hors
        """
        attendance = random.randint(0, 2)
        if attendance == 0:  # absent
            emp_hrs = 0
        else:
            if attendance == 2:  # Full day
                emp_hrs = 8
            else:  # Half day
                emp_hrs = 4
        return emp_hrs

    def calculate_wage(self):
        """
            calculating employee daily wage
        :return:  monthly wage
        """
        total_hrs = 0
        total_days = 0
        monthly_wage = 0
        try:
            while total_hrs < self.max_hrs and total_days < self.number_of_days:
                # calling check_attendance() to get emp hour every day
                emp_Hrs = Employee.emp_attendance()

                # calculating daily wage of an employee
                daily_wage = self.emp_rate * emp_Hrs
                # print("\tDaily Wage :", daily_wage, "\n")
                # calculating monthly wage for an employee
                monthly_wage += daily_wage

                # calculating total working hours of a month for an employee
                total_hrs += emp_Hrs
                total_days += 1
        except Exception as e:
            print("Please do not press any button", e)
        return monthly_wage

    def __repr__(self):
        return f"Name: {self.emp_name}, emp rate {self.emp_rate}, max hrs {self.max_hrs}"


class Company:

    def __init__(self, company_name):
        self.company_name = company_name
        self.emp_dict = {}

    def add_employee(self, employee):
        """
            Taking inputs from user and updating emp_dict dictionary
        :param employee:
        :return: none
        """
        self.emp_dict.update({employee.emp_name: employee})
        print(self.emp_dict)

    def display_employee(self, emp_name):
        """
            printing particular employee details
        :param emp_name: getting employee name
        :return: none
        """
        print(self.emp_dict.get(emp_name))


def add_company():
    try:
        company_name = input("Enter company name to add: ")
        company = Company(company_name)
        company_dict.update({company_name.upper(): company})
        print("Company added successfully")
        print("-----------------------------")
    except Exception as e:
        print("Please enter correct company name → ", e)


def display_company():
    print("Company")
    print("---------")
    for k in company_dict:
        print(k.upper())
    print("-----------")


def reg_employee():
    wage = []
    try:
        company_name = input("Enter company name to add employee : ")
        com_obj = company_dict.get(company_name.upper())
        if com_obj is not None:
            emp_name = input("Enter employee name :")
            if com_obj.emp_dict.get(emp_name) is None:  # take input here bcoz input enter by user
                emp_rate = int(input("Enter per hr wage :"))
                number_of_days = int(input("Enter total working days in month: "))
                max_hrs = int(input("Enter total working hrs in month: "))
                employee = Employee(emp_name.upper(), emp_rate, number_of_days, max_hrs)
                com_obj.emp_dict.update({employee.emp_name.upper(): employee})
                print("Employee successfully added")
                print("-----------------------------")
            else:
                print("Employee already exist")
                print("-----------------------------")
        else:
            print("Company not found")
    except Exception as e:
        print("Please enter correct company name → ", e)


def emp_wage():
    try:
        company_name = input("Enter company name to know wage  : ")
        com_obj = company_dict.get(company_name.upper())
        if com_obj is not None:
            emp_name = input("Enter employee name :")
            emp_obj = com_obj.emp_dict.get(emp_name.upper())

            if emp_obj is not None:
                # print(f"Total Wage : {wage_list[len(wage_list) - 1]}")
                print("________________________________________________________________")
                monthly_wage = emp_obj.monthly_wage  # ← getting value of monthly wage from constructor
                print("________________________________________________________________")
                print(f"\tTotal wage for {emp_obj.emp_name.upper()}:", monthly_wage)
                print("----------------------------------------------------------------")
            else:
                print(f"{company_name} has no employee with name {emp_name}")
                print()
        else:
            print(f"There is no company with name {company_name}")
            print()
    except Exception as e:
        print("Please enter correct company name → ", e)


def display_employee():
    try:
        company_name = input("Enter company name to find details: ")
        com_obj = company_dict.get(company_name.upper())
        if com_obj is not None:
            print("___________________________________________________")
            print("NAME\tRATE\tWORKING DAYS\tMAX Hrs.")
            print("---------------------------------------------------")
            for k, v in com_obj.emp_dict.items():
                print(f"{v.emp_name.upper()}\t\t{v.emp_rate}\t\t{v.number_of_days}\t\t{v.max_hrs}")
                print("===================================================")
        else:
            print("Company does not exist!")
    except Exception as e:
        print("Please enter correct company name → ", e)


if __name__ == '__main__':
    company_dict = {}
    print("-----------------Welcome to Employee Wage Program --------------------")
    print()
    print("\nChoose the operation on the company you want to perform")
    print("=============================================================")

    more_choice = True
    while more_choice:
        print("1.Add company\n"
              "2.Display company\n"
              "3.Add employee\n"
              "4.Employee wages\n"
              "5.Display employees\n"
              "0.Exit employee wage system System")

        choice = {1: add_company, 2: display_company, 3: reg_employee, 4: emp_wage, 5: display_employee}
        print()
        try:
            user_input = int(input("Enter choice: "))
            if user_input != 0:
                choice.get(user_input)()
            elif user_input == 0:
                more_choice = False
                print("Existing Employee wage system...")
                print()
        except Exception as e:
            print("Please enter valid input ↑")
            print()
