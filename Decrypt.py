def decrypt_message(encrypted_message, private_key):
    decrypted_chars = []
    index = 0
    while index < len(encrypted_message):
        if encrypted_message[index] == 'a':
            # Extract the encrypted character value
            encrypted_char_value = ''
            index += 1  # Move to the next character after 'a'
            while index < len(encrypted_message) and encrypted_message[index].isdigit():
                encrypted_char_value += encrypted_message[index]
                index += 1

            if encrypted_char_value:  # Check if encrypted_char_value is not empty
                decrypted_char_value = int(encrypted_char_value) // private_key  # Decrypt the character value
                decrypted_char = chr(decrypted_char_value + ord('A') - 1)  # Convert the decrypted value to a character
                decrypted_chars.append(decrypted_char)
        elif encrypted_message[index] == 'S':
            # If the current character is 'S', it represents a space in the original message
            decrypted_chars.append(' ')
            index += 1  # Move to the next character
        else:
            # If the current character is neither 'a' nor 'S', it's None which represents a non-alphabetic character
            index += 1  # Move to the next character

    decrypted_message = ''.join(decrypted_chars)
    return decrypted_message

# Example usage:
encrypted_message = input("Hva er den enkryptere meldingen?  ")
private_key = int(input("Hva er private keyen?  "))  # Assume the private key used for encryption was 7
decrypted_message = decrypt_message(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
