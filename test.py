import random

messages = ''
public_key = ''
private_key = ''
private_space = ''

def create_private_key():
    global private_key
    private_key = random.randint(1, 2)
    print("---------------------------")
    print("Din private key:", private_key)


def create_public_key():
    global messages, private_key
    print("Skriv inn meldingen din her:")
    message = input('')
    encrypted_message = caesar_cipher(message, private_key)
    return encrypted_message

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26) + ord('a' if char.islower() else 'A'))
            result += shifted_char
        else:
            result += char
    return result

create_private_key()
print(create_public_key())
print("---------------------------")
