import os
import base64
import hashlib
from cryptography.fernet import Fernet

# Generate a secure encryption key from a password
def generate_key(password):
    hashed = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

# Encrypt a file
def encrypt_file(filename, password):
    key = generate_key(password)
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = cipher.encrypt(data)

    encrypted_file = filename + ".vault"

    with open(encrypted_file, "wb") as file:
        file.write(encrypted)

    print("\nFile encrypted successfully.")
    print("Encrypted File:", encrypted_file)

# Decrypt a file
def decrypt_file(filename, password):
    key = generate_key(password)
    cipher = Fernet(key)

    try:
        with open(filename, "rb") as file:
            encrypted = file.read()

        decrypted = cipher.decrypt(encrypted)

        output = filename.replace(".vault", "_decrypted.txt")

        with open(output, "wb") as file:
            file.write(decrypted)

        print("\nFile decrypted successfully.")
        print("Output File:", output)

    except Exception:
        print("\nWrong password or corrupted file.")

# Main menu
while True:

    print("\n======================================")
    print(" CRYPTOGRAPHIC ENCRYPTION VAULT ")
    print("======================================")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        filename = input("Enter file name: ")

        if not os.path.exists(filename):
            print("File not found.")
            continue

        password = input("Enter encryption password: ")

        encrypt_file(filename, password)

    elif choice == "2":

        filename = input("Enter encrypted file: ")

        if not os.path.exists(filename):
            print("Encrypted file not found.")
            continue

        password = input("Enter password: ")

        decrypt_file(filename, password)

    elif choice == "3":
        print("Thank you for using Encryption Vault.")
        break

    else:
        print("Invalid choice.")
