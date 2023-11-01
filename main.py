from block_cipher import Cipher

texto_simples = "DESENVOLVIMENTO!"
chave = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P"
x = Cipher(chave, simple_text=texto_simples).encrypt()
print(x)
"e89639fe5021b0190e3775e77b6a2f7ace48c21ed35a40facd929a1bf25fc595"
