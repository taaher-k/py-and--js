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


