import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r') as f:
    list = f.readlines()
    l = []
    for i in list:
        l.append((i.rstrip("\n").split()))
with open(output_file, 'w') as f:
    f.write("")
    
R_type = ["add", "sub", "slt", "srl", "or", "and"]
I_type = ["lw", "addi", "jalr"]
S_type = ["sw"]
B_type = ["beq", "bne"]
J_type = ["jal"]

label = {}

regABItoBinary = {"zero": "00000",
                  "ra": "00001",
                  "sp": "00010",
                  "gp": "00011",
                  "tp": "00100",
                  "t0": "00101",
                  "t1": "00110",
                  "t2": "00111",
                  "s0": "01000", 
                  "fp": "01000",
                  "s1": "01001",
                  "a0": "01010",
                  "a1": "01011",
                  "a2": "01100",
                  "a3": "01101",
                  "a4": "01110",
                  "a5": "01111",
                  "a6": "10000",
                  "a7": "10001",
                  "s2": "10010",
                  "s3": "10011",
                  "s4": "10100",
                  "s5": "10101",
                  "s6": "10110",
                  "s7": "10111",
                  "s8": "11000",
                  "s9": "11001",
                  "s10": "11010",
                  "s11": "11011",
                  "t3": "11100",
                  "t4": "11101",
                  "t5": "11110",
                  "t6": "11111",
                  }
vir_halt = False
def dec_to_bin(dec_num):
    if dec_num < -2 ** 31 or dec_num >= 2 ** 31:
        raise ValueError("Decimal number out of range for 32 bits representation")
    if dec_num < 0:
        dec_num = 2 ** 32 + dec_num
    bin_repr = bin(dec_num)[2:]
    updated_bin = bin_repr.zfill(32)
    return str(updated_bin)

def instr_type(instr):
    if instr in R_type:
        return "R"
    if instr in I_type:
        return "I"
    if instr in S_type:
        return "S"
    if instr in B_type:
        return "B"
    if instr in J_type:
        return "J"
    return "INVALID"
    def Rtype_conversion(instruction):
    funct3 = {"add": "000",
              "sub": "000",
              "slt": "010",
              "srl": "101",
              "or": "110",
              "and": "111"}
    opcode = "0110011"
    temp = instruction[1].split(',')
    rd = temp[0]
    rs1 = temp[1]
    rs2 = temp[2]
    try:
        regABItoBinary[rs2]
        regABItoBinary[rs1]
        regABItoBinary[rd]
    except:
        return -1
    if instruction[0] == "sub":
        return (f'0100000{regABItoBinary[rs2]}{regABItoBinary[rs1]}{funct3[instruction[0]]}'
                f'{regABItoBinary[rd]}{opcode}')
    return (f'0000000{regABItoBinary[rs2]}{regABItoBinary[rs1]}{funct3[instruction[0]]}'
            f'{regABItoBinary[rd]}{opcode}')
def Itype_conversion(instruction):
    funct3 = {"lw": "010",
              "addi": "000",
              "jalr": "000"
              }
    opcode = {"lw": "0000011",
              "addi": "0010011",
              "jalr": "1100111"
              }
    ins_name = instruction[0]
    if ins_name == "addi"  or ins_name == "jalr":
        temp = instruction[1].split(',')
        rd = temp[0]
        rs = temp[1]

        try:
            regABItoBinary[rs]
            regABItoBinary[rd]
        except:
            return -1
        imm = temp[2]
        imm_bin = dec_to_bin(int(imm))
        return f'{imm_bin[20:]}{regABItoBinary[rs]}{funct3[ins_name]}{regABItoBinary[rd]}{opcode[ins_name]}'
    else:
        temp = instruction[1].split(',')
        temp2 = temp[1].split('(')
        rd = temp[0]
        rs = temp2[1].rstrip(')')
        try:
            regABItoBinary[rs]
            regABItoBinary[rd]
        except:
            return -1
        imm = temp2[0]
        imm_bin = dec_to_bin(int(imm))
        return f'{imm_bin[20:]}{regABItoBinary[rs]}{funct3[ins_name]}{regABItoBinary[rd]}{opcode[ins_name]}'
def Stype_conversion(instruction):
    opcode = {"sw": "0100011"}
    funct3 = {"sw": "010"}
    ins_name = instruction[0]
    temp = instruction[1].split(',')
    temp2 = temp[1].split('(')
    rs2 = temp[0]
    rs1 = temp2[1].rstrip(')')
    try:
        regABItoBinary[rs1]
        regABItoBinary[rs2]
    except:
        return -1
    imm = temp2[0]
    imm_bin = dec_to_bin(int(imm))
    return f'{imm_bin[20:27]}{regABItoBinary[rs2]}{regABItoBinary[rs1]}{funct3[ins_name]}{imm_bin[27:]}{opcode[ins_name]}'
