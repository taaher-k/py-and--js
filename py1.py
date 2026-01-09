
#1.1

print("hellow",end="")
print("world","taaher",sep="***")

print("python\nprogramming")


s = "aabbcc"
print("".join(set(s)))



def fun(a, b=2):
    return a + b

print(fun(5))
# outout 7
print(bool(0))
# output False
print(bool(1))
# output True
print("hello"[::-1])



print(type(set([91,2,123])))
print(type([91,2,123]))
print(type(tuple([91,2,123])))
print(type(dict([(1,'a'),(2,'b'),(3,'c')])))

print(type(frozenset([1,2,3,4])))


print(type(b'hello'))
print(type(bytearray(b'hello')))
print(type(memoryview(b'hello')))

print(type(None))
print(type(...))


# Add to END (like JS push)
fruits = ["apple", "banana"]
fruits.append("cherry")  # Same as push
print(fruits)  # ['apple', 'banana', 'cherry']

# Insert at POSITION (like splice)
fruits.insert(1, "orange")  # Insert at index 1
print(fruits)  # ['apple', 'orange', 'banana', 'cherry']

# Insert at beginning
fruits.insert(0, "grape")
print(fruits)  # ['grape', 'apple', 'orange', 'banana', 'cherry']


# Starting list
fruits = ["apple", "banana"]
print("Original:", fruits)

# 1. append() → Add SINGLE item to END
fruits.append("cherry")
print("After append():", fruits)  
# ['apple', 'banana', 'cherry']

# 2. insert(index, item) → Add at SPECIFIC POSITION
fruits.insert(1, "orange")  # Insert at index 1
print("After insert(1, 'orange'):", fruits)
# ['apple', 'orange', 'banana', 'cherry']

# 3. pop(index=-1) → Remove & RETURN last item (or by index)
last_fruit = fruits.pop()  # Removes last
print("Popped:", last_fruit)     # 'cherry'
print("After pop():", fruits)    # ['apple', 'orange', 'banana']

second_fruit = fruits.pop(1)     # Remove index 1
print("Popped index 1:", second_fruit)  # 'orange'
print("After pop(1):", fruits)   # ['apple', 'banana']

# 4. remove(value) → Remove FIRST occurrence by VALUE
fruits.remove("banana")
print("After remove('banana'):", fruits)
# ['apple']

# 5. extend(iterable) → Add MULTIPLE items from another list
more_fruits = ["grape", "mango"]
fruits.extend(more_fruits)
print("After extend():", fruits)
# ['apple', 'grape', 'mango']

text = "   hello world   "
clean = text.strip()  # Removes spaces from start + end
print(clean)  # "hello world"

text2 = "***python**"
clean2 = text2.strip("*")  # Removes * from both ends
print(clean2)  # "python"


text = "hello world hello python"
count_hello = text.count("hello")  # How many "hello"?
print(count_hello)  # 2

text2 = "banana"
a_count = text2.count("a")  # Count letter 'a'
print(a_count)  # 3




from collections import Counter

text = "hello world"
counter = Counter(text)
print(counter)  # Counter({'l' : 3, 'o': 2, 'h': 1, 'e': 1, ...})

# Most common
print(counter.most_common(2))  # [('l', 3), ('o', 2)]



email = "  user@example.com  "
clean_email = email.strip()  # "user@example.com"

# Count '@' symbols (should be 1)
at_count = clean_email.count("@")
print(f"Valid email: {at_count == 1}")  # True

# Character frequency
char_count = Counter(clean_email)
print(f"Length: {len(clean_email)}, Chars: {char_count}")

x = 10
print(x)  # 10

del x
#print(x)  # NameError: name 'x' is not defined


fruits = ["apple", "banana", "cherry", "date"]

# Delete by index
del fruits[1]  # Remove "banana"
print(fruits)  # ['apple', 'cherry', 'date']

# Delete by slice (multiple items)
del fruits[1:3]  # Remove index 1 to 2
print(fruits)  # ['apple']


user = {"name": "Taaher", "age": 25, "city": "Chennai"}

del user["city"]
print(user)  # {'name': 'Taaher', 'age': 25}

my_list = [1, 2, 3]
del my_list
# print(my_list)  # NameError!

my_dict = {"a": 1}
del my_dict

import threading
import time

def task(name, duration):
    print(f"Task {name} started")
    time.sleep(duration)  # Simulate work
    print(f"Task {name} finished")

# Create threads
t1 = threading.Thread(target=task, args=("A", 2))
t2 = threading.Thread(target=task, args=("B", 3))

# Start threads (they run concurrently)
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()
print("All tasks done!")


import threading
import time

def download_file(file_name, size_mb):
    print(f"Starting download: {file_name} ({size_mb}MB)")
    time.sleep(size_mb)  # Simulate download
    print(f"✅ {file_name} downloaded!")

files = [("doc1.pdf", 2), ("img.jpg", 5), ("video.mp4", 3)]

# Create & start threads
threads = []
for file_name, size in files:
    t = threading.Thread(target=download_file, args=(file_name, size))
    t.start()
    threads.append(t)

# Wait for all downloads
for t in threads:
    t.join()

print("All downloads complete!")

"""
❌ CPU-heavy tasks = Multithreading SLOW (GIL blocks)
✅ I/O tasks (files, network, database) = Multithreading FAST
✅ For CPU tasks → Use multiprocessing instead
✅ Use threading for: Downloads, API calls, file I/O
❌ Don't use for: Math calculations, image processing
✅ Always use join() to wait for threads
"""



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


