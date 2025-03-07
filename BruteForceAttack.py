import itertools

# Function to decrypt the message using a given key (key is a permutation of the alphabet)
def decrypt(message, key):
    # Create a dictionary for the substitution cipher mapping
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    substitution_map = {alphabet[i]: key[i] for i in range(len(alphabet))}
    decrypted_message = []

    # Decrypt the message
    for char in message:
        if char.isalpha():
            decrypted_message.append(substitution_map[char.lower()] if char.islower() else substitution_map[char.lower()].upper())
        else:
            decrypted_message.append(char)  # Preserve non-alphabetic characters

    return ''.join(decrypted_message)

# Function to perform brute-force decryption
def brute_force_decrypt(ciphertext):
    # Generate all permutations of the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    possible_keys = itertools.permutations(alphabet)

    # Try all permutations and print the result
    decrypted_texts = []
    for key_tuple in possible_keys:
        key = ''.join(key_tuple)
        decrypted_message = decrypt(ciphertext, key)
        decrypted_texts.append(decrypted_message)
    
    return decrypted_texts

# Main function to take input and run brute-force decryption
def main():
    # Take input encrypted message
    ciphertext = input("Enter the encrypted message: ")
    
    # Perform brute-force decryption
    decrypted_texts = brute_force_decrypt(ciphertext)
    
    # Output all possible decrypted texts
    print(f"\nAll possible decrypted texts:\n")
    for idx, text in enumerate(decrypted_texts):
        print(f"Decrypted {idx+1}: {text}")

#if __name__ == "__main__":
    main()
