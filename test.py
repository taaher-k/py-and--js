c = "1 684 456 684 786 64"


cl = c.split(" ")

intlist = [int(x)for x in cl ]

print(type(intlist))
print(type(c))
print(type(cl))



#


def reverse_words(sentence):
    # Split sentence into words
    words = sentence.split()
    # Reverse each word
    reversed_words = [word[::-1] for word in words]
    # Join back into a string
    return " ".join(reversed_words)

# Test
s = "hi  hello how are you"
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
        for j in range(i+1, n):   # important avoid duplicate pairs
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
    print(result)


#6.5
l=[3,5,1,8,9,11,48]
a=10
sum=0
print ("pair of numbers:")
for i in l:
    for j in l:
        if (i!=j):
            sum=i+j
            if (a==sum):
                print(i,j)




#all pairs of sum in list 

def find_pair(nums):
    pairs = []
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if (i!=j):   # add duplicate pairs also 
                s = nums[i] + nums[j]
                if s in nums:         # check if sum exists in list
                 pairs.append((nums[i], nums[j], s))
    return pairs

# Test
nums = [15, 5, 78, 1, 2, 3, 4, 6, 7, 8, 9, 14, 16]
result = find_pair(nums)

print("Pairs with sum present in list:")
for a, b, s in result:
    print(f"{a} + {b} = {s}")




#6.2
#anagram
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare sorted characters
    return sorted(str1) == sorted(str2)

# Test
s1 = "listen"
s2 = "silent"

if is_anagram(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


strings = ["apple", "banana", "cherry", "watermelon", "kiwi"]


def find_longest_string_from_a_list(x):
    longest = strings[0]
    for i in x:
        if len(i)> len(longest):
            longest = i
    return longest        
print(f"the longest number is in the list is {find_longest_string_from_a_list(strings)}")

str = "mom"

def pal(x):
    if not x:
        raise ValueError("cannot be empty")
    x = x.replace(" ","").lower()

    if x == x[::-1]:
        return True
    else:
         False  


print(f"{pal(str)}")



def find_and_replace(original, find_val, replace_val):
    result = ""
    i = 0
    
    while i < len(original):
        # Check if substring starting at i matches find_val
        match = True
        for j in range(len(find_val)):
            if i + j >= len(original) or original[i + j] != find_val[j]:
                match = False
                break
        
        if match:
            result += replace_val
            i += len(find_val)   # skip over the matched substring
        else:
            result += original[i]
            i += 1
    
    return result


# Example
text = "hello world, hello python"
print(find_and_replace(text, "hello", "hi"))
