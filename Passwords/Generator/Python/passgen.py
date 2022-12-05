import string
import random

# Prompt the user for the password length
length = int(input("Enter the password length: "))

# Generate a random password of the specified length
password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

# Print the generated password
print(f"Your password is: {password}")
