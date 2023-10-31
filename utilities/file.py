def get_file(file_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()
        return file_content


def pkcs7_padding(data):
    padding_length = 16 - (len(data) % 16)
    padding = bytes([padding_length] * padding_length)
    check_str = isinstance(data, str)
    if check_str:
        data = data.encode('utf-8')
    return data + padding


def format_data(data):
    hex_string = data.hex()
    hex_groups = [hex_string[i:i + 2] for i in range(0, len(hex_string), 2)]
    grid = [hex_groups[i:i + 4] for i in range(0, len(hex_groups), 4)]
    return grid



# data = get_file("../teste.txt")
# print(data)
# x = [[0x44, 0x45, 0x53, 0x45], [0x4e, 0x56, 0x4f, 0x4c], [0x56, 0x49, 0x4d, 0x45], [0x4e, 0x54, 0x4f, 0x21]]
# padded_data = pkcs7_padding(data)
# grid = format_data(padded_data)
# print(grid)
# hex_list = [[int(hex_str, 16) for hex_str in inner_list] for inner_list in original_list]
# print(hex_list)