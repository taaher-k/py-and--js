
#1.1

print("hellow",end="")
print("world","taaher",sep="***")

print("python\nprogramming")




#1.2


mydetails = ("taaher","B.com ComputerApplication",2023,)

name = mydetails[0]
course = mydetails[1]
year = mydetails[2]

print(f"Name: {name}\nCourse: {course}\nYear of passing: {year}")



a = 5
b = 3
# in python we have to use f""" """ for multi line formatted string

print(f"""all the arithmatic operation between .{a} and {b} are:\n
Addition: {a + b}\n
Subtraction: {a - b}\n
Multiplication: {a * b}\n
Division: {a / b}\n
Floor Division: {a // b}\n
Modulus: {a % b}\n
Exponentiation: {a ** b} (eg)5x5x5 = 125\n """)



c = b
b = a
a = c

print(f"before swapping a = 5 b = 3  after swapping a = {a} and b = {b}")



a, b = b, a

print(f"before swapping:\n a = 3\n b = 5\n after swapping:\n a = {a}\n b = {b}")


#2.1
num  = int(input("Enter a number to check if its odd or even: "))

print(f"The number {num} is", "Even\n" if num % 2 == 0 else "Odd\n")


y = []
count = 1
subject = int(input("Enter number of subjects: "))
for x in range(subject):
    marks = int(input(f"Enter your marks for subject {count}: "))
    y.append(marks)
    count += 1
    
print (f"Your marks are: {y}")



def find_average_list(numbers):
    average = sum(numbers) / len(numbers)
    return average


print(f"Your average marks are: {find_average_list(y)}")
