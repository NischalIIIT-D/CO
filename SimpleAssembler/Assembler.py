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
    if instr in Bonus_type:
        return "Bonus"
    return "INVALID"
