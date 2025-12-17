#1. Polymorphism
#Meaning: Same method name, different behavior depending on the object.

#Example:  


class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())   # Woof! / Meow!


#2. Abstraction
#Meaning: Hiding implementation details and exposing only the essential features.

#In Python, abstraction is often done using abstract base classes (ABC).

#Example:


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print(c.area())   # 78.5



#3. Constructor & Destructor
#Constructor (__init__) → initializes object state.

#Destructor (__del__) → cleans up resources when object is deleted.

#Example:


class Demo:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

d = Demo()
del d


#4. Method Types
#Instance methods → work with object data (self).

#Class methods → work with class-level data (@classmethod).

#Static methods → utility functions (@staticmethod).

#Example:

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def show(self):   # instance method
        print("Name:", self.name)

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def greet():
        print("Hello Students!")

s = Student("Taaher")
s.show()
Student.greet()
Student.change_school("XYZ School")
print(Student.school)

#Encapsulation → hiding data inside the class

#Inheritance → child class reusing parent functionality

#Polymorphism → same method name behaving differently

#Abstraction → defining abstract methods that must be implemented#


from abc import ABC, abstractmethod

# 🔹 Abstraction: Abstract base class
class Person(ABC):
    def __init__(self, name):
        self._name = name   # Encapsulation: protected attribute

    @abstractmethod
    def display_info(self):
        pass


