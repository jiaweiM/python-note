from Bio.PDB.MMCIFParser import MMCIFParser
from Bio.PDB.MMCIF2Dict import MMCIF2Dict

parser = MMCIFParser()
structure = parser.get_structure("AF-A0A0A0MRZ7-F1",
                                 r'D:\data\database\UP000005640_9606_HUMAN\AF-A0A0A0MRZ7-F1-model_v1.cif')
mmcif_dict = MMCIF2Dict(r'D:\data\database\UP000005640_9606_HUMAN\AF-A0A0A0MRZ7-F1-model_v1.cif')
# sc = mmcif_dict['_exptl_crystal.density_percent_sol']

y_list = mmcif_dict["_atom_site.Cartn_y"]
print(y_list)