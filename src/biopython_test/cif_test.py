from Bio.PDB.MMCIFParser import MMCIFParser
from Bio.PDB import PDBList
from Bio.PDB import MMCIF2Dict
from Bio.PDB import vectors

def test_info():
    data = MMCIF2Dict.MMCIF2Dict('1fat.cif')
    structure_id = data['_entry.id']
    assert structure_id == ['1FAT']

    print(structure_id)


def test_navigate():
    parser = MMCIFParser()
    structure = parser.get_structure("test", '1fat.cif')
    assert len(structure) == 1
    model = structure[0]
    chain = model['A']
    residue = chain[1]
    atom = residue['CA']

    atom_list = list(structure.get_atoms())
    atom1 = atom_list[0]
    atom2 = atom_list[1]
    atom3 = atom_list[2]

    distance = atom1 - atom2
    print(distance)

    vector1 = atom1.get_vector()
    vector2 = atom2.get_vector()
    vector3 = atom3.get_vector()

    angle = vectors.calc_angle(vector1, vector2, vector3)
    print(angle)

    # for model in structure:
    #     for chain in model:
    #         for residue in chain:
    #             for atom in residue:
    #                 print(atom)


def test_download():
    pdbl = PDBList()
    pdbl.retrieve_pdb_file("1FAT")
