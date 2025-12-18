#Sort list items in ascending order.

lit = [9,8,7,45,6,1,56,63,21,1,2,1]

nums = [15, 5, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 16]

# Sort in ascending order
numh=sorted(nums)
print("Ascending order:", numh)


nums.sort()
print("Ascending order:", nums)


#2. Find maximum and second maximum number from a list.

nums = [15, 5, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 16]

# Sort in ascending order
sorted_nums = sorted(nums)

# Maximum is last element
maximum = sorted_nums[-1]

# Second maximum is second last element
second_maximum = sorted_nums[-2]

print("Maximum:", maximum)
print("Second Maximum:", second_maximum)


#fsdffsdfsdfdsfsd
nums = [15, 5, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 16]

maximum = max(nums)
nums.remove(maximum)   # remove the largest
second_maximum = max(nums)

print("Maximum:", maximum)
print("Second Maximum:", second_maximum)






nums = [15, 5, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 16]

# Bubble Sort
for i in range(len(nums)):
    for j in range(0, len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            # Swap
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Ascending order:", nums)






#Selection Sort (another approach)
nums = [15, 5, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 16]

for i in range(len(nums)):
    min_index = i
    for j in range(i+1, len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j
    # Swap
    nums[i], nums[min_index] = nums[min_index], nums[i]

print("Ascending order:", nums)


#

def reverse_words(sentence):
    # Split sentence into words
    words = sentence.split()
    # Reverse each word
    reversed_words = [word[::-1] for word in words]
    # Join back into a string
    return " ".join(reversed_words)

# Test
s = input("Enter a string: ")
print("Reversed words:", reverse_words(s))


#non rep 
nums = [15, 5, 78, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 16, 2, 9]

non_repeated = [n for n in nums if nums.count(n) == 1]
print("Non-repeated elements:", non_repeated)


#all pairs of sum in list 

def find_pairs(nums):
    pairs = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):   # avoid duplicate pairs
            s = nums[i] + nums[j]
            if s in nums:         # check if sum exists in list
                pairs.append((nums[i], nums[j], s))
    return pairs

# Test
nums = [15, 5, 78, 1, 2, 3, 4, 6, 7, 8, 9, 14, 16]
result = find_pairs(nums)

print("Pairs with sum present in list:")
for a, b, s in result:
    print(f"{a} + {b} = {s}")


#anagram
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare sorted characters
    return sorted(str1) == sorted(str2)

# Test
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if is_anagram(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
