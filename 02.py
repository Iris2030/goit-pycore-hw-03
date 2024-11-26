import random

def get_numbers_ticket(min_val, max_val, quantity):
    # Ensure quantity does not exceed the possible number of unique values in the range
    if quantity > (max_val - min_val + 1):
        raise ValueError("Quantity of numbers requested exceeds the available range.")

    # Generate 'quantity' unique numbers in the range from 'min_val' to 'max_val'
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    
    print(sorted(numbers))
    return sorted(numbers)

# Example usage
get_numbers_ticket(2, 800, 6)

# Negative example usage
get_numbers_ticket(2, 50, 51)