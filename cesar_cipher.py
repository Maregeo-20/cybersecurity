L_alfabet = 'abcdefghijklmnopqrstuvwxyz'
U_alfabet = L_alfabet.upper()
special_caracter = '-_.,;:(){}"^<>'

def Cesar_cipher(text):
    
    for k in range(1000):
        F_text = ''  # Reset F_text for each shift
        for i in range(len(text)):
            if text[i] in L_alfabet:
                F_text += L_alfabet[(L_alfabet.index(text[i]) - k) % 26]
            elif text[i] in U_alfabet:
                F_text += U_alfabet[(U_alfabet.index(text[i]) - k) % 26]
            elif text[i] in special_caracter:
                F_text += text[i]
            else:
                F_text += text[i]  # For spaces and other characters not in the lists
        
        for j in range(len(F_text) - 3):
            if F_text[j] == 'F' and F_text[j+1] == 'L' and F_text[j+2] == 'A' and F_text[j+3] == 'G':
                print(f"Found 'FLAG' with shift {k}: {F_text}")
                print(F_text)
        


Cesar_cipher('iodj{irro_zkr_uhdgv}')
