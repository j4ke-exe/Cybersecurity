import string
import random

# Define a function to check the password complexity
def check_complexity(password):
    # Initialize the complexity counter
    complexity = 0

    # Check if the password contains lowercase letters
    if any(char.islower() for char in password):
        complexity += 1

    # Check if the password contains uppercase letters
    if any(char.isupper() for char in password):
        complexity += 1

    # Check if the password contains digits
    if any(char.isdigit() for char in password):
        complexity += 1

    # Check if the password contains punctuation characters
    if any(char in string.punctuation for char in password):
        complexity += 1

    # Return the password complexity
    return complexity

# Prompt the user for the password length and complexity level
length = int(input("Enter the password length: "))
complexity = int(input("Enter the password complexity (1-4): "))

# Generate a random password of the specified length
password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

# Check the password complexity
password_complexity = check_complexity(password)

# Keep generating new passwords until the desired complexity level is reached
while password_complexity < complexity:
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_complexity = check_complexity(password)

# Print the generated password
print(f"Your password is: {password}")
