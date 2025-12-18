
import numbers

list_base =[2,3,6,45,6,8,9,5,64,965,784,8,5,4]

print(f"all the even numbers from the list is: {numbers.return_even(list_base)}")
print(f"all the prime numbers from the list is: {numbers.return_prime(list_base)}")


def main():
    # Read list of numbers from user
    #nums = list(map(int, input("Enter numbers separated by space: ").split()))
    numsc = input("e").split()
    print(numsc)
    nums = [int(x) for x in numsc ]





    # Get even numbers
    evens = numbers.get_even_numbers(nums)
    print("Even numbers:", evens)

    # Get prime numbers
    primes = numbers.get_prime_numbers(nums)
    print("Prime numbers:", primes)

if __name__ == "__main__":
    main()

name = "ta aher"
print(name)
print(name.split(" "))
b ="".join(name)
print("".join(name))