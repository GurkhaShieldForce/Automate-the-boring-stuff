#! Python3
'''
It walks through the specified folder and its subfolders using os.walk().
For each PDF file, it attempts to decrypt it using the provided password.
If successful, it creates a decrypted copy with the "_decrypted.pdf" suffix.
If the password is incorrect, it prints a message and continues to the next file.

To use run: 
python decrypt_pdfs.py /path/to/folder password

Replace /path/to/folder with the actual path to the folder containing your PDFs, and password with the desired encryption/decryption password.
'''
import os
import sys
from PyPDF2 import PdfReader, PdfWriter

def decrypt_pdf(input_path, output_path, password):
    reader = PdfReader(input_path)
    
    if reader.is_encrypted:
        try:
            reader.decrypt(password)
        except:
            print(f"Incorrect password for: {input_path}")
            return False

        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        return True
    else:
        print(f"File is not encrypted: {input_path}")
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
                output_path = os.path.join(foldername, f"{os.path.splitext(filename)[0]}_decrypted.pdf")

                try:
                    if decrypt_pdf(input_path, output_path, password):
                        print(f"Successfully decrypted: {input_path}")
                except Exception as e:
                    print(f"Error processing {input_path}: {str(e)}")

if __name__ == "__main__":
    main()