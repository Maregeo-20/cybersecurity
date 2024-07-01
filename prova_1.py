# Your frequencies
your_frequencies =        "SLXWVAUDZFCNMRXTOIGPKHEQYBJ"

# Traditional frequencies
traditional_frequencies = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Assumptions
assumptions = {
    'P': 'T',
    'D': 'H',
    'V': 'E',
    'A': 'F',
    'N': 'L',
    'S': 'A',
    'U': 'G'
}

# Adjust the remaining mappings
remaining_traditional = [c for c in traditional_frequencies if c not in assumptions.values()]
remaining_your = [c for c in your_frequencies if c not in assumptions.keys()]

# Create the final mapping dictionary
mapping = {**assumptions}
mapping.update({remaining_your[i]: remaining_traditional[i] for i in range(len(remaining_your))})

# Decode the text
text = 'PDV KLRBC IOEXQ AEY TLGMF EJVO PDV NSWH ZEU. PDRF PVYP RF S MSQUOSG, XDRBD GVSQF PDSP RP BEQPSRQF SNN 26 NVPPVOF EA PDV VQUNRFD SNMDSIVP. PDRF GSCVF RP RZVSN AEO AOVKLVQBH SQSNHFRF, SF PDV BOHMPSQSNHFP BSQ BEGMSOV PDV AOVKLVQBH EA NVPPVOF RQ PDV BRMDVOPVYP PE PDV CQEXQ AOVKLVQBH EA NVPPVOF RQ PDV VQUNRFD NSQULSUV. AEO VYSGMNV, PDV GEFP BEGGEQ NVPPVO RQ PDV VQUNRFD NSQULSUV RF V. RA PDV GEFP BEGGEQ NVPPVO RQ PDV BRMDVOPVYP RF Y, PDVQ PDV BOHMPSQSNHFP BSQ SFFLGV PDSP Y RF NRCVNH PE IV S FLIFPRPLPREQ AEO V. EPDVO BEGGEQ NVPPVOF RQ PDV VQUNRFD NSQULSUV RQBNLZV P, S, E, R, Q, F, SQZ D. PDV BOHMPSQSNHFP BSQ L V PDRF RQAEOGSPREQ PE GSCV VZLBSPVZ ULVFFVF SIELP PDV EPDVO FLIFPRPLPREQF RQ PDV BRMDVOPVYP. ANSU{QEX_RJV_NVSOQVZ_GH_SIBF}'
decoded_text = ''

for char in text:
    if char in mapping:
        decoded_text += mapping[char]
    else:
        decoded_text += char

print(decoded_text)
