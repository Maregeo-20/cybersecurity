L_alfabet = 'abcdefghijklmnopqrstuvwxyz'
U_alfabet = L_alfabet.upper()
special_caracter = '-_.,;:(){}"^<>'

def Vigenère_cipher(white_word, black_word, text):
    I_white_word = []
    I_black_word = []
    F_text = ''

    # Calcola gli indici per white_word e black_word
    for i in range(len(white_word)):
        I_white_word.append(L_alfabet.index(white_word[i].lower()))
    for i in range(len(black_word)):
        I_black_word.append(L_alfabet.index(black_word[i].lower()))

    # Calcola la chiave
    key = []
    for k in range(len(I_black_word)):
        diff = (I_black_word[k] - I_white_word[k]) % 26
        key.append(diff)
    print("Chiave calcolata:", key)
    
    c = 0  # Variabile per tracciare l'indice della chiave
    
    for f in range(len(text)):
        if text[f] in L_alfabet:
            F_text += L_alfabet[(L_alfabet.index(text[f]) - key[c]) % 26]
            c = (c + 1) % len(key)
        elif text[f] in U_alfabet:
            F_text += U_alfabet[(U_alfabet.index(text[f]) - key[c]) % 26]
            c = (c + 1) % len(key)
        elif text[f] in special_caracter:
            F_text += text[f]
        else:
            F_text += text[f]  # Per spazi e altri caratteri non presenti nelle liste
    
    print(F_text)

# Test del codice con l'esempio fornito
Vigenère_cipher('WNAK', 'FLAG', 'Vhi Nixgnije tkplwr zu a tglpcltzasgtmu sldsxatlvisf czrhij. Ik ks e eoig sshhzutmuakgd zwrjkor gf kje Gsejcr gapygr, azitj uwws r uirylv uhmxt mclyw tf gngjygv tlw eevivw mvuseye. WNAK{yek_xikyy_nktl_at}')
