import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars, special_chars):
    characters = ''
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += special_chars

    if not characters:
        return "No character types selected for password generation."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("Enter the desired password length: "))
    amnt_str = input("Enter how many you want: ")
    amount = int(amnt_str)
    use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Use digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Use special characters? (y/n): ").lower() == 'y'

    special_chars = "!@#$%^&*()_+[]{}|;:'\",.<>?/\\"
    if use_special_chars:
        special_chars = input("Enter the special characters to use: ")

    for x in range(amount):
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars, special_chars)
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
