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

PC = "00000000000000000000000000000000"
mem = {
    "0x00010000": "00000000000000000000000000000000",
    "0x00010004": "00000000000000000000000000000000",
    "0x00010008": "00000000000000000000000000000000",
    "0x0001000C": "00000000000000000000000000000000",
    "0x00010010": "00000000000000000000000000000000",
    "0x00010014": "00000000000000000000000000000000",
    "0x00010018": "00000000000000000000000000000000",
    "0x0001001C": "00000000000000000000000000000000",
    "0x00010020": "00000000000000000000000000000000",
    "0x00010024": "00000000000000000000000000000000",
    "0x00010028": "00000000000000000000000000000000",
    "0x0001002C": "00000000000000000000000000000000",
    "0x00010030": "00000000000000000000000000000000",
    "0x00010034": "00000000000000000000000000000000",
    "0x00010038": "00000000000000000000000000000000",
    "0x0001003C": "00000000000000000000000000000000",
    "0x00010040": "00000000000000000000000000000000",
    "0x00010044": "00000000000000000000000000000000",
    "0x00010048": "00000000000000000000000000000000",
    "0x0001004C": "00000000000000000000000000000000",
    "0x00010050": "00000000000000000000000000000000",
    "0x00010054": "00000000000000000000000000000000",
    "0x00010058": "00000000000000000000000000000000",
    "0x0001005C": "00000000000000000000000000000000",
    "0x00010060": "00000000000000000000000000000000",
    "0x00010064": "00000000000000000000000000000000",
    "0x00010068": "00000000000000000000000000000000",
    "0x0001006C": "00000000000000000000000000000000",
    "0x00010070": "00000000000000000000000000000000",
    "0x00010074": "00000000000000000000000000000000",
    "0x00010078": "00000000000000000000000000000000",
    "0x0001007C": "00000000000000000000000000000000",
}
regs_mappin = {"00000": "00000000000000000000000000000000",
                "00001": "00000000000000000000000000000000",
                "00010": "00000000000000000000000101111100",
                "00011": "00000000000000000000000000000000",
                "00100": "00000000000000000000000000000000",
                "00101": "00000000000000000000000000000000",
                "00110": "00000000000000000000000000000000",
                "00111": "00000000000000000000000000000000",
                "01000": "00000000000000000000000000000000", 
                "01001": "00000000000000000000000000000000",
                "01010": "00000000000000000000000000000000",
                "01011": "00000000000000000000000000000000",
                "01100": "00000000000000000000000000000000",
                "01101": "00000000000000000000000000000000",
                "01110": "00000000000000000000000000000000",
                "01111": "00000000000000000000000000000000",
                "10000": "00000000000000000000000000000000",
                "10001": "00000000000000000000000000000000",
                "10010": "00000000000000000000000000000000",
                "10011": "00000000000000000000000000000000",
                "10100": "00000000000000000000000000000000",
                "10101": "00000000000000000000000000000000",
                "10110": "00000000000000000000000000000000",
                "10111": "00000000000000000000000000000000",
                "11000": "00000000000000000000000000000000",
                "11001": "00000000000000000000000000000000",
                "11010": "00000000000000000000000000000000",
                "11011": "00000000000000000000000000000000",
                "11100": "00000000000000000000000000000000",
                "11101": "00000000000000000000000000000000",
                "11110": "00000000000000000000000000000000",
                "11111": "00000000000000000000000000000000",
                }

def error_hand_instruction(ins):
    opcode = ins[25:]
    if opcode not in ["0110011", "0000011", "0010011", "1100111", "0100011", "1100011", "1101111"]:
        raise ValueError(f"Invalid opcode: {opcode}")
    

def error_hand_pc(pc):
    if int(pc, 2) % 4 != 0:
        raise ValueError(f"PC is not a multiple of four: {pc}")

def error_hand_memory_access(address):
    if address not in mem:
        raise ValueError(f"Memory access out of bounds: {address}")

