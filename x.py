from block_cipher import Cipher

texto_simples = [[0x44, 0x45, 0x53, 0x45], [0x4e, 0x56, 0x4f, 0x4c], [0x56, 0x49, 0x4d, 0x45], [0x4e, 0x54, 0x4f, 0x21]]
chave = "20,1,94,33,199,0,48,9,31,94,112,40,59,30,100,248"
x = Cipher(chave, file_path="teste.txt").encrypt()
"e89639fe5021b0190e3775e77b6a2f7ace48c21ed35a40facd929a1bf25fc595"
