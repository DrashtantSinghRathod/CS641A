#plaintext generation
def create_inputs_file(filename):
    # Define a mapping of 4-bit binary strings to characters from 'f' to 's'
    binary_to_char = {
        '0000': 'f',
        '0001': 'g',
        '0010': 'h',
        '0011': 'i',
        '0100': 'j',
        '0101': 'k',
        '0110': 'l',
        '0111': 'm',
        '1000': 'n',
        '1001': 'o',
        '1010': 'p',
        '1011': 'q',
        '1100': 'r',
        '1101': 's',
        '1110': 't',
        '1111': 'u'
    }
    
    # Open the output file in write mode
    with open(filename, 'w') as f:
        # Loop over the rows of the input matrix
        for row in range(8):
            # Loop over the 128 values in each row
            for value in range(128):
                # Convert the value to an 8-bit binary string
                binary_str = '{:08b}'.format(value)
                # Replace the first and second 4-bit blocks with corresponding characters
                first_char = binary_to_char[binary_str[:4]]
                second_char = binary_to_char[binary_str[4:8]]
                # Create a 64-bit binary string by concatenating 'ff' padding
                binary_row = 'ff' * row + first_char + second_char + 'ff' * (8 - row - 1)
                # Write the binary string and a space to the file
                f.write(binary_row + ' ')
            # Write a newline character to separate each row
            f.write('\n')

create_inputs_file("input.txt")