import random

message = ''
public_key = ''
private_key = ''
private_space = ''

def create_private_key():
    private_key = random.randint(3, 30)
    print("Din private key: ",  private_key)
    

def create_public_key():
    print("Skriv inn meldingen din her:")
    message = input('')

    numbers = []
    for char in message:
            if char.isalpha():
                numbers.append(ord(char.upper()) - ord('A') + 1)
            elif char.isspace(): 
                numbers.append("Space")
            else:
                numbers.append(None)
    return numbers
    
    print(numbers)


create_private_key()
print(create_public_key())
