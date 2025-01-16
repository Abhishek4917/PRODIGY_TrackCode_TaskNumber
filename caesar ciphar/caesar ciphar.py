def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a message using the Caesar Cipher algorithm.

    :param text: The input message to be processed
    :param shift: The shift value for the cipher
    :param mode: Mode of operation ('encrypt' or 'decrypt')
    :return: The processed message
    """
    if mode == 'decrypt':
        shift = -shift

    result = ''
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result

def main():
    print("Caesar Cipher Program")
    while True:
        mode = input("Enter mode (encrypt/decrypt/exit): ").strip().lower()
        if mode == 'exit':
            print("Goodbye!")
            break
        if mode not in ('encrypt', 'decrypt'):
            print("Invalid mode. Please enter 'encrypt', 'decrypt', or 'exit'.")
            continue

        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        result = caesar_cipher(message, shift, mode)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()
