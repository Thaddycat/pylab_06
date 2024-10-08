def vigenere_sq():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    header = "|   | " + " | ".join(alphabet) + " |"
    print(header)
    print("|---" + "|---" * len(alphabet) + "|")
    for i in range(len(alphabet)):
        # Start each row with the corresponding letter
        row = f"| {alphabet[i]} | "
        for j in range(len(alphabet)):
            # Calculate the shifted letter
            shifted_letter = alphabet[(i + j) % len(alphabet)]
            row += f"{shifted_letter} | "
        print(row)

def letter_to_index(letter, alphabet):
    return alphabet.index(letter)

def index_to_letter(index, alphabet):
    return alphabet[index]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    ciphertext_index = (plaintext_index + key_index) % len(alphabet)
    return index_to_letter(ciphertext_index, alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    encrypted_text = ""
    key_length = len(key)
    for i, letter in enumerate(plaintext):
        if letter in alphabet:
            key_index = i % key_length
            key_letter = key[key_index]
            ciphertext_letter = vigenere_index(key_letter, letter, alphabet)
            encrypted_text += ciphertext_letter
        else:
            encrypted_text += letter
    return encrypted_text

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)
    plaintext_index = (cipher_index - key_index) % len(alphabet)
    return index_to_letter(plaintext_index, alphabet)

def decrypt_vigenere(key, cipher_text, alphabet):
    decrypted_text = ""
    key_length = len(key)
    for i, letter in enumerate(cipher_text):
        if letter in alphabet:
            key_index = i % key_length
            key_letter = key[key_index]
            plaintext_letter = undo_vigenere_index(key_letter, letter, alphabet)
            decrypted_text += plaintext_letter
        else:
            decrypted_text += letter
    return decrypted_text

def vig_app():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. EXIT")
        try:
            choice = input("Select an option (1-3): ")
            if choice == "1":
                plaintext = input("Enter plaintext: ").upper()
                key = input("Enter key: ").upper()
                encrypted_message = encrypt_vigenere(key, plaintext, alphabet)
                print(f"Encrypted Message: {encrypted_message}")
            elif choice == "2":
                cipher_text = input("Enter ciphertext: ").upper()
                key = input("Enter key: ").upper()
                decrypted_message = decrypt_vigenere(key, cipher_text, alphabet)
                print(f"Decrypted Message: {decrypted_message}")
            elif choice == "3":
                print("Exiting the program.")
                vigenere_sq()
                break
            else:
                print("Invalid option. Please select again.")
        except KeyboardInterrupt:
                print("\nProgram interrupted. Exiting...")
                vigenere_sq()
                break


vig_app()