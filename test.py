import random

messages = ''
public_key = ''
private_key = ''
private_space = ''

def create_private_key():
    global private_key
    private_key = random.randint(3, 30)
    print("Din private key:", private_key)
    print("test")


def create_public_key():
    print("Skriv inn meldingen din her:")
    message = input('')

    numbers = []
    for char in message:
        if char.isalpha():
            numbers.append(ord(char.upper()) - ord('A') + 1)
            numbers.append("a")
        elif char.isspace(): 
            numbers.append("S")
        else:
            numbers.append(None)

    numbers_str = ''.join(str(num) for num in numbers if num is not None)
    return numbers_str

print(create_private_key())

while True:
    print(create_public_key())

