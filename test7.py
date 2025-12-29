

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
