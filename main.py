def main():
    def encode(password: str) -> str:
        if len(password) != 8 or not password.isdigit():
            raise ValueError("The password must be an 8-digit integer string.")

        encoded_password = ''.join([str((int(digit) + 3) % 10) for digit in password])
        return encoded_password
    pass

if __name__ == "__main__":
    main()
    password = input("Enter 8-digit password: ")
    encoded = encode(password)
    decoded = decode(password)
    print(f"Original Password: {password}")
    print(f"Encoded Password: {encoded}")
    print(f"Decoded Password: {decoded}")
#changes
