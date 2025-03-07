import string
from collections import Counter

# Frequency analysis of English language letters
english_letter_freq = {
    'e': 0.12702, 't': 0.09056, 'a': 0.08167, 'o': 0.07507, 'i': 0.06966, 'n': 0.06749,
    's': 0.06327, 'h': 0.06094, 'r': 0.05987, 'd': 0.04253, 'l': 0.04025, 'u': 0.02758,
    'c': 0.02702, 'm': 0.02406, 'f': 0.02228, 'y': 0.01974, 'p': 0.01929, 'b': 0.01492,
    'g': 0.01292, 'v': 0.00829, 'k': 0.00772, 'w': 0.00748, 'x': 0.00150, 'q': 0.00095,
    'j': 0.00077, 'z': 0.00074
}

# Function to perform frequency analysis on ciphertext
def frequency_analysis(text):
    # Remove non-alphabet characters and convert to lowercase
    text = ''.join(filter(str.isalpha, text)).lower()
    
    # Count the frequency of each letter
    letter_count = Counter(text)
    
    # Sort the letters by frequency (highest first)
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    
    # Return the sorted list of (letter, frequency) pairs
    return sorted_letters

# Function to suggest a decryption based on frequency analysis
def suggest_decryption(ciphertext):
    # Perform frequency analysis on the ciphertext
    freq_analysis = frequency_analysis(ciphertext)
    
    # Get the sorted letters from the analysis
    sorted_cipher_letters = [item[0] for item in freq_analysis]
    
    # English letters sorted by frequency
    english_sorted_letters = sorted(english_letter_freq, key=lambda x: english_letter_freq[x], reverse=True)
    
    # Create a mapping from the ciphertext letters to the English letters based on frequency
    letter_mapping = {}
    for i in range(min(len(sorted_cipher_letters), len(english_sorted_letters))):
        letter_mapping[sorted_cipher_letters[i]] = english_sorted_letters[i]
    
    # Decrypt the ciphertext based on the letter mapping
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            # If the character is in the mapping, replace it with the mapped letter
            decrypted_text.append(letter_mapping.get(char.lower(), char))
        else:
            # Otherwise, just append the non-alphabetic character (like spaces, punctuation)
            decrypted_text.append(char)
    
    # Join the list of characters to form the decrypted text
    return ''.join(decrypted_text)

# Main function
def main():
    # Take input encrypted message (ciphertext)
    ciphertext = input("Enter the encrypted message: ")
    
    # Suggest the most likely decryption based on frequency analysis
    decrypted_text = suggest_decryption(ciphertext)
    
    # Output the most likely decrypted text
    print("\nMost likely decrypted text (using frequency analysis):\n")
    print(decrypted_text)

if __name__ == "__main__":
    main()
