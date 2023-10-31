from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Define the plaintext and the key
plaintext = "DESENVOLVIMENTO!"
key = b'ABCDEFGHIJKLMNOP'
cipher = AES.new(key, AES.MODE_ECB)
print(plaintext)

# Pad the plaintext with PKCS7 padding
block_size = AES.block_size
padded_plaintext = pad(plaintext.encode('utf-8'), block_size)
print(padded_plaintext)

ciphertext = cipher.encrypt(padded_plaintext)
print(ciphertext.hex())

# Print the ciphertext
print("Ciphertext:", ciphertext)

# To decrypt the ciphertext, you'll need the same key and use the same AES.MODE_ECB mode
decipher = AES.new(key, AES.MODE_ECB)
decrypted_plaintext = unpad(decipher.decrypt(ciphertext), block_size)
print("Decrypted plaintext:", decrypted_plaintext.decode('utf-8'))

ciphertext_bytes = bytes.fromhex("e89639fe5021b0190e3775e77b6a2f7ace48c21ed35a40facd929a1bf25fc595")
print(ciphertext_bytes)