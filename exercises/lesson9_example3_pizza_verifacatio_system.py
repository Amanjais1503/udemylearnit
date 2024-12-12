# Pizza Order Verification System
# Follow these TODO steps to complete the exercise!

# Problem Description:
# You are working as a developer for "Python Pizza Palace". They need a system
# to verify customer orders against receipt numbers. The system should take two inputs
# from the customer (number of slices and price per slice) and check if their
# multiplication matches the receipt number stored in the system.

# TODO 1: Create a variable called 'receipt_number' and assign it any four-digit number
# Hint: This will be the number that customers need to match with their order details
receipt_number = None  # Replace None with your number

# TODO 2: Create an input statement to get the number of pizza slices from the customer
# Hint: Remember to convert the input to an integer using int()
# Hint: Use a descriptive prompt message for the customer

# TODO 3: Create another input statement to get the price per slice
# Hint: Similar to TODO 2, remember to convert to integer
# Hint: Use clear prompt message

# TODO 4: Calculate the total by multiplying slices with price_per_slice
# Hint: Create a variable to store the result of multiplication

# TODO 5: Compare the calculated total with receipt_number and print the result
# Hint: Use the == operator for comparison
# Hint: This should print True if they match, False if they don't

# BONUS TODO 6: Add error handling for invalid inputs
# Hint: What happens if someone enters "abc" instead of a number?
# Hint: Look into try/except blocks

# Test your code with these cases:
# Test Case 1: If receipt_number is 2468
#   - Input 26 slices and 95 per slice
#   - Expected output: True (because 26 * 95 = 2470)
#
# Test Case 2: If receipt_number is 2468
#   - Input 28 slices and 88 per slice
#   - Expected output: False (because 28 * 88 = 2464)