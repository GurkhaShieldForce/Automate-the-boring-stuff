#! Python3
'''
It loads the dictionary file into a list of words.
For each word in the dictionary, it tries both the lowercase and uppercase versions.
It uses the decrypt() method from PyPDF2 to attempt decryption.
If successful, it prints the found password and exits.
If no password is found after trying all words, it notifies the user.

Run the script from the command line like this:
python pdf_password_breaker.py /path/to/encrypted.pdf /path/to/dictionary.txt

Replace /path/to/encrypted.pdf with the path to your encrypted PDF file, and /path/to/dictionary.txt with the path to the dictionary file you downloaded.

This is strictly for educational and profesional training purposes only. Please consider the legal aspects of this activity. 

'''

import sys
from PyPDF2 import PdfReader

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [word.strip() for word in file]

def try_decrypt(pdf_path, password):
    reader = PdfReader(pdf_path)
    if reader.is_encrypted:
        try:
            if reader.decrypt(password) == 1:
                return True
        except:
            pass
    return False

def brute_force_pdf(pdf_path, dictionary_path):
    words = load_dictionary(dictionary_path)
    total_words = len(words) * 2  # For both lowercase and uppercase
    
    print(f"Starting brute-force attack with {total_words} word combinations...")
    
    for i, word in enumerate(words):
        # Try lowercase
        if try_decrypt(pdf_path, word.lower()):
            return word.lower()
        
        # Try uppercase
        if try_decrypt(pdf_path, word.upper()):
            return word.upper()
        
        # Print progress every 1000 words
        if (i + 1) % 500 == 0:
            progress = ((i + 1) * 2 / total_words) * 100
            print(f"Progress: {progress:.2f}% ({(i + 1) * 2}/{total_words})")
    
    return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <pdf_path> <dictionary_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    dictionary_path = sys.argv[2]

    password = brute_force_pdf(pdf_path, dictionary_path)

    if password:
        print(f"Password found: {password}")
    else:
        print("Password not found in the dictionary.")

if __name__ == "__main__":
    main()