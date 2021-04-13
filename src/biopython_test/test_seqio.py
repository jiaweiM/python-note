from Bio import SeqIO


def test_read():
    it = SeqIO.parse(r"D:\data\fasta\uniprot-proteome-UP000000624.fasta", "fasta")
    record = next(it)
    print(record.id)
    print(record.name)
