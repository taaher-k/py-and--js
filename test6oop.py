import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage:
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print(f"Area of the circle: {circle.area():.2f}")
print(f"Perimeter of the circle: {circle.perimeter():.2f}")




class Employee:
    def __init__(self,Name,Role):
        self.Name = Name
        self.Role = Role
    def printdata(self):
        print(f"Name: {self.Name} ")
        print(f"Role: {self.Role} ")    

emp = Employee("Taaher","FullStack-Developer")

emp.printdata()



class Employee:
    def __init__(self):
        # Initialize attributes with default values
        self.name = ""
        self.age = 0
        self.salary = 0.0

    def assignData(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def printData(self):
        print("Employee Details:")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Salary : ₹{self.salary:.2f}")


# Example usage:
emp = Employee()

# Assign data
emp.assignData("Taaher", 23, 45000)

# Print data
emp.printData()

class Employee:
    def __init__(self, Name, Role):
        self.Name = Name
        self.Role = Role

    def getdata(self):
        # Return a formatted string instead of printing directly
        return f"Name: {self.Name}\nRole: {self.Role}"


# Example usage:
emp = Employee("Taaher", "FullStack-Developer")

# Option 1: Print directly
print(emp.getdata())

# Option 2: Store in a variable
details = emp.getdata()
print("Employee Details:\n" + details)



class Student:
    def __init__(self):
        self.marks = []

    def readMarks(self):
        n = int(input("Enter number of subjects: "))
        for i in range(n):
            mark = float(input(f"Enter marks for subject {i+1}: "))
            self.marks.append(mark)
        return sum(self.marks)   # return total marks

    def calculateAverage(self, total, num_subjects):
        average = total / num_subjects
        return average


# Example usage:
student = Student()

# Read marks and get total
total_marks = student.readMarks()
print(f"Total Marks = {total_marks}")

# Calculate average
num_subjects = len(student.marks)
average_marks = student.calculateAverage(total_marks, num_subjects)
print(f"Average Marks = {average_marks:.2f}")



class Banking:
    def __init__(self, balance):
        if balance < 500:
            raise ValueError("Initial balance must be at least ₹500.")
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. Current Balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.balance - amount < 500:
            print("Withdrawal denied. Minimum balance of ₹500 must be maintained.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Current Balance: ₹{self.balance}")

    def checkBalance(self):
        print(f"Current Balance: ₹{self.balance}")


class SavingAccount(Banking):
    def calculateInterest(self):
        if self.balance > 25000:
            interest = self.balance * 6.5 / 100
            self.balance += interest
            print(f"Interest of ₹{interest:.2f} added. New Balance: ₹{self.balance:.2f}")
        else:
            print("Balance less than ₹25,000. No interest applied.")


# ---------------- Menu-driven program ----------------
def main():
    print("Welcome to the Banking System")
    initial_balance = float(input("Enter initial balance (minimum ₹500): "))
    account = SavingAccount(initial_balance)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Calculate Interest")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.checkBalance()
        elif choice == "4":
            account.calculateInterest()
        elif choice == "5":
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
main()



class Division:
    def __init__(self, num1, num2):
        # Constructor initializes two numbers
        self.num1 = num1
        self.num2 = num2

    def quotient(self):
        # Normal division (floating-point result)
        return self.num1 / self.num2

    def floorQuotient(self):
        # Floor division (integer result)
        return self.num1 // self.num2

    def remainder(self):
        # Remainder after division
        return self.num1 % self.num2


# Example usage:
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

obj = Division(n1, n2)

print(f"Quotient (division): {obj.quotient()}")
print(f"Quotient (floor division): {obj.floorQuotient()}")
print(f"Remainder: {obj.remainder()}")





class Employee:
    def __init__(self, name, emp_id, designation, department):
        self.name = name
        self.emp_id = emp_id
        self.designation = designation
        self.department = department

    def displayEmployee(self):
        print("=== Employee Details ===")
        print(f"Name       : {self.name}")
        print(f"ID         : {self.emp_id}")
        print(f"Designation: {self.designation}")
        print(f"Department : {self.department}")


class Salary:
    def __init__(self):
        self.basic_pay = 0.0
        self.hra = 0.0
        self.pf = 0.0
        self.insurance = 0.0

    def readSalary(self):
        self.basic_pay = float(input("Enter Basic Pay: "))
        self.hra = float(input("Enter HRA: "))
        self.pf = float(input("Enter PF: "))
        self.insurance = float(input("Enter Insurance: "))

    def displaySalary(self):
        print("=== Salary Details ===")
        print(f"Basic Pay : ₹{self.basic_pay:.2f}")
        print(f"HRA       : ₹{self.hra:.2f}")
        print(f"PF        : ₹{self.pf:.2f}")
        print(f"Insurance : ₹{self.insurance:.2f}")
        total = self.basic_pay + self.hra - self.pf - self.insurance
        print(f"Net Salary: ₹{total:.2f}")


# Example usage:
emp = Employee("Taaher", 101, "FullStack Developer", "IT")
emp.displayEmployee()

sal = Salary()
sal.readSalary()
sal.displaySalary()















class Salary:
    def __init__(self, basic_pay=0.0, hra=0.0, pf=0.0, insurance=0.0):
        self.basic_pay = basic_pay
        self.hra = hra
        self.pf = pf
        self.insurance = insurance

    def readSalary(self):
        self.basic_pay = float(input("Enter Basic Pay: "))
        self.hra = float(input("Enter HRA: "))
        self.pf = float(input("Enter PF: "))
        self.insurance = float(input("Enter Insurance: "))

    def displaySalary(self):
        print("=== Salary Details ===")
        print(f"Basic Pay : ₹{self.basic_pay:.2f}")
        print(f"HRA       : ₹{self.hra:.2f}")
        print(f"PF        : ₹{self.pf:.2f}")
        print(f"Insurance : ₹{self.insurance:.2f}")
        total = self.basic_pay + self.hra - self.pf - self.insurance
        print(f"Net Salary: ₹{total:.2f}")


class Employee:
    def __init__(self, name, emp_id, designation, department):
        self.name = name
        self.emp_id = emp_id
        self.designation = designation
        self.department = department
        self.salary = Salary()   # Association: each Employee has a Salary object

    def displayEmployee(self):
        print("=== Employee Details ===")
        print(f"Name       : {self.name}")
        print(f"ID         : {self.emp_id}")
        print(f"Designation: {self.designation}")
        print(f"Department : {self.department}")
        # Also display salary details
        self.salary.displaySalary()


# Example usage:
emp = Employee("Taaher", 101, "FullStack Developer", "IT")

# Read salary details for this employee
emp.salary.readSalary()

# Display both employee and salary details together
emp.displayEmployee()



class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. Current Balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= 0:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Current Balance: ₹{self.balance}")
        else:
            print("Withdrawal denied. Insufficient balance or invalid amount.")


# Child class: Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, balance=0.0, rate=0.05, time=1):
        super().__init__(balance)
        self.rate = rate   # Interest rate (default 5%)
        self.time = time   # Time in years

    def calculateInterest(self):
        interest = self.balance * self.rate * self.time
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} added. New Balance: ₹{self.balance:.2f}")


