

import os

try:
    # Step 1: Read input from user
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")
    hobby = input("Enter your hobby: ")

    # Step 2: Check if file already exists
    if os.path.exists("userinfo.txt"):
        raise FileExistsError("The file 'userinfo.txt' already exists!")

    # Step 3: Create and write to file
    file = open("userinfo.txt", "w")
    file.write(f"Name: {name}\n")
    file.write(f"Gender: {gender}\n")
    file.write(f"Hobby: {hobby}\n")

    print("User information saved successfully!")

except FileExistsError as e:
    print(e)

finally:
    # Step 4: Close the file safely
    try:
        file.close()
    except NameError:
        # File was never opened
        pass




try:
    # Step 1: Read 5 integers and store in a list
    numbers = []
    for i in range(5):
        try:
            num = int(input(f"Enter integer {i+1}: "))
            numbers.append(num)
        except ValueError:
            raise ValueError("Invalid input! Please enter integers only.")

    # Step 2: Read 2 positions between 0 and 4
    try:
        pos1 = int(input("Enter first position (0-4): "))
        pos2 = int(input("Enter second position (0-4): "))
    except ValueError:
        raise ValueError("Invalid input! Positions must be integers.")

    # Step 3: Validate positions
    if not (0 <= pos1 < 5 and 0 <= pos2 < 5):
        raise IndexError("Positions must be between 0 and 4.")

    # Step 4: Fetch numbers and calculate product
    num1 = numbers[pos1]
    num2 = numbers[pos2]
    product = num1 * num2

    print(f"Numbers at positions {pos1} and {pos2} are {num1} and {num2}.")
    print(f"Their product is: {product}")

except Exception as e:
    print("Error:", e)








# the try block only execute when the try does'nt have any except:



try:
    # Step 1: Get two integers from the user
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    # Step 2: Perform division
    result = num1 / num2
    print(f"The result of {num1} / {num2} is: {result}")

# Handle invalid input (non-integer values)
except ValueError:
    print("Error: Please enter valid integers only.")

# Handle division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Catch any other unexpected errors
except Exception as e:
    print("Unexpected error:", e)




# for the custom exception we need to add the class as the name of the custom error

class NegativeError(Exception):
    pass



while True:
  
  try :

   age =  int(input("enter your age"))
   if age <=0:
      raise NegativeError(" the age value cant be in negative ")

   if age >= 18:
       print("your eligible to vote ")
   else:
       print("your not eligible to vote")
       
   break
  
  except ValueError:
    print(" age must be an integer ")

    
  except NegativeError as e:
        
        print("error",e)


try:
    # Step 1: Read input from user
    num = int(input("Enter a number: "))

    # Step 2: Calculate cube
    cube = num ** 3

except ValueError:
    # Step 3: Handle invalid input
    print("Error: Please enter a valid integer.")

else:
    # Step 4: Executed only if no exception occurs
    print(f"The cube of {num} is {cube}")













# Step 1: Define custom exceptions
class InvalidTransactionType(Exception):
    """Raised when transaction type is not withdraw or deposit."""
    pass

class InvalidWithdrawAmount(Exception):
    """Raised when withdraw amount is not in hundreds or exceeds limit."""
    pass


# Step 2: Initialize account balance
balance = 50000

try:
    # Step 3: Read transaction type and amount
    transaction_type = input("Enter transaction type (withdraw/deposit): ").strip().lower()
    amount = int(input("Enter transaction amount: "))

    # Step 4: Validate transaction type
    if transaction_type not in ["withdraw", "deposit"]:
        raise InvalidTransactionType("Transaction type must be 'withdraw' or 'deposit'.")

    # Step 5: Handle withdraw
    if transaction_type == "withdraw":
        if amount % 100 != 0:
            raise InvalidWithdrawAmount("Withdraw amount must be in multiples of 100.")
        if amount > 25000:
            raise InvalidWithdrawAmount("Withdraw amount cannot exceed 25000.")
        if amount > balance:
            raise InvalidWithdrawAmount("Insufficient balance for withdrawal.")

        balance -= amount
        print(f"✅ Withdrawal successful! New balance: {balance}")

    # Step 6: Handle deposit
    elif transaction_type == "deposit":
        balance += amount
        print(f"✅ Deposit successful! New balance: {balance}")

# Step 7: Exception handling
except ValueError:
    print("Error: Amount must be an integer.")

except InvalidTransactionType as e:
    print("Error:", e)

except InvalidWithdrawAmount as e:
    print("Error:", e)





"""
-- Find average salary per department
SELECT Dept, AVG(Salary) AS AvgSalary
FROM Employee
GROUP BY Dept;

-- List employees with more than 10 years of experience
SELECT Name, Dept, Exp, Salary
FROM Employee
WHERE Exp > 10;

-- Find highest paid employee in each location
SELECT Location, Name, MAX(Salary) AS MaxSalary
FROM Employee
GROUP BY Location;


this code will print employee name in ascending order

SELECT Name
FROM Employee
ORDER BY Name ASC;



"""