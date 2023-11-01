def string_to_hex_list(input_string):
    hex_list = []
    for char in input_string:
        hex_value = hex(ord(char))
        hex_list.append(hex_value)
    return hex_list


# Read the content of the "teste.txt" file
with open("teste.txt", "r") as file:
    content = file.read()

# Split the content into lines and convert each character to hex
lines = content.split('\n')
result = [string_to_hex_list(line) for line in lines]
input_list = result[0]

# Create the 4x4 matrix
matrix = []

# Iterate through the input list and group elements into rows of 4
for i in range(0, len(input_list), 4):
    row = input_list[i:i + 4]
    matrix.append(row)

# Transpose the matrix
transposed_matrix = [[matrix[j][i] for j in range(4)] for i in range(4)]
print(transposed_matrix)
