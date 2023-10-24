# Function to convert a string to a list of hexadecimal values
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
x = [[]]
for i in range(len(result)):
    for j in i:
        