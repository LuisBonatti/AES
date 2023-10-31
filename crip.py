from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Define the key
key = b'ABCDEFGHIJKLMNOP'
cipher = AES.new(key, AES.MODE_ECB)

# Read the PDF file as binary data
pdf_filename = "T1 - Trabalho.pdf"

with open(pdf_filename, "rb") as pdf_file:
    pdf_data = pdf_file.read()

# Convert the binary data to a string (assuming it's text)
pdf_text = pdf_data.decode('utf-8', 'ignore')  # This may not work well for all PDFs

# Encrypt the PDF text
block_size = AES.block_size
padded_pdf_text = pad(pdf_text.encode('utf-8'), block_size)
ciphertext = cipher.encrypt(padded_pdf_text)
print(ciphertext.hex())
# Save the encrypted content to a file
encrypted_pdf_filename = "encrypted_pdf"
with open(encrypted_pdf_filename, "wb") as encrypted_pdf_file:
    encrypted_pdf_file.write(ciphertext)

print("PDF content encrypted and saved to", encrypted_pdf_filename)
