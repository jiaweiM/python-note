from numpy import promote_types
import pandas as pd

# 蛋白质序列
ProteinSequence = 'GLSDGEWQQVLNVWGKVEADIAGHGQEVLIRLFTGHPETLEKFDKFKHLKTEAEMKASEDLKKHGTVVLTALGGILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISDAIIHVLHSKHPGDFGADAQGAMTKALELFRNDIAAKYKELGFQG'
# 氨基酸信息
AA_Info_File = r'/Users/liuzheyi/Desktop/Python/Amino_acid_fragment_ions.xlsx'
AA_Info = pd.read_excel(AA_Info_File)

# 计算蛋白质的质量
ProMass = 0
for AA in ProteinSequence:
    AA_Mass = AA_Info.ResidueMass[AA_Info.Code1 == AA]
    ProMass += AA_Mass.iat[0]
ProMass = ProMass + 18.01528

# calculate the masses of N-terminal fragment ions
Masses = pd.DataFrame(columns=('Index', 'a', 'b', 'c', 'a1', 'x', 'x1', 'y', 'y1', 'z'))
b = 0
a = 0
c = 0
a1 = 0
n = 0
y = 0
x = 0
y1 = 0
x1 = 0
z = 0

for Ind in range(1, len(ProteinSequence) + 1):
    c_AA = ProteinSequence[Ind - 1]
    n_AA = ProteinSequence[len(ProteinSequence) - Ind]
    c_AA_Mass = AA_Info.ResidueMass[AA_Info.Code1 == c_AA]
    n_AA_Mass = AA_Info.ResidueMass[AA_Info.Code1 == n_AA]
    b = b + c_AA_Mass.iat[0]
    a = b - 27.99491
    c = b + 17.02655
    a1 = a + 1.007825
    n = n_AA_Mass.iat[0] + n
    y = n + 18.01056
    x = n + 43.98983
    y1 = y - 1.007825
    x1 = x + 1.007825
    z = y - 16.01872
    Masses = Masses.append(pd.DataFrame(
        {'Index': [Ind], 'a': [a], 'b': [b], 'c': [c], 'a1': [a1], 'x': [x], 'x1': [x1], 'y': [y], 'y1': [y1],
         'z': [z]}), ignore_index=True)

Masses_apo = Masses.melt(id_vars='Index', var_name='IonName', value_name='monoisotopic mass')
Masses_apo['IonType'] = 'Apo'
##加入含有配体的质量
LigandMass = 615.1695
Masses_holo = Masses + LigandMass
Masses_holo['Index'] = range(1, len(ProteinSequence) + 1)
Masses_holo = Masses_holo.melt(id_vars='Index', var_name='IonName', value_name='monoisotopic mass')
Masses_holo['IonType'] = 'Holo'

result_Masses = pd.concat([Masses_apo, Masses_holo])

result_Masses.to_excel('Calculated mass of native myoglobin with heme.xlsx')