def func_R(ins):
    funct7 = ins[0:7]
    rs2 = regs_mappin.get(ins[7:12])
    rs1 = regs_mappin.get(ins[12:17])
    funct3 = ins[17:20]
    rd = ins[20:25]

    if rs1 is None or rs2 is None or rd not in regs_mappin:
        raise ValueError(f"Invalid register index in R-type instruction: rs1={ins[12:17]}, rs2={ins[7:12]}, rd={rd}")

    if funct7 == "0000000":
        if funct3 == "000":  # add
            rs1_value = b_dec_2s_comp_convert(rs1)
            rs2_value = b_dec_2s_comp_convert(rs2)
            rd_value = rs1_value + rs2_value
            regs_mappin[rd] = dec_2s_comp_convert(rd_value)
        elif funct3 == "010":  # slt
            regs_mappin[rd] = "00000000000000000000000000000001" if sext(rs1) < sext(rs2) else "00000000000000000000000000000000"
        elif funct3 == "101":  # srl
            shift_amount = int(unsigned(rs2)[-5:], 2)
            result = int(rs1, 2) >> shift_amount
            regs_mappin[rd] = bin(result & 0xFFFFFFFF)[2:].zfill(32)
        elif funct3 == "110":  # or
            regs_mappin[rd] = bitwise_or(rs1, rs2)
        elif funct3 == "111":  # and
            regs_mappin[rd] = bitwise_and(rs1, rs2)
        else:
            raise ValueError(f"Invalid funct3 for R-type instruction: {funct3}")
    elif funct7 == "0100000" and funct3 == "000":  # sub
        rs1_value = signed(rs1)
        rs2_value = signed(rs2)
        regs_mappin[rd] = dec_2s_comp_convert(rs1_value - rs2_value)
    else:
        raise ValueError(f"Invalid funct7 or funct3 for R-type instruction: funct7={funct7}, funct3={funct3}")

def func_S(ins):

    imm_bin = ins[0:7] + ins[20:25]
    rs2 = regs_mappin[ins[7:12]]
    rs1 = regs_mappin[ins[12:17]]
    funct3 = ins[17:20]
    mem_ind = add_2s_comp(rs1, sext(imm_bin))
    mem_ind = b_hex_conv(mem_ind)
    mem_ind = "0x" + mem_ind
    mem[mem_ind] = rs2
def func_B(ins):
    global PC
    imm_bin = ins[0] + ins[24] + ins[1:7] + ins[20:24]
    rs2 = regs_mappin.get(ins[7:12])
    rs1 = regs_mappin.get(ins[12:17])
    funct3 = ins[17:20]

    if rs1 is None or rs2 is None:
        raise ValueError(f"Invalid register index in B-type instruction: rs1={ins[12:17]}, rs2={ins[7:12]}")

    if funct3 == "000":  # beq
        if rs1 == rs2:
            PC = add_2s_comp(PC, sext(imm_bin + "0"))
        else:
            PC = add_2s_comp(PC, "100")
    elif funct3 == "001":  # bne
        if rs1 != rs2:
            PC = add_2s_comp(PC, sext(imm_bin + "0"))
        else:
            PC = add_2s_comp(PC, "100")
    else:
        raise ValueError(f"Invalid funct3 for B-type instruction: {funct3}")

    error_hand_pc(PC)


def func_J(ins):
    global PC
    imm = ins[0] + ins[12:20] + ins[11] + ins[1:11]
    imm = sext(imm + "0")
    rd = ins[20:25]

    if rd not in regs_mappin:
        raise ValueError(f"Invalid register index in J-type instruction: rd={rd}")

    regs_mappin[rd] = add_2s_comp(PC, unsigned("100"))
    PC = add_2s_comp(PC, imm)
    PC = PC[:-1] + "0"

    error_hand_pc(PC)

l = dict()
for i in range(len(li)):
    l[dec_ubin_convert(i * 4)] = li[i]

with open(op_file, 'w') as f:
    f.write("")
while True:
    try:
        ins = l[PC]
        error_hand_instruction(ins)
        ins_type = instruc_type(ins)
        if ins_type == "R":
            func_R(ins)
            PC = add_2s_comp(PC, "100")
        elif ins_type == "I":
            func_I(ins)
        elif ins_type == "S":
            func_S(ins)
            PC = add_2s_comp(PC, "100")
        elif ins_type == "B":
            func_B(ins)
        elif ins_type == "J":
            func_J(ins)
        error_hand_pc(PC)
        regs_mappin["00000"] = "00000000000000000000000000000000"
        with open(op_file, 'a') as f:
            f.write("0b" + PC + " ")
            for key, value in regs_mappin.items():
                f.write("0b" + value + " ")
            f.write("\n")
        if ins == "00000000000000000000000001100011" or ins == "00000000000000000000000000000000":
            # halt
            break
    except ValueError as e:
        with open(op_file, 'a') as f:
            f.write(f"Error: {e}\n")
        break

with open(op_file, 'a') as f:
    for key, value in mem.items():
        f.write(key + ":0b" + value + "\n")