# 🔹 Parent class
class MarksCollector(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__marks = []   # Encapsulation: private attribute
        self.__count = 1
        self.__subjects = 0

    def get_subjects(self):
        while True:
            try:
                subject = int(input("Enter number of subjects: "))
                if subject <= 0 or subject > 100:
                    print("Number of subjects must be between 1 and 100. Try again.")
                    continue
                self.__subjects = subject
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    def collect_marks(self):
        for _ in range(self.__subjects):
            while True:
                try:
                    marks = int(input(f"Enter your marks for subject {self.__count}: "))
                    if marks < 0 or marks > 100:
                        print("Marks should be between 0 and 100. Try again.")
                        continue
                    self.__marks.append(marks)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid integer for marks.")
            self.__count += 1

    def display_marks(self):
        print(f"Marks collected: {self.__marks}")

    def find_average(self):
        if self.__marks:
            return sum(self.__marks) / len(self.__marks)
        return 0

    def _get_marks(self):
        return self.__marks

    # 🔹 Polymorphism: implementing abstract method
    def display_info(self):
        print(f"Collector Name: {self._name}")


# 🔹 Child class (Inheritance)
class StudentMarksCollector(MarksCollector):
    def __init__(self, student_name):
        super().__init__(student_name)
        self.student_name = student_name

    # 🔹 Polymorphism: overriding parent method
    def display_info(self):
        print(f"Student Name: {self.student_name}")

    def highest_mark(self):
        marks = self._get_marks()
        return max(marks) if marks else None

    def lowest_mark(self):
        marks = self._get_marks()
        return min(marks) if marks else None


# 🔹 Example usage
student = StudentMarksCollector("Taaher")
student.get_subjects()
student.collect_marks()
student.display_info()
student.display_marks()
print(f"Average Marks: {student.find_average()}")
print(f"Highest Mark: {student.highest_mark()}")
print(f"Lowest Mark: {student.lowest_mark()}")



#Method Overriding → A child class provides a new implementation of
#a method already defined in the parent class.

#Method Overloading → Same method name but different
#number/types of parameters.

#⚠️ In Python, true overloading doesn’t exist like in Java/C++; instead,
#we simulate it using default arguments or *args.


from abc import ABC, abstractmethod

# Abstraction
class Person(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def display_info(self):
        pass


class MarksCollector(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__marks = []
        self.__count = 1
        self.__subjects = 0

    def get_subjects(self):
        while True:
            try:
                subject = int(input("Enter number of subjects: "))
                if subject <= 0 or subject > 100:
                    print("Number of subjects must be between 1 and 100. Try again.")
                    continue
                self.__subjects = subject
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    def collect_marks(self):
        for _ in range(self.__subjects):
            while True:
                try:
                    marks = int(input(f"Enter your marks for subject {self.__count}: "))
                    if marks < 0 or marks > 100:
                        print("Marks should be between 0 and 100. Try again.")
                        continue
                    self.__marks.append(marks)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid integer for marks.")
            self.__count += 1

    def display_marks(self):
        print(f"Marks collected: {self.__marks}")

    def find_average(self):
        if self.__marks:
            return sum(self.__marks) / len(self.__marks)
        return 0

    def _get_marks(self):
        return self.__marks

    # Polymorphism (abstract method implemented)
    def display_info(self):
        print(f"Collector Name: {self._name}")


class StudentMarksCollector(MarksCollector):
    def __init__(self, student_name):
        super().__init__(student_name)
        self.student_name = student_name

    # 🔹 Method Overriding: redefining parent's display_info()
    def display_info(self):
        print(f"Student Name: {self.student_name}")

    # 🔹 Method Overloading (simulated with default args)
    def calculate_total(self, *args):
        """
        If no arguments → use collected marks.
        If arguments provided → calculate total of those numbers.
        """
        if args:
            return sum(args)
        else:
            return sum(self._get_marks())

    def highest_mark(self):
        marks = self._get_marks()
        return max(marks) if marks else None

    def lowest_mark(self):
        marks = self._get_marks()
        return min(marks) if marks else None


# Example usage
student = StudentMarksCollector("Taaher")
student.get_subjects()
student.collect_marks()
student.display_info()   # Overridden method
student.display_marks()

print(f"Average Marks: {student.find_average()}")
print(f"Highest Mark: {student.highest_mark()}")
print(f"Lowest Mark: {student.lowest_mark()}")

# Demonstrating Overloading
print("Total (collected marks):", student.calculate_total())
print("Total (custom numbers 10, 20, 30):", student.calculate_total(10, 20, 30))



#Quick Answer: In Python, dispatch usually refers to function overloading or dynamic
#method selection. The most common way is using the @dispatch
#decorator (from the multipledispatch library) which lets you define
#multiple versions of a function with the same name but different argument
# types, and Python will automatically choose the correct one at runtime.

#Dispatch = deciding which function/method to call based on the arguments.

#Python doesn’t support traditional method overloading like Java or C++. Instead, you can achieve it using:

#Single Dispatch → one function chosen based on the type of the first argument.

#Multiple Dispatch → function chosen based on the types of all arguments.


#✅ Example: Multiple Dispatch with multipledispatch

from multipledispatch import dispatch

@dispatch(int, int)
def add(x, y):
    return x + y

@dispatch(str, str)
def add(x, y):
    return x + " " + y

@dispatch(object, object)
def add(x, y):
    return f"{x} + {y}"

print(add(1, 2))        # 3
print(add("Hello", "World"))  # "Hello World"
print(add(1, "Python")) # "1 + Python"


#Here:

#add(int, int) → adds numbers.

#add(str, str) → concatenates strings.

#add(object, object) → fallback for other types.
#👉 Python automatically dispatches to the correct version depending on argument types.


#✅ Example: Single Dispatch with functools.singledispatch

from functools import singledispatch

@singledispatch
def process(value):
    print("Default:", value)

@process.register(int)
def _(value):
    print("Integer:", value)

@process.register(list)
def _(value):
    print("List:", value)

process(10)        # Integer: 10
process([1, 2, 3]) # List: [1, 2, 3]
process("Hi")      # Default: Hi


#@singledispatch creates a base function.

#.register(type) adds specialized versions.

#Python dispatches based on the type of the first argument.


#⚡ When to Use Dispatch
#Cleaner code when you want different behavior for different types.

#Avoids long if/elif chains checking types manually.

#Useful in OOP systems, data processing, or API design where inputs vary.

#🚨 Limitations & Risks
#Requires external libraries (multipledispatch) for full multiple dispatch.

#Can be harder to debug if too many overloads exist.

#Overuse may reduce readability compared to explicit type checks.