# Child class: Current Account
class CurrentAccount(BankAccount):
    # Only deposit and withdraw (inherits directly from BankAccount)
    pass


# ---------------- Example usage ----------------
print("=== Savings Account Example ===")
savings = SavingsAccount(10000, rate=0.06, time=2)  # balance, rate, time
savings.deposit(2000)
savings.withdraw(1500)
savings.calculateInterest()


print("\n=== Current Account Example ===")
current = CurrentAccount(5000)
current.deposit(1000)
current.withdraw(2000)




# Superclass: Employee
class Employee:
    def __init__(self, emp_id, first_name, last_name, salary):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def displayEmployee(self):
        print("=== Employee Details ===")
        print(f"ID        : {self.emp_id}")
        print(f"Name      : {self.first_name} {self.last_name}")
        print(f"Salary    : ₹{self.salary:.2f}")


# Subclass: Manager
class Manager(Employee):
    def __init__(self, emp_id, first_name, last_name, salary, stock_options):
        super().__init__(emp_id, first_name, last_name, salary)
        self.stock_options = stock_options

    def displayManager(self):
        self.displayEmployee()
        print(f"Stock Options : {self.stock_options}")


# Subclass: SalesPerson
class SalesPerson(Employee):
    def __init__(self, emp_id, first_name, last_name, salary, num_sales, commission_rate):
        super().__init__(emp_id, first_name, last_name, salary)
        self.num_sales = num_sales
        self.commission_rate = commission_rate

    def calculateCommission(self):
        commission = self.num_sales * self.commission_rate
        return commission

    def displaySalesPerson(self):
        self.displayEmployee()
        print(f"Number of Sales : {self.num_sales}")
        print(f"Commission Rate : ₹{self.commission_rate:.2f} per sale")
        print(f"Total Commission: ₹{self.calculateCommission():.2f}")



