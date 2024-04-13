# James Rolen

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
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print("\nMenu")
            print("-------------")

        elif choice == "2":
            encoded_password = input("Please enter the encoded password: ")
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            print("\nMenu")
            print("-------------")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
