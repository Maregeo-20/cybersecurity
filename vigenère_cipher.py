L_alfabet = 'abcdefghijklmnopqrstuvwxyz'
U_alfabet = L_alfabet.upper()
special_caracter = '-_.,;:(){}"^<>'

ciphertext = 'Vhi Nixgnije tkplwr zu a tglpcltzasgtmu sldsxatlvisf czrhij. Ik ks e eoig sshhzutmuakgd zwrjkor gf kje Gsejcr gapygr, azitj uwws r uirylv uhmxt mclyw tf gngjygv tlw eevivw mvuseye. WNAK{yek_xikyy_nktl_at}'

def Vigenère_cipher_key(key, text):
    # Calcola la chiave
    key_n = [L_alfabet.index(char.lower()) for char in key]
    print("Chiave calcolata:", key_n)
    
    # Variabile per tracciare l'indice della chiave
    c = 0
    F_text = ''

    for f in range(len(text)):
        if text[f] in L_alfabet:
            F_text += L_alfabet[(L_alfabet.index(text[f]) - key_n[c]) % 26]
            c = (c + 1) % len(key_n)
        elif text[f] in U_alfabet:
            F_text += U_alfabet[(U_alfabet.index(text[f]) - key_n[c]) % 26]
            c = (c + 1) % len(key_n)
        elif text[f] in special_caracter:
            F_text += text[f]
        else:
            F_text += text[f]  # Per spazi e altri caratteri non presenti nelle liste
    
    print(F_text)

# Test del codice con l'esempio fornito
key = 'caesar'
Vigenère_cipher_key(key, ciphertext)


