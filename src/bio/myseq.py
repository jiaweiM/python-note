class MySeq:
    """Biological sequence class"""

    def __init__(self, seq, seq_type="DNA"):
        self.seq = seq
        self.seq_type = seq_type

    def print_sequence(self):
        print("Sequence: " + self.seq)

    def get_seq_biotype(self):
        return self.seq_type

    def show_info_seq(self):
        print("Sequence: " + self.seq + " biotype: " + self.seq_type)

    def count_occurrences(self, seq_search):
        return self.seq.count(seq_search)
