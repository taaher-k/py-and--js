
from numaric import calculate_power, calculate_maximum

def main():
    base = float(input("Enter base value: "))
    exponent = int(input("Enter exponent value: "))
    print(f"{base}^{exponent} = {calculate_power(base, exponent)}")

    nums = list(map(float, input("Enter numbers separated by space: ").split()))
    print("Maximum value:", calculate_maximum(nums))

if __name__ == "__main__":
    main()
