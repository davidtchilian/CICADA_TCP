def convert_to_base29(number):
    if number == 0:
        return '0'

    base29_digits = []
    while number > 0:
        number, remainder = divmod(number, 29)
        base29_digit = chr(ord('0') + remainder) if remainder < 10 else chr(ord('A') + remainder - 10)
        base29_digits.append(base29_digit)

    base29_digits.reverse()
    return ''.join(base29_digits)

# Example usage
number = 3301
base29 = convert_to_base29(number)
print(f"Number: {number}")
print(f"Base 29: {base29}")
