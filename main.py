from block_cipher import Cipher

texto_simples = "DESENVOLVIMENTO!"
chave = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P"
encrypt_text = Cipher(chave, simple_text=texto_simples).encrypt()
print(encrypt_text)


simple_example = [[0x44, 0x45, 0x53, 0x45], [0x4e, 0x56, 0x4f, 0x4c], [0x56, 0x49, 0x4d, 0x45], [0x4e, 0x54, 0x4f, 0x21]]
key = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P"
encrypt_text = Cipher(key, file_path="teste.txt", dest_file="testando.txt").encrypt()
print(encrypt_text)
