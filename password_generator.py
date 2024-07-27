import random
import string

def password_generator():
    print("Password Generator")

    length = int(input("Enter the desired length of the password: "))

    if length < 8:
        print("Password length should be at least 8 characters.")
        return

    print("Select password complexity:")
    print("1. Low (letters only)")
    print("2. Medium (letters and numbers)")
    print("3. High (letters, numbers, and special characters)")

    complexity = input("Enter your choice (1/2/3): ")

    if complexity == '1':
        characters = string.ascii_letters
    elif complexity == '2':
        characters = string.ascii_letters + string.digits
    elif complexity == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice.")
        return

    password = ''.join(random.choice(characters) for i in range(length))
    print("Generated Password:", password)

password_generator()
