

def return_even(list):
    if len(list) <= 0  :
        raise ValueError("list cannot be empty")
    f = [x for x in list if x %2==0 ]
    return f



def return_prime(list):
    prime_list=[]
    if len(list) <= 0:
        raise ValueError("list cannot be empty")
    
    for x in list:
        if x <= 1:
            continue

        
        for i in range(2,int(x**0.5)+1):
            if  x % i == 0:
              break
              
        else:
            prime_list.append(x)
    

    return prime_list       


# numbers.py

def get_even_numbers(nums):
    """Return a list of even numbers from the given list."""
    return [n for n in nums if n % 2 == 0]

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_numbers(nums):
    """Return a list of prime numbers from the given list."""
    return [n for n in nums if is_prime(n)]




if __name__ == "__main__":
    sample_list =[15,5,78,1,2,3,4,5,6,7,8,9,14,16]
    print(return_even(sample_list))
    print(return_prime(sample_list))

"""# numbers.py

def get_even_numbers(nums):
    
    return [n for n in nums if n % 2 == 0]

def is_prime(n):
    
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_numbers(nums):
    
    return [n for n in nums if is_prime(n)]
"""


"""

def isprime(list):
    prime_l=[]
    if len(list) == 0:
        raise ValueError("list cannot be empty!")
    


    for x in list:
        if x <=1:
            continue


        for i in range(2,int(x**0.5)+1):
           
           if x % i == 0:
                     break
        else:
            prime_l.append(x)

    return prime_l

print(isprime(sample_list))
"""