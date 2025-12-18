#1. Store 10 numbers in a list. Remove duplicates by using pre-defined
#function.

mylist = [20,50,80,56,20,50,80,90,100,56]


listwithoutduplicates =  list(set(mylist))

print(listwithoutduplicates,mylist)


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(my_tuple[0])

myset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}




my_dict = {"1": "Taaher", "age": 22}
print(my_dict["1"])

text = "python"

print(text[-1:-7:-1])  #n o h t y p

print(text[::-1])      #n o h t y p


my_list = [1, 2, 3, 4]

# Convert to tuple
my_tuple = tuple(my_list)
print(my_tuple)   # (1, 2, 3, 4)


my_list = [1, 2, 2, 3, 4]

# Convert to set
my_set = set(my_list)
print(my_set)   # {1, 2, 3, 4}


my_list = [("name", "Taaher"), ("age", 22), ("city", "Chennai")]

# Convert to dictionary
my_dict = dict(my_list)
print(my_dict)   # {'name': 'Taaher', 'age': 22, 'city': 'Chennai'}


keys = ["name", "age", "city"]
values = ["Taaher", 22, "Chennai"]

# Zip them together
my_dict = dict(zip(keys, values))
print(my_dict)   # {'name': 'Taaher', 'age': 22, 'city': 'Chennai'}


# Step 1: Create dictionary with subject names as keys and marks as values
marks_dict = {
    "Math": 85,
    "Science": 90,
    "English": 78
}

# Step 2: Display marks one by one
print("Marks in each subject:")
for subject in marks_dict:
    print(marks_dict[subject])


for subject, mark in marks_dict.items():
    print(subject, ":", mark)


fruits = ["apple", "banana", "cherry"]

# Equivalent to a for loop:
iterator = iter(fruits)

print(next(iterator))  # apple
print(next(iterator))  # banana
print(next(iterator))  # cherry
# next(iterator) → raises StopIteration

cd="pyprepare"

cdp = iter(cd)
print(next(cdp))
print(next(cdp))            
print(next(cdp))
print(next(cdp))

rt = [123485]

rty = iter(str(rt))

print(next(rty))
print(next(rty))
print(next(rty))

tyr = "TAaher"#input("e").lower()

count = 0
volwels = "aeiou"#"aeiouAEIOU"
volwels_list =[]
for char in tyr.lower():
    if char in  volwels:#or "aeiou":
        volwels_list.append(char)
        count += 1
print(f"Total vowels in {tyr} are {count} and the vowels are {volwels_list}")        




text = "Aftab"#input("Enter a string: ")
count = sum(1 for char in text if char.lower() in "aeiou")
print("Number of vowels:", count)


"""
subjects_dict = {}
count = 0
num_of_subjects = int (input("enter the number of subjects:"))


for _ in range(num_of_subjects):
    subject_name = input("Enter the subject name:")
    marks = int(input(f"enter teh marks for {subject_name}"))
    subjects_dict[subject_name] = marks
    count +=1


print(subjects_dict) 

total_marks = sum(subjects_dict.values())

average_marks = total_marks / count

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")

if average_marks >= 90:
  print("Grade: A")
elif average_marks >= 80:
  print("Grade: B")
elif average_marks >= 70:
  print("Grade: C")
elif average_marks >= 60:
  print("Grade: D")
else:
  print("Grade: F")

def check_percentage(x):
    match x:
        case x if x >= 75:
            print("Distinction.")
        case x if x >= 60:
            print("First Class.")
        case x if x >= 50:
            print("Second Class.")
        case x if x < 50:
            print("Fail.")
        case _:
            print("Invalid entry.")
check_percentage(average_marks)
"""
q,w,e = 10,20,30

if q>w and q>e:
    print("q is greater")
elif w>q and w>e:
    print("w is greater")
else:
    print("e is greater")    

if q>w:
    if q>e:
       print("q is greater")
    else:
       print("e is greater")      
else:

    if w>e:
       print("w is greater")
    else:
       print("e is greater")              



num = int(input("Enter a number: "))

print("Digits are:")
for digit in str(num):
    print(digit)






#same same but different start

for i in range(30, 1, -1):
    if i % 2 != 0:
     print(i)

f = []
for q in range(1, 31):
    if q % 2 != 0:
        f.append(q)
print(list(reversed(f)))

f = [q for q in range(29, 0, -2)]
print(f)

f = [q for q in range(1, 31) if q % 2 != 0]
print(list(reversed(f)))

#same same but different end


#4.1

list_numbers = [10, 25, 5, 75, 60, 45, 90, 15, 30,150,50]

def max_num(x):
    max_value = x[0]
    for num in x:
        if num > max_value:
            max_value = num

    return max_value


def second_max(x):
    first_max = max_num(x)
    second_max_value = x[0]
    for num in x:
        if num < first_max and num > second_max_value:
            second_max_value = num
    return second_max_value

