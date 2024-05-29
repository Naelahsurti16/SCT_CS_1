def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))
        if choice == 'e':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        else:
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")

        another = input("Do you want to process another message? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
