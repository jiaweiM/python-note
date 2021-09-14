from Bio import SeqIO
from Bio.Seq import Seq


def test_read():
    it = SeqIO.parse(r"D:\data\fasta\uniprot-proteome-UP000000624.fasta", "fasta")
    record = next(it)
    print(record.id)
    print(record.name)


def test_genbank():
    count_all = 0
    count = 0
    unverified = 0
    records = []
    for record in SeqIO.parse(r"D:\data\hbv\sequence.gb", "genbank"):
        count_all += 1
        annotations = record.annotations
        topology = annotations['topology']
        definition = record.description
        if "UNVERIFIED" in definition:
            unverified += 1
            continue
        if topology == 'circular':
            records.append(record)
            count += 1

        # print(record.annotations)
        # print(record.id)
    SeqIO.write(records, r"D:\data\hbv\hav_complete_genome_clean.fasta", "fasta")
    print(count_all)
    print(count)


def test_transcription():
    rna_seq = Seq("AGGUGAAGCGAAGUGCACA")
    comp_seq = rna_seq.complement_rna()
    print(rna_seq.reverse_complement())


def test_genbank_hbv_s_gene():
    records = list(SeqIO.parse(r"D:\data\hbv\sequence (1).gb", 'genbank'))
    print(len(records))