print("Maximum number is:", max_num(list_numbers))
print("Second maximum number is:", second_max(list_numbers)) 


def add(a,b):
    return a + b


def sub(a,b):
    return a - b


def mul(a,b):
    return a * b


def div(a,b):
    return a / b


def moules(a,b):
    return a % b

def floor_div(a,b):
    return a // b

def power(a,b):
    return a ** b

print("Addition:", add(10, 5))
print("Subtraction:", sub(10, 5))
print("Multiplication:", mul(10, 5))
print("Division:", div(10, 5))
print("Modulus:", moules(10, 5))
print("Floor Division:", floor_div(10, 5))
print("Power:", power(10, 5))

xlist = [10, 5]
ylist = [2, 0]


def calculator(x, y, operation):
    match operation:
        case "add":
            return add(x, y)
        case "sub":
            return sub(x, y)
        case "mul":
            return mul(x, y)
        case "div":
            return div(x, y)
        case "moules":
            return moules(x, y)
        case "floor_div":
            return floor_div(x, y)
        case "power":
            return power(x, y)
        case _:
            return "Invalid operation"

print("Addition:", calculator(sum(xlist), sum(ylist), "add"))


bill_amount =35000

gst = 18

numnber_of_EMIs = 6

def emi_calculator(bill, gst_rate, num_emis):
    total_bill = bill + (bill * gst_rate / 100)
    emi_amount = total_bill / num_emis
    return total_bill, emi_amount

print("Total Bill and EMI Amount:", emi_calculator(bill_amount, gst, numnber_of_EMIs))


def read_to_digi():
    input_num = input("Enter a number: ")
    cond = [int(c) for c in input_num]
    #con = list(input_num)
    #cond = list(map(int,con))
    #cond = [int(c)for c in con]
 
    return cond
print("Digits are:", (read_to_digi()))

#4.2



def avg_marks(sudent_name, *marks):
    total = sum(marks)
    average = total / len(marks)
    return f"Student: {sudent_name}, Average Marks: {average}"
print(avg_marks("Taaher", 85, 90, 78, 92, 88))



def student_info(name, age, **kwargs):
    info = f"Name: {name}, Age: {age}"
    for key, value in kwargs.items():
        info += f", {key}: {value}"
    return info
print(student_info("Taaher", 22, City="Chennai", Course="Engineering"))



def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120




def sum_of_digits(n):
    # Base case
    if n == 0:
        return 0
    # Recursive case
    else:
        return (n % 10) + sum_of_digits(n // 10)

# Example usage
print(sum_of_digits(1234),"this is the last digit from 1234 by using num % 10 ",1234%10,"this is the last digit removed from 1234 by using num // 10 ",1234//10)  # Output: 10

def fibonacci(n):
    # Base case
    if n <= 0:
        return []  
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    # Recursive case
    else:
        fib_sequence = fibonacci(n - 1)
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
        return fib_sequence
    
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Generator function for Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the limit (n): "))
    print(f"Fibonacci numbers up to {n}:")
    for num in fibonacci(n):
        print(num, end=" ")
 
def fibo():
    n = int(input("Enter the number of terms in Fibonacci sequence: "))
    for x in range(n):
       a,b = 0,1
       if a <= n:
         a, b = b, a + b
       print(x,a,b)

print(fibo())

# Generator function to reverse a string
def reverse_string(text):
    index = len(text) - 1
    while index >= 0:
        yield text[index]
        index -= 1

# Example usage
if __name__ == "__main__":
    input_str = input("Enter a string: ")
    print("Reversed string:")
    for char in reverse_string(input_str):
        print(char, end="")
           
        
def rev(n):
    for i in  n [::-1]:
        yield i
n = input("enter the string")
r= rev(n)
print ("reversed string")

for i in r:
    print(i,end=" ")        

# 2

def reverse_string_gen(s):
    for i in range(len(s) - 1, -1, -1):
        yield s[i]

# Example usage
text = "Taaher"
print(f"Reversed string of '{text}':")
for char in reverse_string_gen(text):
    print(char, end="")


#3

name = "aftab"
namerev = []

for x in range(len(name)-1,-1,-1):
    namerev.append(name[x])

print( "".join(namerev))

"""
tr = "Taaher"
def revs(tr):
    for i in x(len(tr)-1,-1,-1):
     yield tr[i]

for j in revs(tr):
    print(j,end="")

    error because x is looks like a function 
"""



def genrev(x):
    for i in x[::-1]:
        yield i

for y in genrev("Taaher"):
   #print("Reversed string:",y,end="")  do not add any things when you print yielded value expect the value and use end="" to avoid new line
   print(y,end="")


# Option 1: Using a for loop
print("Reversed string:", end=" ")
for j in genr   ev("Taaher"):
    print(j, end="")

# Option 2: Collect into a string
print("\nReversed string:", "".join(genrev("Taaher")))