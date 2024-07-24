#! Python 3
'''
It walks through the specified folder and its subfolders using os.walk().
For each PDF file, it creates an encrypted copy with the "_encrypted.pdf" suffix.
It verifies the encryption by attempting to decrypt the newly created file.
If successful, it deletes the original file.

To Use run:
python encrypt_pdfs.py /path/to/folder password

Replace /path/to/folder with the actual path to the folder containing your PDFs, and password with the desired encryption/decryption password.
'''
import os
import sys
from PyPDF2 import PdfReader, PdfWriter

def encrypt_pdf(input_path, output_path, password):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

def verify_encryption(file_path, password):
    try:
        reader = PdfReader(file_path)
        reader.decrypt(password)
        return True
    except:
        return False

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <folder_path> <password>")
        sys.exit(1)

    folder_path = sys.argv[1]
    password = sys.argv[2]

    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                input_path = os.path.join(foldername, filename)
                output_path = os.path.join(foldername, f"{os.path.splitext(filename)[0]}_encrypted.pdf")

                try:
                    encrypt_pdf(input_path, output_path, password)
                    
                    if verify_encryption(output_path, password):
                        print(f"Successfully encrypted: {input_path}")
                        os.remove(input_path)
                    else:
                        print(f"Failed to encrypt: {input_path}")
                        os.remove(output_path)
                except Exception as e:
                    print(f"Error processing {input_path}: {str(e)}")

if __name__ == "__main__":
    main()