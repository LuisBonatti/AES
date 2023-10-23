from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define the plaintext and the key
plaintext = "DESENVOLVIMENTO!"
key = b'ABCDEFGHIJKLMNOP'
cipher = AES.new(key, AES.MODE_ECB)
print(key)

block_size = AES.block_size
plaintext = plaintext + ' ' * (block_size - len(plaintext) % block_size)
print(plaintext)
# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
print(ciphertext.hex())

# Print the ciphertext
print("Ciphertext:", ciphertext)

# To decrypt the ciphertext, you'll need the same key and use the same AES.MODE_ECB mode
decipher = AES.new(key, AES.MODE_ECB)
decrypted_plaintext = decipher.decrypt(ciphertext).rstrip()
print("Decrypted plaintext:", decrypted_plaintext.decode('utf-8'))