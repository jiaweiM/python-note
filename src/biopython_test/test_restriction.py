from Bio import Restriction


def test_all_enzymes():
    for enzyme in Restriction.AllEnzymes:
        print(enzyme)
