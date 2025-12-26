c = "1 684 456 684 786 64"


cl = c.split(" ")

inrlist = [int(x)for x in cl ]

print(type(inrlist))
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

strt = "mom"

def pal(x):
    if not x:
        raise ValueError("cannot be empty")
    x = x.replace(" ","").lower()

    if x == x[::-1]:
        return True
    else:
         False  


print(f"{pal(strt)}")



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
text = "`hello world, hello python"  
print(find_and_replace(text, "hello", "hi"))






def rp(current_value,search_val,rp_val):
    out = ""
    x = 0

    while x  < len(current_value): #range 0 to len(current_value)

        match = True
        
        for i in range(len(search_val)):   #range 0 to len(search_val)

            if x + i >= len(current_value) or current_value[x+i] != search_val[i]: 
            #count + i >= en(current_value) or current_value[count+i] != search_val[i]

                match = False
                break
         
        if match:
            out += rp_val          #important string will not support .append so we use += .append is a list attribute
            x += len(search_val)
        else:

            out += current_value[x]
            x += 1
    return out

sample_string = "hi taaher how are you"
sample_string2 ="taaher just start it "

print(rp(sample_string,"taaher","khan"))
print(rp(sample_string2,"taaher","khan"))



def represent_powers(n):
    results = []
    for base in range(2, n):
        exp = 2
        value = base ** exp

        while value <= n:

            if value == n:
                results.append(f"{base}^{exp}")
                break
            exp += 1
            value = base ** exp

    return results if results else "false"
print(represent_powers(64))  # ['2^6', '4^3', '8^2']
print(represent_powers(20))  # FLASE


strrr = "hi hello how are you who are where are you!?"
def faodd(x):
    for i in range (1,len(x),+2):

        print(strrr[i]," ",end="")

faodd(strrr)


print()

for x in range (0,100):
    if x %2 !=0:
        print(x," ",end="")



def is_niven(n):

        digit_sum = sum(int(d) for d in str(n))
        if n % digit_sum == 0:   # divisible check
         return True
        else:
         return False

print(is_niven(18))  # True
print(is_niven(15))  # False






def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(lst):
    primes = []
    for x in lst:
        if is_prime(x):
            primes.append(x)
    return primes

# Example usage
numbers = [10, 2, 3, 4, 5, 15, 17, 20, 23]
print(filter_primes(numbers))  # Output: [2, 3, 5, 17, 23]


"""#3

#1


def fibonacci_upto(limit):
    a, b = 0, 1
    fib_list = []
    while a <= limit:
        fib_list.append(a)
        a, b = b, a + b   # update values
    
    p = len(fib_list)-1

    if fib_list[p]==limit:
            return "its a fibonacci"
    else:
            return "not a fibonacci"


num = int(input("enter any number to check its fibonacci or not"))
print(fibonacci_upto(num))



#2
def fibonacci_upto(limit):
    a, b = 0, 1
    fib_list = []
    while a <= limit:
        fib_list.append(a)
        a, b = b, a + b   # update values
    
    if limit in fib_list:   # check membership in the whole list
        return "its a fibonacci"
    else:
        return "not a fibonacci"

num = int(input("enter any number to check its fibonacci or not: "))
print(fibonacci_upto(num))


"""

"""#Find the Factorial of a given number.


def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

# Example
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")"""

