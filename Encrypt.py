import random

messages = ''
public_key = ''
private_key = ''
private_space = ''

def create_private_key():
    global private_key
    private_key = random.randint(3, 30)
    print("---------------------------")
    print("Din private key:", private_key)


def create_public_key():
    global message
    print("Skriv inn meldingen din her:")
    message = input('')
    print(message)

    numbers = []
    for char in message:
        numbers.append("a")
        if char.isalpha():
            numbers.append((ord(char.upper()) - ord('A') + 1) * private_key)
            numbers.append("a")
        elif char.isspace(): 
            numbers.append("S")
        else:
            numbers.append(char)

    numbers_str = ''.join(str(num) for num in numbers if num is not None)
    return numbers_str

create_private_key()
print(create_public_key())
print("---------------------------")