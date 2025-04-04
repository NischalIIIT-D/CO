import sys
io_file = sys.argv[1]
op_file = sys.argv[2]

with open(io_file) as f:
    list = f.readlines()
    li = []
    for i in list:
        li.append(i.rstrip("\n"))

def instruc_type(ins):
    opcode = ins[25:]
    if opcode == "0110011":
        return "R"
    if opcode == "0000011" or opcode == "0010011" or opcode == "1100111":
        return "I"
    if opcode == "0100011":
        return "S"
    if opcode == "1100011":
        return "B"
    if opcode == "1101111":
        return "J"
    return "Invalid"

def dec_ubin_convert(num_dec):
    bin_Str = bin(num_dec & 0xFFFFFFFF)[2:].zfill(32)
    return bin_Str

def dec_2s_comp_convert(num_dec):
    bin_Str = bin(abs(num_dec) & 0xFFFFFFFF)[2:].zfill(32)
    inv_str = ''
    if num_dec < 0:
        for bit in bin_Str:
            if bit == '0':
                inv_str += '1'
            else:
                inv_str += '0'
        twos_comp = bin(int(inv_str, 2) + 1)[2:].zfill(32)
        return twos_comp
    return bin_Str

def add_2s_comp(b1, b2): 
    n1 = int(b1, 2)
    n2 = int(b2, 2)
    result = n1 + n2
    bin_result = bin(result & 0xFFFFFFFF)[2:].zfill(32)
    inv_str = ''
    if result >= 0:
        return bin_result
    else:
        for bit in bin_result:
            if bit == '0':
                inv_str += '1'
            else:
                inv_str += '0'
        twos_comp = bin(int(inv_str, 2) + 1)[2:].zfill(32)
        return twos_comp

def bitwise_and(b1, b2):
    n1 = int(b1, 2)
    n2 = int(b2, 2)
    result = n1 & n2
    bin_result = bin(result)[2:].zfill(len(b1))
    return bin_result

def bitwise_or(b1, b2):
    n1 = int(b1, 2)
    n2 = int(b2, 2)
    result = n1 | n2
    bin_result = bin(result)[2:].zfill(len(b1))
    return bin_result

def b_dec_2s_comp_convert(bin_str):  
    if bin_str[0] == '1':
        inv = ""
        for bit in bin_str:
            if bit == '0':
                inv += '1'
            else:
                inv += '0'
        inverted_int = int(inv, 2)
        twos_comp_int = inverted_int + 1
        twos_comp_bin = bin(twos_comp_int)[2:].zfill(32)
        dec_val = int(twos_comp_bin, 2)
        dec_val = -dec_val
    else:
        dec_val = int(bin_str, 2)
    return dec_val

def sext(bin_str):
    lent = len(bin_str)
    if bin_str[0] == '1':
        extd = ''
        for k1 in range(32 - lent):
            extd += '1'
        bin_str = extd + bin_str
    else:
        extd = ''
        for k2 in range(32 - lent):
            extd += '0'
        bin_str = extd + bin_str
    return bin_str

def unsigned(bin_str):
    no_of_0 = 32 - len(bin_str)
    extd_str = '0' * no_of_0 + bin_str
    return extd_str

def b_dec_unsign_conv(bin_str):
    if bin_str[0] == '1':
        inv = ''
        for bit in bin_str:
            if bit == '0':
                inv += '1'
            else:
                inv += '0'
        new_incs = bin(int(inv, 2) + 1)[2:].zfill(len(bin_str))
        return -int(new_incs, 2)
    else:
        return int(bin_str, 2)

def signed(bin_str):
    return b_dec_unsign_conv(bin_str)

def b_hex_conv(bin_str):
    len_req = (len(bin_str) + 3) // 4 * 4
    bin_str = bin_str.zfill(len_req)

    L_dash = []
    for i in range(0, len(bin_str), 4):
        L_dash.append(bin_str[i:i + 4])

    hexdig = []
    for i in L_dash:
        decimal_value = int(i, 2) 
        hex_digit = hex(decimal_value)[2:]
        hexdig.append(hex_digit)

    hex_str = ''.join(hexdig)
    return hex_str
