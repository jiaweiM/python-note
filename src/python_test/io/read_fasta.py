file = open(r"D:\database\oglycan_proteins.fasta")
count = 0
header = ""
seq = []
for line in file:
    line = line.strip()
    if line.startswith(">"):
        count += 1
        if len(seq) != 0:
            protein = "".join(seq)
            print(header + "\t" + protein)
            seq.clear()
        header = line
    else:
        seq.append(line)
print(count)
