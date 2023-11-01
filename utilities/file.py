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


def create_file(data, filename):
    try:
        with open(filename, "w") as file:
            file.write(data)
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
