import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."

    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
