import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    all_characters = letters + digits + special_chars
    password = ''
    
    while True:
        password = ''.join(random.choice(all_characters) for _ in range(length))
        if (any(char in special_chars for char in password) and
            sum(char in digits for char in password) >= 2):
            return password

password_length = int(input("Enter the desired length for your password: "))
print("Generated Password:", generate_password(password_length))

