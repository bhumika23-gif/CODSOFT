import random
import string

# Step 1: User Input
length = int(input("Enter desired password length: "))

# Step 2: Define characters (letters, digits, punctuation)
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Step 4: Display password
print("Generated Password:", password)