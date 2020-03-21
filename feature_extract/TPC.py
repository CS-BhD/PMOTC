import re


def tpc(fastas):
    protein = []
    aa = 'ACDEFGHIKLMNPQRSTVWY'
    encodings = []
    aa_dict = {}
    for i in range(len(aa)):
        aa_dict[aa[i]] = i
    for i in fastas:
        protein.append(i[0])
        sequence = re.sub('-', '', i[1])
        tmp_code = [0] * 8000
        for j in range(len(sequence) - 3 + 1):
            tmp_code[aa_dict[sequence[j]] * 400 + aa_dict[sequence[j+1]]*20 + aa_dict[sequence[j+2]]] = tmp_code[aa_dict[sequence[j]] * 400 + aa_dict[sequence[j+1]]*20 + aa_dict[sequence[j+2]]] +1
        if sum(tmp_code) != 0:
            tmp_code = [i/sum(tmp_code) for i in tmp_code]
        encodings.append(tmp_code)
    return protein, encodings

