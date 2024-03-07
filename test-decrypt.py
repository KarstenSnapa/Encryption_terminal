

import random

messages = ''
public_key = ''
private_key = ''
private_space = ''

def create_private_key():
    global private_key
    private_key = input("What is your private key?")
    print("---------------------------")
    print("Your private key:", private_key)


def create_public_key():
    global messages, private_key
    print("Enter your message here:")
    message = input('')
    encrypted_message = caesar_cipher(message, int(private_key))
    return encrypted_message

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result += shifted_char
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            result += shifted_char
        else:
            result += char
    return result

create_private_key()
encrypted_message = create_public_key()
print("Encrypted message:", encrypted_message)
print("Decrypted message:", caesar_decipher(encrypted_message, int(private_key)))
print("---------------------------")
