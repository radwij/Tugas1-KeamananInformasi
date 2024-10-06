# NAMA:     I Putu Raditya Partha Wijay
# NRP:      5025221210
# KELAS:    Keamanan Informasi A    


IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

P = [
    16,7,20,21,
    29,12,28,17,
    1,15,23,26,
    5,18,31,10,
    2,8,24,14,
    32,27,3,9,
    19,13,30,6,
    22,11,4,25
]

PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

SHIFTS = [
    1, 1, 2, 2,
    2, 2, 2, 2,
    1, 2, 2, 2,
    2, 2, 2, 1
]

SBOX = [
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ],

    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ],

    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ],

    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ],

    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ],

    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ],

    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ],

    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
]


def initial_permutation(block, table):
    permuted_block = []
    for index in table:
        permuted_block.append(block[index - 1])
    return permuted_block

def final_permutation(block, table):
    permuted_block = []
    for index in table:
        permuted_block.append(block[index - 1])
    return permuted_block

def permute(block, table):
    permuted_block = []
    for index in table:
        permuted_block.append(block[index - 1])
    return permuted_block

def left_shift(key_half, shift):
    for i in range(shift):
        first_bit = key_half.pop(0)
        key_half.append(first_bit)
    return key_half

def key_schedule(key):
    permuted_key = permute(key, PC1)
    left_half = permuted_key[:28]
    right_half = permuted_key[28:]
    subkeys = []
    for i in range(len(SHIFTS)):
        shift = SHIFTS[i]
        left_half = left_shift(left_half, shift)
        right_half = left_shift(right_half, shift)
        combined_key = left_half + right_half
        subkey = permute(combined_key, PC2)
        subkeys.append(subkey)
    return subkeys

def feistel_function(right_half, subkey):
    expanded_right = permute(right_half, E)
    xored = []
    for i in range(len(expanded_right)):
        xored_bit = expanded_right[i] ^ subkey[i]
        xored.append(xored_bit)
    sbox_output = []
    for i in range(8):
        block = xored[i*6:(i+1)*6]
        row_bits = [block[0], block[5]]
        row_str = str(block[0]) + str(block[5])
        row = int(row_str, 2)
        column_bits = [block[1], block[2], block[3], block[4]]
        column_str = ''.join(str(bit) for bit in column_bits)
        column = int(column_str, 2)
        sbox_value = SBOX[i][row][column]
        sbox_bits = bin(sbox_value)[2:].rjust(4, '0')
        for bit in sbox_bits:
            sbox_output.append(int(bit))
    permuted_output = permute(sbox_output, P)
    return permuted_output

def des_encrypt(block, key):
    permuted_block = initial_permutation(block, IP)
    left_half = permuted_block[:32]
    right_half = permuted_block[32:]
    subkeys = key_schedule(key)
    for i in range(16):
        subkey = subkeys[i]
        temp_right = right_half.copy()
        f_output = feistel_function(right_half, subkey)
        new_right = []
        for j in range(len(left_half)):
            new_bit = left_half[j] ^ f_output[j]
            new_right.append(new_bit)
        right_half = new_right
        left_half = temp_right
    combined_halves = right_half + left_half
    cipher_block = final_permutation(combined_halves, FP)
    return cipher_block

def des_decrypt(block, key):
    permuted_block = initial_permutation(block, IP)
    left_half = permuted_block[:32]
    right_half = permuted_block[32:]
    subkeys = key_schedule(key)
    for i in range(15, -1, -1):
        subkey = subkeys[i]
        temp_right = right_half.copy()
        f_output = feistel_function(right_half, subkey)
        new_right = []
        for j in range(len(left_half)):
            new_bit = left_half[j] ^ f_output[j]
            new_right.append(new_bit)
        right_half = new_right
        left_half = temp_right
    combined_halves = right_half + left_half
    plain_block = final_permutation(combined_halves, FP)
    return plain_block

def text_to_bit_array(text):
    bit_array = []
    for char in text:
        ascii_value = ord(char)
        bin_value = bin(ascii_value)[2:]
        while len(bin_value) < 8:
            bin_value = '0' + bin_value
        for bit in bin_value:
            bit_array.append(int(bit))
    return bit_array

def pad_bit_array(bit_array):
    padded_array = bit_array.copy()
    while len(padded_array) % 64 != 0:
        padded_array.append(0)
    return padded_array

def bit_array_to_hex(bit_array):
    hex_string = ''
    i = 0
    while i < len(bit_array):
        nibble = bit_array[i:i+4]
        nibble_str = ''
        for bit in nibble:
            nibble_str += str(bit)
        hex_digit = hex(int(nibble_str, 2))[2:]
        hex_string += hex_digit
        i += 4
    return hex_string

def bit_array_to_text(bit_array):
    text = ''
    i = 0
    while i < len(bit_array):
        byte = bit_array[i:i+8]
        byte_str = ''
        for bit in byte:
            byte_str += str(bit)
        ascii_char = chr(int(byte_str, 2))
        text += ascii_char
        i += 8
    return text

def encrypt_text(plaintext, key_text):
    key = text_to_bit_array(key_text[:8])
    key = pad_bit_array(key)
    bit_array = text_to_bit_array(plaintext)
    bit_array = pad_bit_array(bit_array)
    cipher_bits = []
    i = 0
    while i < len(bit_array):
        block = bit_array[i:i+64]
        encrypted_block = des_encrypt(block, key)
        cipher_bits.extend(encrypted_block)
        i += 64
    cipher_text = bit_array_to_hex(cipher_bits)
    return cipher_text

def decrypt_text(ciphertext, key_text):
    key = text_to_bit_array(key_text[:8])
    key = pad_bit_array(key)
    bit_array = []
    i = 0
    while i < len(ciphertext):
        hex_byte = ciphertext[i:i+2]
        bin_value = bin(int(hex_byte, 16))[2:]
        while len(bin_value) < 8:
            bin_value = '0' + bin_value
        for bit in bin_value:
            bit_array.append(int(bit))
        i += 2
    plain_bits = []
    i = 0
    while i < len(bit_array):
        block = bit_array[i:i+64]
        decrypted_block = des_decrypt(block, key)
        plain_bits.extend(decrypted_block)
        i += 64
    decrypted_text = bit_array_to_text(plain_bits).rstrip('\x00')
    return decrypted_text

# Main Program

def main():
    action = input("Do you want to (E)ncrypt or (D)ecrypt? ")
    action = action.lower()
    key_text = input("Enter the key (8 characters): ")
    if action == 'e':
        plaintext = input("Enter the plaintext: ")
        cipher_text = encrypt_text(plaintext, key_text)
        print("Encrypted Text (Cipher):", cipher_text)
    elif action == 'd':
        ciphertext = input("Enter the ciphertext (hex format): ")
        decrypted_text = decrypt_text(ciphertext, key_text)
        print("Decrypted Text (Plaintext):", decrypted_text)
    else:
        print("Invalid option selected. Please choose 'E' for encryption or 'D' for decryption.")

main()
