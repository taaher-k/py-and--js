

def zero_one_pattern(rows):
    for i in range(1, rows+1):
        pattern = ""
        for j in range(1, i+1):
            if j % 2 == 1:   # odd position → 1
                pattern += "1"
            else:            # even position → 0
                pattern += " 0 "
        print(pattern)

# Example: 5 rows
zero_one_pattern(5)


rows = 5

for i in range(1, rows+1):                 # Outer loop → controls rows
    # Print spaces before stars
    for j in range(rows-i):
        print(" ", end=" ")
    
    # Print stars
    for k in range(2*i-1):
        print("*", end=" ")
    
    print()                                # Move to next line




#2


for i in range(1,10):
    for j in range (i,10):
        print(" ",end=" ")
    for k in range(1,i+1):
        print (" * ",end=" " )
    print()       


    
    #ijjjjjkkkkk
    #ijjjjjkkkkk
    #ijjjjjkkkkk
    #ijjjjjkkkkk
    #ijjjjjkkkkk
    

    """def file_statistics(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()

        # Count characters (including spaces and newlines)
        char_count_all = len(content)

        # Count characters excluding spaces and newlines
        char_count_filtered = len([ch for ch in content if ch not in [" ", "\n"]])

        # Count words (split by whitespace)
        word_count = len(content.split())

        # Count lines
        line_count = len(content.splitlines())

        print(f"File: {filename}")
        print(f"Characters (all): {char_count_all}")
        print(f"Characters (excluding spaces/newlines): {char_count_filtered}")
        print(f"Words: {word_count}")
        print(f"Lines: {line_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
file_statistics("test.txt")
"""

"""
def remove_vowels_from_file(input_file, output_file):
    try:
        # Read original content
        f_in = open(input_file, "r")
        content = f_in.read()
        f_in.close()

        # Define vowels
        vowels = "aeiouAEIOU"

        # Count vowels removed
        removed_count = sum(1 for ch in content if ch in vowels)

        # Remove vowels
        filtered_content = "".join(ch for ch in content if ch not in vowels)

        # Write filtered content to output file
        f_out = open(output_file, "w")
        f_out.write(filtered_content)
        f_out.close()

        # Show comparison
        print("=== Original Content ===")
        print(content)
        print("\n=== Content Without Vowels ===")
        print(filtered_content)
        print(f"\nVowels removed: {removed_count}")
        print(f"Result written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
remove_vowels_from_file("input.txt", "output.txt")


#filtered_content = "".join(ch for ch in content if ch not in vowels)
#filtered_content = ""
#for ch in content:
#    if ch not in vowels:
#        filtered_content += ch
#
"""
"""import re
filtered_content = re.sub(r"[aeiouAEIOU]", "", content)
"""

"""🔍 Explanation
re.sub(pattern, replacement, string)

pattern → what you want to match (here, vowels).

replacement → what you want to put instead (here, "", meaning nothing).

string → the text you’re processing (content)."""

import csv

def store_user_info():
    # Read user input
    username = input("Enter your name: ")
    email = input("Enter your email: ")
    mobile = input("Enter your mobile number: ")
    dob = input("Enter your date of birth (DD-MM-YYYY): ")

    # File name
    filename = "userinfo.csv"

    try:
        # Open CSV file in append mode
        f = open(filename, "a", newline="")
        writer = csv.writer(f)

        # Write header only if file is empty
        if f.tell() == 0:
            writer.writerow(["Name", "Email", "Mobile", "DOB"])

        # Write user info
        writer.writerow([username, email, mobile, dob])
        f.close()

        print(f"User information stored in {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the function
store_user_info()
"""import csv

def store_multiple_users():
    filename = "userinfo.csv"

    try:
        # Open CSV file in append mode
        f = open(filename, "a", newline="")
        writer = csv.writer(f)

        # Write header only if file is empty
        if f.tell() == 0:
            writer.writerow(["Name", "Email", "Mobile", "DOB"])

        while True:
            # Ask for user input
            username = input("Enter your name (or type 'exit' to stop): ")
            if username.lower() == "exit":
                break

            email = input("Enter your email: ")
            mobile = input("Enter your mobile number: ")
            dob = input("Enter your date of birth (DD-MM-YYYY): ")

            # Write user info into CSV
            writer.writerow([username, email, mobile, dob])
            print(f"User '{username}' stored successfully!\n")

        f.close()

        # ✅ Display all stored records
        print("\n=== All Stored Users ===")
        with open(filename, "r") as f_read:
            reader = csv.reader(f_read)
            for row in reader:
                print(row)

        print(f"\nAll user information stored in {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the function
store_multiple_users()
"""

import csv

def display_userinfo():
    filename = "userinfo.csv"

    try:
        # Open CSV file in read mode
        f = open(filename, "r")
        reader = csv.reader(f)

        print("=== User Information ===")
        for row in reader:
            print(row)

        f.close()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the function
display_userinfo()

"""import csv

def store_subject_marks():
    filename = "marks.csv"

    try:
        # Open CSV file in write mode (fresh file each run)
        f = open(filename, "w", newline="")
        writer = csv.writer(f)

        # Write header row
        writer.writerow(["Subject", "Marks"])

        total_marks = 0

        while True:
            subject = input("Enter subject name (or type 'exit' to stop): ")
            if subject.lower() == "exit":
                break

            marks = int(input(f"Enter marks for {subject}: "))
            total_marks += marks

            # Write subject and marks into CSV
            writer.writerow([subject, marks])

        # Write total marks at the end
        writer.writerow(["Total", total_marks])

        f.close()
        print(f"All subject marks stored in {filename}")
        print(f"Total Marks = {total_marks}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the function
store_subject_marks()

"""

