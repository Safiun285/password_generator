import random
import string

def generate_password(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = uppercase + lowercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

def main():
    print("🔐 Secure Password Generator 🔐")
    try:
        length = int(input("Enter password length (minimum 8): "))
    except ValueError:
        print("❌ Please enter numbers only")
        return

    password = generate_password(length)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