# Manager object
mgr = Manager(101, "Taaher", "Khan", 80000, 50)
mgr.displayManager()

print("\n")

# SalesPerson object
sp = SalesPerson(102, "Rahul", "Sharma", 40000, num_sales=120, commission_rate=500)
sp.displaySalesPerson()



class EmployeeSalary:
    def __init__(self, basic_salary=0.0, bonus=0.0, loss_of_pay=0.0):
        # Private attributes (encapsulation)
        self.__basic_salary = basic_salary
        self.__bonus = bonus
        self.__loss_of_pay = loss_of_pay

    # Getter and Setter for Basic Salary
    def setBasicSalary(self, amount):
        self.__basic_salary = amount

    def getBasicSalary(self):
        return self.__basic_salary

    # Getter and Setter for Bonus
    def setBonus(self, amount):
        self.__bonus = amount

    def getBonus(self):
        return self.__bonus

    # Getter and Setter for Loss of Pay
    def setLossOfPay(self, amount):
        self.__loss_of_pay = amount

    def getLossOfPay(self):
        return self.__loss_of_pay

    # Method to calculate total salary
    def calculateTotalSalary(self):
        total = self.__basic_salary + self.__bonus - self.__loss_of_pay
        return total

    # Display method
    def displaySalary(self):
        print("=== Employee Salary Details ===")
        print(f"Basic Salary : ₹{self.__basic_salary:.2f}")
        print(f"Bonus        : ₹{self.__bonus:.2f}")
        print(f"Loss of Pay  : ₹{self.__loss_of_pay:.2f}")
        print(f"Total Salary : ₹{self.calculateTotalSalary():.2f}")


# ---------------- Example usage ----------------
emp = EmployeeSalary()
emp.setBasicSalary(50000)
emp.setBonus(10000)
emp.setLossOfPay(2000)

emp.displaySalary()





from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def findarea(self):
        pass


# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def findarea(self):
        return math.pi * self.radius ** 2


# Derived Class: Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def findarea(self):
        return self.side ** 2


# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def findarea(self):
        return self.length * self.width


# ---------------- Menu-driven program ----------------
def main():
    while True:
        print("\n=== Shape Area Calculator ===")
        print("1. Circle")
        print("2. Square")
        print("3. Rectangle")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            r = float(input("Enter radius: "))
            circle = Circle(r)
            print(f"Area of Circle: {circle.findarea():.2f}")

        elif choice == "2":
            s = float(input("Enter side length: "))
            square = Square(s)
            print(f"Area of Square: {square.findarea():.2f}")

        elif choice == "3":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            rectangle = Rectangle(l, w)
            print(f"Area of Rectangle: {rectangle.findarea():.2f}")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()



from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def findarea(self):
        pass


# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def findarea(self):
        area = math.pi * self.radius ** 2
        print(f"Circle Area (radius={self.radius}): {area:.2f}")
        return area


# Derived Class: Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def findarea(self):
        area = self.side ** 2
        print(f"Square Area (side={self.side}): {area:.2f}")
        return area


# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def findarea(self):
        area = self.length * self.width
        print(f"Rectangle Area (length={self.length}, width={self.width}): {area:.2f}")
        return area


# ---------------- Example usage ----------------
circle = Circle(5)
circle.findarea()

square = Square(4)
square.findarea()

rectangle = Rectangle(6, 3)
rectangle.findarea()


class Gmail:
    def login(self, *args):
        if len(args) == 2:
            username, password = args
            print(f"Logging in with username: {username} and password: {password}")
        elif len(args) == 1:
            password = args[0]
            print(f"Logging in with password only: {password}")
        else:
            print("Invalid login attempt. Provide either password or username+password.")


# Usage this is methode overloading
g = Gmail()
g.login("taaher", "secure123")   # username + password
g.login("secure123")             # password only


class Gmail:
    def __init__(self):
        self.username = None
        self.password = None
        self.logged_in = False

    def login(self, *args):
        if len(args) == 2:
            self.username, self.password = args
            self.logged_in = True
            print(f"✅ Logged in with username: {self.username}")
        elif len(args) == 1:
            self.password = args[0]
            self.logged_in = True
            print(f"✅ Logged in with password only")
        else:
            print("⚠️ Invalid login attempt. Provide either password or username+password.")

    def logout(self):
        if self.logged_in:
            print(f"👋 User {self.username if self.username else 'Unknown'} logged out.")
            self.username = None
            self.password = None
            self.logged_in = False
        else:
            print("⚠️ No active session to logout.")

    def view_credentials(self):
        if self.logged_in:
            print(f"🔐 Username: {self.username if self.username else 'Not set'}")
            print(f"🔐 Password: {self.password}")
        else:
            print("⚠️ Not logged in. No credentials stored.")


