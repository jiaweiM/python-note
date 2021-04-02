import pandas as pd

data = pd.read_csv("D:\data\iedb_epitopes_104.csv")
seq_dict = {}
for id, val in data.iloc[:, 1].items():
    # print(str(id) + "\t" + val)
    seq_dict[val] = data.iloc[id, :]


def remove_duplicate(seq_set):
    dup_seq_set = set()
    for seq in seq_set:
        if seq in dup_seq_set:
            continue
        add = True
        to_remove = set()
        for dup_seq in dup_seq_set:
            if seq in dup_seq:
                add = False
                break
            elif dup_seq in seq:
                to_remove.add(dup_seq)

        dup_seq_set = dup_seq_set - to_remove
        if add:
            dup_seq_set.add(seq)
    return dup_seq_set


seqs = remove_duplicate(seq_dict.keys())
print(len(seqs))


# for seq in seqs:
#     row = seq_dict[seq]
#     print(str(row.iloc[0]) + "\t" + str(row.iloc[1]) + "\t" + str(row.iloc[2]) + "\t" + str(row.iloc[3]) + "\t" + str(
#         row.iloc[4]) + "\t" +
#           str(row.iloc[5]) + "\t" + str(row.iloc[6]) + "\t")


def find_overlap(seq_set):
    overlap_set = set()
    for seq1 in seq_set:
        for seq2 in seq_set:
            if seq1 == seq2:
                continue
            for count in range(4, 20):
                if seq1[:count] == seq2[-count:]:
                    overlap_set.add((seq2, seq1))
                elif seq2[:count] == seq1[-count:]:
                    overlap_set.add((seq1, seq2))
    return overlap_set


overlap_set = find_overlap(seqs)
print(len(overlap_set))
for seq in overlap_set:
    print(seq[0]+"\t"+seq[1])
    # row = seq_dict[seq]
    # print(str(row.iloc[0]) + "\t" + str(row.iloc[1]) + "\t" + str(row.iloc[2]) + "\t" + str(row.iloc[3]) + "\t" + str(
    #     row.iloc[4]) + "\t" +
    #       str(row.iloc[5]) + "\t" + str(row.iloc[6]) + "\t")
