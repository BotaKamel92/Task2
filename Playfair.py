# Helper function to create the Playfair matrix from the keyword
def create_playfair_matrix(keyword):
    # Remove duplicates and replace 'j' with 'i'
    matrix = []
    alphabet = "abcdefghiklmnopqrstuvwxyz"  # No 'j' in the matrix, 'i' and 'j' are considered the same letter
    keyword = keyword.lower().replace("j", "i")
    
    # Add characters from keyword to matrix
    for char in keyword:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    
    # Add remaining letters from the alphabet
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    # Create a 5x5 matrix
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix

# Helper function to display the Playfair matrix
def display_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

# Function to prepare the text (plaintext or ciphertext) for encryption/decryption
def prepare_text(text, encrypt=True):
    text = text.lower().replace("j", "i")
    
    # Split into pairs of letters
    pairs = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] != text[i + 1]:
            pairs.append(text[i:i+2])
            i += 2
        else:
            pairs.append(text[i] + "x")  # If the letters are the same or last single letter, add 'x'
            i += 1
    return pairs

# Helper function to find the position of a letter in the matrix
def find_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return -1, -1

# Function to encrypt using the Playfair cipher
def encrypt_playfair(matrix, plaintext):
    pairs = prepare_text(plaintext, encrypt=True)
    encrypted_text = []

    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        # If both letters are in the same row
        if row1 == row2:
            encrypted_text.append(matrix[row1][(col1 + 1) % 5])
            encrypted_text.append(matrix[row2][(col2 + 1) % 5])
        # If both letters are in the same column
        elif col1 == col2:
            encrypted_text.append(matrix[(row1 + 1) % 5][col1])
            encrypted_text.append(matrix[(row2 + 1) % 5][col2])
        # If letters form a rectangle
        else:
            encrypted_text.append(matrix[row1][col2])
            encrypted_text.append(matrix[row2][col1])

    return ''.join(encrypted_text)

# Function to decrypt using the Playfair cipher
def decrypt_playfair(matrix, ciphertext):
    pairs = prepare_text(ciphertext, encrypt=False)
    decrypted_text = []

    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        # If both letters are in the same row
        if row1 == row2:
            decrypted_text.append(matrix[row1][(col1 - 1) % 5])
            decrypted_text.append(matrix[row2][(col2 - 1) % 5])
        # If both letters are in the same column
        elif col1 == col2:
            decrypted_text.append(matrix[(row1 - 1) % 5][col1])
            decrypted_text.append(matrix[(row2 - 1) % 5][col2])
        # If letters form a rectangle
        else:
            decrypted_text.append(matrix[row1][col2])
            decrypted_text.append(matrix[row2][col1])

    return ''.join(decrypted_text)

# Main function
def main():
    # Take the keyword from the user
    keyword = input("Enter the keyword for the Playfair cipher: ")
    
    # Create and display the Playfair matrix
    matrix = create_playfair_matrix(keyword)
    print("\nPlayfair Matrix:")
    display_matrix(matrix)
    
    # Allow the user to choose between encryption and decryption
    choice = input("\nDo you want to (E)ncrypt or (D)ecrypt? ").lower()
    
    if choice == "e":
        plaintext = input("Enter the plaintext to encrypt: ")
        ciphertext = encrypt_playfair(matrix, plaintext)
        print(f"\nEncrypted text: {ciphertext}")
    
    elif choice == "d":
        ciphertext = input("Enter the ciphertext to decrypt: ")
        decrypted_text = decrypt_playfair(matrix, ciphertext)
        print(f"\nDecrypted text: {decrypted_text}")
    
    else:
        print("Invalid choice. Please choose either 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