# Menu-driven simulation
def main():
    g = Gmail()
    while True:
        print("\n--- Gmail Menu ---")
        print("1. Login with username & password")
        print("2. Login with password only")
        print("3. View credentials")
        print("4. Logout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            u = input("Enter username: ")
            p = input("Enter password: ")
            g.login(u, p)
        elif choice == "2":
            p = input("Enter password: ")
            g.login(p)
        elif choice == "3":
            g.view_credentials()
        elif choice == "4":
            g.logout()
        elif choice == "5":
            print("Exiting Gmail simulation. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


# Run program
main()

class Calculator:
    def add(self, *args):
        if len(args) == 2:
            result = args[0] + args[1]
            print(f"Adding two numbers: {args[0]} + {args[1]} = {result}")
        elif len(args) == 3:
            result = args[0] + args[1] + args[2]
            print(f"Adding three numbers: {args[0]} + {args[1]} + {args[2]} = {result}")
        else:
            print("⚠️ Please provide 2 or 3 numbers only.")


# Usage
calc = Calculator()
calc.add(10, 20)        # Two numbers
calc.add(5, 15, 25)     # Three numbers
calc.add(7)             # Invalid case





class Calculator:
    def add(self, *args):
        if len(args) == 2:
            print(f"Result: {args[0]} + {args[1]} = {args[0] + args[1]}")
        elif len(args) == 3:
            print(f"Result: {args[0]} + {args[1]} + {args[2]} = {args[0] + args[1] + args[2]}")
        else:
            print("⚠️ Provide 2 or 3 numbers only.")

    def subtract(self, *args):
        if len(args) == 2:
            print(f"Result: {args[0]} - {args[1]} = {args[0] - args[1]}")
        elif len(args) == 3:
            print(f"Result: {args[0]} - {args[1]} - {args[2]} = {args[0] - args[1] - args[2]}")
        else:
            print("⚠️ Provide 2 or 3 numbers only.")

    def multiply(self, *args):
        if len(args) == 2:
            print(f"Result: {args[0]} × {args[1]} = {args[0] * args[1]}")
        elif len(args) == 3:
            print(f"Result: {args[0]} × {args[1]} × {args[2]} = {args[0] * args[1] * args[2]}")
        else:
            print("⚠️ Provide 2 or 3 numbers only.")

    def divide(self, *args):
        try:
            if len(args) == 2:
                print(f"Result: {args[0]} ÷ {args[1]} = {args[0] / args[1]}")
            elif len(args) == 3:
                print(f"Result: {args[0]} ÷ {args[1]} ÷ {args[2]} = {args[0] / args[1] / args[2]}")
            else:
                print("⚠️ Provide 2 or 3 numbers only.")
        except ZeroDivisionError:
            print("❌ Division by zero is not allowed!")


# Menu-driven simulation
def main():
    calc = Calculator()
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "4"]:
            nums = input("Enter 2 or 3 numbers separated by space: ").split()
            nums = list(map(float, nums))  # convert to float for flexibility

            if choice == "1":
                calc.add(*nums)
            elif choice == "2":
                calc.subtract(*nums)
            elif choice == "3":
                calc.multiply(*nums)
            elif choice == "4":
                calc.divide(*nums)
        elif choice == "5":
            print("👋 Exiting Calculator. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


# Run program
main()




class Employee:
    def work(self):
        print("Employee is working on general tasks.")

class Trainee(Employee):
    def work(self):   # overriding
        print("Trainee is learning and assisting with tasks.")

class Manager(Employee):
    def work(self):   # overriding
        print("Manager is planning and supervising tasks.")


# Polymorphism in action
def show_work(emp):
    emp.work()   # same method name, different behavior


# Usage
e = Employee()
t = Trainee()
m = Manager()

for person in (e, t, m):
    show_work(person)



class Employee:
    def __init__(self, staff_id, name, basic_salary, loss_of_pay):
        self.staff_id = staff_id
        self.name = name
        self.basic_salary = basic_salary
        self.loss_of_pay = loss_of_pay

    def calculate_pay(self):
        # Base calculation (without incentives)
        net_pay = self.basic_salary - self.loss_of_pay
        return net_pay

    def display(self):
        print("\n--- Employee Details ---")
        print(f"Staff ID   : {self.staff_id}")
        print(f"Name       : {self.name}")
        print(f"Basic Pay  : {self.basic_salary}")
        print(f"Loss of Pay: {self.loss_of_pay}")
        print(f"Net Pay    : {self.calculate_pay()}")


class Trainee(Employee):
    def __init__(self, staff_id, name, basic_salary, loss_of_pay, incentives):
        # Call parent constructor
        super().__init__(staff_id, name, basic_salary, loss_of_pay)
        self.incentives = incentives

    # Method overriding
    def calculate_pay(self):
        net_pay = (self.basic_salary - self.loss_of_pay) + self.incentives
        return net_pay

    def display(self):
        print("\n--- Trainee Details ---")
        print(f"Staff ID   : {self.staff_id}")
        print(f"Name       : {self.name}")
        print(f"Basic Pay  : {self.basic_salary}")
        print(f"Loss of Pay: {self.loss_of_pay}")
        print(f"Incentives : {self.incentives}")
        print(f"Net Pay    : {self.calculate_pay()}")


# 🖥️ Usage
# Get details from user
sid = input("Enter Staff ID: ")
name = input("Enter Name: ")
basic = float(input("Enter Basic Salary: "))
lop = float(input("Enter Loss of Pay: "))
inc = float(input("Enter Incentives: "))

# Create Trainee object
t = Trainee(sid, name, basic, lop, inc)
t.display()










#Association (Has-a relationship)

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine   # association

    def drive(self):
        self.engine.start()
        print("Car is driving.")

# Usage
eng = Engine()
car = Car(eng)
car.drive()

#. Composition (Strong ownership)
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [Room("Living Room"), Room("Bedroom")]  # composition

    def show_rooms(self):
        for room in self.rooms:
            print(f"Room: {room.name}")

# Usage
h = House()
h.show_rooms()



#. Aggregation (Weak ownership)

class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, players):
        self.players = players   # aggregation

    def show_team(self):
        for p in self.players:
            print(f"Player: {p.name}")

# Usage
p1 = Player("Virat")
p2 = Player("Dhoni")
team = Team([p1, p2])
team.show_team()




