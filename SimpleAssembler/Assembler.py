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
