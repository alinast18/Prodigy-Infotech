# Caesar Cipher Program

def caesar_encrypt(message, shift):
    """
    Encrypts a message using the Caesar Cipher algorithm.

    :param message: The message to encrypt
    :param shift: The shift value to use for encryption
    :return: The encrypted message
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    """
    Decrypts a message using the Caesar Cipher algorithm.

    :param encrypted_message: The message to decrypt
    :param shift: The shift value to use for decryption
    :return: The decrypted message
    """
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def main():
    message = input("Enter a message: ")
    shift = int(input("Enter a shift value: "))

    encrypted_message = caesar_encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = caesar_decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
