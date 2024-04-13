def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

def main():
    while True:
        print("\nMenu:")
        print("1. Encode Password")
        print("2. Decode Password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            password = input("Enter the password to encode (8 digits): ")
            if len(password) != 8 or not password.isdigit():
                print("Invalid input. Password must be 8 digits.")
            else:
                encoded_password = encode(password)
                print("Encoded Password:", encoded_password)

        elif choice == "2":
            encoded_password = input("Enter the encoded password (8 digits): ")
            if len(encoded_password) != 8 or not encoded_password.isdigit():
                print("Invalid input. Encoded password must be 8 digits.")
            else:
                decoded_password = decode(encoded_password)
                print("Decoded Password:", decoded_password)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
    
