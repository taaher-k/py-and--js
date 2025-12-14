def collect_marks():
    y = []
    count = 1

    # Keep asking until a valid integer for subjects is entered
    while True:
        try:
            subject = int(input("Enter number of subjects: "))
            if subject <= 0 or subject > 100:
                print("Number of subjects must be greater than 0 and lesser than 100 Try again.")
                continue
            break   # valid input, exit loop
        except ValueError:
            print("Invalid input! Please enter a valid integer for number of subjects.")

    # Now collect marks for each subject
    for x in range(subject):
        while True:  # keep asking until valid marks are entered
            try:
                marks = int(input(f"Enter your marks for subject {count}: "))
                if marks < 0 or marks > 100:
                    print("Marks should be between 0 and 100. Try again.")
                    continue
                
                y.append(marks)
                #y = [*y, marks]  # using unpacking to add marks to the list
                #y += [marks]  # another way to add marks to the list
                
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer for marks.")
        count += 1

    print(f"Your marks are: {y}")
    return y   # return the list so you can use it later


# Example usage
marks_list = collect_marks()

if marks_list:  # only calculate average if list is not empty
    def find_average_list(numbers):
        return sum(numbers) / len(numbers)

    print(f"Your average marks are: {find_average_list(marks_list)}")
