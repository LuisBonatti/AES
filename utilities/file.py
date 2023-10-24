def get_file(file_path):
    with open(file_path, 'rb') as file:
        # Read the entire content of the file into a bytes object
        file_content = file.read()
        return file_content


def pkcs7_padding(data, block_size):
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length] * padding_length)
    return data + padding


data = get_file("../teste.txt")
block_size = 16
padded_data = pkcs7_padding(data, block_size)
print(padded_data)

# Convert the bytes to a hexadecimal string
hex_string = padded_data.hex()

# Split the hex string into 2-character segments to represent bytes
bytes_list = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

# Create a 4x4 matrix
matrix = [bytes_list[i:i+4] for i in range(0, len(bytes_list), 4)]

# Print the hexadecimal string and the matrix
print("Hexadecimal String:", hex_string)

# Divida a string em grupos de 2 caracteres
hex_groups = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

# Crie um grid 4x4
grid = [hex_groups[i:i+4] for i in range(0, len(hex_groups), 4)]

blocos = int(len(grid)/4)

for i in range(blocos):
    x = grid[:4]
    grid.pop(0), grid.pop(1), grid.pop(2), grid.pop(3)

