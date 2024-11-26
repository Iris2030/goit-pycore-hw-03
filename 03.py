import re
ready_to_send_numbers = []  # List to store normalized numbers

def normalize_phone(phone_number):
    # Remove all characters except digits and plus sign
    stripped_number = re.sub(r"[^\d+]", "", phone_number.strip())

    # If the number starts with "+", but not "+38"
    if stripped_number.startswith("+"):
        if not stripped_number.startswith("+38"):
            return stripped_number
    # If the number starts with "38", add "+"
    elif stripped_number.startswith("38"):
        stripped_number = "+" + stripped_number
    # If the number does not contain the country code
    else:
        stripped_number = "+38" + stripped_number
    
    # Optional check for the length of the number 
    if len(stripped_number) != 13:
        raise ValueError("The phone number has wrong format. Fix it and try again.")
    else:
        ready_to_send_numbers.append(stripped_number)
    
    return ready_to_send_numbers  # Return the list of normalized numbers

# Test cases
print(normalize_phone("    +38(050)123-32-34"))  # ['+380501233234']
print(normalize_phone("     0503451234"))        # ['+380503451234']
print(normalize_phone("(050)8889900"))           # ['+380508889900']
print(normalize_phone("38050-111-22-22"))        # ['+380501112222']
print(normalize_phone("38050 111 22 11   "))     # ['+380501112211']
print(normalize_phone("   +44(123)456-78-90"))   # ['+441234567890']
print(normalize_phone("38050 111 22 11  77 "))   # ValueError: The phone number has wrong format. Fix it and try again.
print(normalize_phone("38050 111 22 1"))         # ValueError: The phone number has wrong format. Fix it and try again.