import constants
from utilities.file import pkcs7_padding, format_data, get_file


class Cipher:
    def __init__(self, key, file_path=None, simple_text=None):
        if (simple_text, file_path) is None:
            raise Exception("Simple text or file_path is required!")
        self.simple_text = simple_text
        self.file_path = file_path
        self.key = key
        self.matrizes = {}
        self.keyMatrix = self.key_matrix(self.key)

    def encrypt_block(self, data):
        self.expansao_de_chave(self.keyMatrix)
        round = self.add_round_key(data, self.matrizes[0])
        for i in range(1, 10):
            sub = self.sub_bytes(round)
            shift = self.shift_row(sub)
            mix = self.mix_columns(shift)
            round = self.add_round_key(self.matrizes[i], mix)

        sub = self.sub_bytes(round)
        shift = self.shift_row(sub)
        round = self.add_round_key(shift, self.matrizes[10])
        self.matrizes = {}
        return round

    def to_hex_string(self, hex_list):
        return ''.join([hex_value[2:].zfill(2) for row in hex_list for hex_value in row])

    def encrypt(self):
        if self.file_path:
            data = get_file(self.file_path)
        else:
            data = self.simple_text
        text_padded = pkcs7_padding(data)
        self.simple_text = format_data(text_padded)
        blocks_qtd = int(len(self.simple_text) / 4)
        final_result = ''
        for b in range(blocks_qtd):
            block_grid = self.get_block()
            encrypted_block = self.encrypt_block(block_grid)
            final_result += self.to_hex_string(encrypted_block)
        return final_result

    def get_block(self):
        block = self.simple_text[:4]
        self.simple_text.pop(0), self.simple_text.pop(0), self.simple_text.pop(0), self.simple_text.pop(0)
        return block

    def sub_bytes(self, round):
        k = []
        for i in round:
            k.append(self.sub_word(i))
        return k

    def first_add_round_key(self, texto_simples, roundkey):
        l = []
        for idx, item in enumerate(roundkey):
            p = []
            for i, e in enumerate(item):
                try:
                    x = hex(texto_simples[idx][i])
                except TypeError:
                    x = hex(int(texto_simples[idx][i], 16))
                y = int(e, 16)
                p.append(hex(int(x, 16) ^ y))
            l.append(p)
        return l

    def add_round_key(self, texto_simples, roundkey):
        l = []
        for idx, item in enumerate(roundkey):
            p = []
            for i, e in enumerate(item):
                try:
                    x = hex(texto_simples[idx][i])
                except TypeError:
                    x = hex(int(texto_simples[idx][i], 16))
                y = int(e, 16)
                p.append(hex(int(x, 16) ^ y))
            l.append(p)
        return l

    def sub_word(self, word):
        new_word = []
        for w in word:
            try:
                left, right = w.split('0x')[1]
            except ValueError:
                left = '0'
                right = w.split('0x')[1]
            if left.isnumeric() and right.isnumeric():
                new_word.append(hex(constants.sbox[int(left)][int(right)]))
            elif left.isnumeric() and (right.isnumeric() == False):
                new_word.append(hex(constants.sbox[int(left)][constants.idx[right]]))
            elif right.isnumeric() and (left.isnumeric() == False):
                new_word.append(hex(constants.sbox[constants.idx[left]][int(right)]))
            else:
                new_word.append(hex(constants.sbox[constants.idx[left]][constants.idx[right]]))
        return new_word

    def rot_word(self, key_matrix):
        x = []
        [x.append(i) for i in key_matrix[-1]]
        last = x
        last.append(last.pop(0))
        return last

    def key_matrix(self, key):
        board = [
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
        ]
        key_list = key.split(",")
        hexadecimal_key = []
        add_0x = False
        for i in key_list:
            try:
                hexadecimal_key.append(hex(int(i)))
            except ValueError:
                hexadecimal_key.append(i.encode('utf-8').hex())
                add_0x = True
        if add_0x:
            hex_key = [f"0x{i}" for i in hexadecimal_key]
        else:
            hex_key = hexadecimal_key
        count = 0
        for i in range(4):
            for j in range(4):
                board[i][j] = hex_key[count]
                count += 1
        return board

    def expansao_de_chave(self, matriz_da_chave):
        self.matrizes[0] = matriz_da_chave
        for j in range(1, 11):
            last_word_line = self.rot_word(matriz_da_chave)
            new_words = self.sub_word(last_word_line)
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
            self.matrizes[j] = matriz_da_chave

    def sub_tabela_e(self, word):
        try:
            left, right = word.split('0x')[1]
            if len(right) > 2:
                right = right[-1]
                left = right[:2]
        except ValueError:
            left = '0'
            right = word.split('0x')[1]
            if len(right) > 2:
                right = right[-1]
                left = right[:2]
        if left.isnumeric() and right.isnumeric():
            return hex(constants.tabela_e[int(left)][int(right)])
        elif left.isnumeric() and (right.isnumeric() == False):
            return hex(constants.tabela_e[int(left)][constants.idx[right]])
        elif right.isnumeric() and (left.isnumeric() == False):
            return hex(constants.tabela_e[constants.idx[left]][int(right)])
        else:
            return hex(constants.tabela_e[constants.idx[left]][constants.idx[right]])

    def sub_tabela_l(self, word):
        try:
            left, right = word.split('0x')[1]
        except ValueError:
            left = '0'
            right = word.split('0x')[1]
        if left.isnumeric() and right.isnumeric():
            return hex(constants.tabela_l[int(left)][int(right)])
        elif left.isnumeric() and (right.isnumeric() == False):
            return hex(constants.tabela_l[int(left)][constants.idx[right]])
        elif right.isnumeric() and (left.isnumeric() == False):
            return hex(constants.tabela_l[constants.idx[left]][int(right)])
        else:
            return hex(constants.tabela_l[constants.idx[left]][constants.idx[right]])

    def sub_mix(self, word, w_num):
        k = '0x00'
        for i, e in enumerate(word):
            aux = constants.multi_matrix[w_num][i]
            d = None
            if int(e, 16) == 0:
                d = 0
            if int(e, 16) == 1:
                d = aux
            if aux == 1:
                d = e
            if d is None:
                x = self.sub_tabela_l((word[i]))
                aux = constants.multi_matrix[w_num][i]
                y = self.sub_tabela_l(hex(aux))
                m = hex(int(x, 16) + int(y, 16))
                if int(m, 16) > int('0xFF', 16):
                    m = hex(int(m, 16) - int('0xFF', 16))
                d = self.sub_tabela_e(m)
            try:
                k = hex(int(k, 16) ^ int(d, 16))
            except TypeError:
                k = hex(int(k, 16) ^ d)
        return k

    def mix_columns(self, shift):
        new_matriz = []
        ft = []
        sd = []
        tr = []
        qt = []
        for i in range(4):
            new_word = []
            for j, e in enumerate(shift):
                new_word.append(self.sub_mix(e, i))
            new_matriz.append(new_word)
        for i, e in enumerate(new_matriz):
            for j, k in enumerate(e):
                if j == 0:
                    ft.append(k)
                if j == 1:
                    sd.append(k)
                if j == 2:
                    tr.append(k)
                if j == 3:
                    qt.append(k)
        return [ft, sd, tr, qt]

    def shift_row(self, item):
        ft_row = []
        sd_row = []
        tr_row = []
        new_matriz = item
        for i, e in enumerate(item):
            for j, f in enumerate(e):
                if j == 1:
                    ft_row.append(f)
                if j == 2:
                    sd_row.append(f)
                if j == 3:
                    tr_row.append(f)
        ft = ft_row
        ft.append(ft.pop(0))
        sd = sd_row
        f = sd.pop(0)
        s = sd.pop(0)
        sd.append(f)
        sd.append(s)
        tr = tr_row
        f = tr.pop(3)
        tr.insert(0, f)
        for i, e in enumerate(item):
            for j, f in enumerate(e):
                if j == 1:
                    new_matriz[i][j] = ft[i]
                if j == 2:
                    new_matriz[i][j] = sd[i]
                if j == 3:
                    new_matriz[i][j] = tr[i]
        return new_matriz
