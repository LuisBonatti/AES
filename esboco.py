import constants
from utils import key_matrix, RotWord, SubWord, addRoundKey, SubBytes, ShiftRow, sub_tabela_e, sub_tabela_l, sub_mix, \
    MixColumns

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
    for j in range(10):
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
        matrizes[j] = matriz_da_chave
        matriz_da_chave = new_matrix


expansao_de_chave(matriz_da_chave=keyMatrix)

for i in range(8):
    round = addRoundKey(texto_simples, matrizes[i])
    sub = SubBytes(round)
    shift = ShiftRow(sub)
    matrizes[i + 1] = MixColumns(shift)

round = addRoundKey(texto_simples, matrizes[9])
sub = SubBytes(round)
shift = ShiftRow(sub)
print(shift)
