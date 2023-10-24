import constants
from utils import key_matrix, RotWord, SubWord, addRoundKey, SubBytes, ShiftRow, sub_tabela_e, sub_tabela_l, sub_mix, \
    MixColumns, addRoundKey1

chave = "ABCDEFGHIJKLMNOP"
# texto_simples = [[0x44, 0x45, 0x53, 0x45],
#                  [0x4e, 0x56, 0x4f, 0x4c],
#                  [0x56, 0x49, 0x4d, 0x45],
#                  [0x4e, 0x54, 0x4f, 0x21]]

texto_simples = [[0x44, 0x4e, 0x56, 0x4e],
                 [0x45, 0x56, 0x49, 0x54],
                 [0x53, 0x4f, 0x4d, 0x4f],
                 [0x45, 0x4c, 0x45, 0x21]]

keyMatrix = key_matrix(chave)
matrizes = {}


def expansao_de_chave(matriz_da_chave):
    matrizes[0] = matriz_da_chave
    for j in range(1, 11):
        last_word_line = RotWord(matriz_da_chave)
        new_words = SubWord(last_word_line)
        rcon = constants.roundConstant[j]
        hex(rcon)
        new_words[0] = hex(rcon ^ int(new_words[0], 16))
        new_matrix = []
        last_word = []
        for idx, item in enumerate(matriz_da_chave):
            p = []
            for i, e in enumerate(item):
                if len(new_matrix) == 0:
                    p.append(hex(int(new_words[i], 16) ^ int(e, 16)))
                else:
                    p.append(hex(int(last_word[i], 16) ^ int(e, 16)))
            new_matrix.append(p)
            last_word = p
        matriz_da_chave = new_matrix
        matrizes[j] = matriz_da_chave


expansao_de_chave(matriz_da_chave=keyMatrix)
round = addRoundKey(texto_simples, matrizes[0])

for i in range(1, 10):
    sub = SubBytes(round)
    shift = ShiftRow(sub)
    mix = MixColumns(shift)
    round = addRoundKey1(matrizes[i], mix)

sub = SubBytes(round)
shift = ShiftRow(sub)
round = addRoundKey1(shift, matrizes[10])
print(round)
