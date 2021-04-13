from Bio import SeqIO
import pandas as pd

seq_dict = {}
for record in SeqIO.parse(r"D:\data\fasta\uniprot-proteome-UP000000624.fasta", "fasta"):
    id = record.id
    seq_dict[id.split('|')[1]] = str(record.seq)

data = pd.read_excel(r"D:\data\fasta\epitope.xlsx", sheet_name="IEDB104")


def add_start_index(row):
    acc = row["Parent Protein Accession"]
    seq = row['Description']
    if acc not in seq_dict:
        return -2

    prot_seq = seq_dict[acc]
    print(seq)
    print(prot_seq)
    idx = prot_seq.find(seq)
    return idx


data['Index'] = data.apply(add_start_index, axis=1)

data.to_excel(r"D:\data\fasta\epitope2.xlsx", sheet_name="Sheet")

print(data)
