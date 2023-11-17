def binary_to_decimal(binary):
    decimal_number = 0
    power = 0

    # Traverse the binary number from right to left
    for digit in reversed(binary):
        # Convert the digit to an integer
        digit = int(digit)
        # Calculate the decimal value of the digit and add it to the result
        decimal_number += digit * (2 ** power)
        # Increment the power for the next digit
        power += 1

    return decimal_number

# Example usage
binary_number = input("enter binary numbers:")
decimal_number = binary_to_decimal(binary_number)
print(decimal_number)
