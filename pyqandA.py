print("this a new project")


print("today im going to complete this work ",end="")
print("in here",)
print("client's name : ",end="")
print("arshad","azeez","hidayath","syed","mubarak","ameenudeen",sep=" *** ")

numbers = [10, 90, 20, 10, 30, 40, 20, 50, 60, 30, 70]

# Remove duplicates using set and dict()


#unique_numbers = set(numbers)
unique_numbersdic = list(dict.fromkeys(numbers))
unique_numbersset = list(set(numbers))
b = list(sorted(unique_numbersset))
c = b.reverse()
print(unique_numbersdic,unique_numbersset,b,c)




newtuple = (23,9,36,748,57487,4585,4874,)

print(newtuple[:4])



num = int(input("Enter a number: "))

print(f"Divisors of {num} are:")


# Loop through all numbers from 1 to num


for i in range(1, num + 1):
    if num % i == 0:
        print(i)

num = int(input("Enter a number: "))

# Separate and display each digit
for digit in str(num):
    print(digit)

for num in range(29, 0, -2):
    print(num)    


for nu in range(1, 29+1, +2):
    print(nu)        


