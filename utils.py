import constants


def key_matrix(key):
    board = [
        ["", "", "", ""],
        ["", "", "", ""],
        ["", "", "", ""],
        ["", "", "", ""],
    ]
    key = key.encode('utf-8')
    hex_key = [f"0x{i}" for i in key.hex(":").split(':')]
    count = 0
    for i in range(4):
        for j in range(4):
            board[i][j] = hex_key[count]
            count += 1
    return board


def RotWord(key_matrix):
    x = []
    [x.append(i) for i in key_matrix[-1]]
    last = x
    last.append(last.pop(0))
    return last


def addRoundKey1(texto_simples, roundkey):
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


def addRoundKey(texto_simples, roundkey):
    l = []
    for idx, item in enumerate(roundkey):
        p = []
        for i, e in enumerate(item):
            try:
                x = hex(texto_simples[i][idx])
            except TypeError:
                x = hex(int(texto_simples[i][idx], 16))
            y = int(e, 16)
            p.append(hex(int(x, 16) ^ y))
        l.append(p)
    return l


def SubBytes(round):
    k = []
    for i in round:
        k.append(SubWord(i))
    return k


def ShiftRow(item):
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


def SubWord(word):
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


def sub_tabela_e(word):
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


def sub_tabela_l(word):
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


def sub_mix(word, w_num):
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
            x = sub_tabela_l((word[i]))
            aux = constants.multi_matrix[w_num][i]
            y = sub_tabela_l(hex(aux))
            m = hex(int(x, 16) + int(y, 16))
            if int(m, 16) > int('0xFF', 16):
                m = hex(int(m, 16) - int('0xFF', 16))
            d = sub_tabela_e(m)
        try:
            k = hex(int(k, 16) ^ int(d, 16))
        except TypeError:
            k = hex(int(k, 16) ^ d)
    return k


# TODO verificar mix colums, o restante foi validado.
def MixColumns(shift):
    new_matriz = []
    ft = []
    sd = []
    tr = []
    qt = []
    for i in range(4):
        new_word = []
        for j, e in enumerate(shift):
            new_word.append(sub_mix(e, i))
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
