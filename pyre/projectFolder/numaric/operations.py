




def calculate_power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent

def calculate_maximum(values):
    """Return the maximum value from a list of numbers."""
    if not values:
        raise ValueError("List of values cannot be empty.")
    return max(values)

listd=[1,2,3,56,8,8,4,8]

def calculate_max_value(values):
    if not values:
        raise ValueError("List of values cannot be empty.")
    max_value = 0
    for x in values:
        if x > max_value:
           max_value = x
    return max_value

if __name__ =="__main__":

  print(calculate_max_value(listd))

