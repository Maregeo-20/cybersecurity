def Vigenère_cipher(white_word, black_word, text):
    # Calcola la lunghezza della chiave
    key_length = len(black_word)
    
    # Calcola gli indici per white_word e black_word
    I_white_word = [L_alfabet.index(char.lower()) for char in white_word]
    I_black_word = [L_alfabet.index(char.lower()) for char in black_word]
    
    # Calcola la chiave
    key = [(I_black_word[i] - I_white_word[i]) % 26 for i in range(key_length)]
    print("Chiave calcolata:", key)
    
    # Variabile per tracciare l'indice della chiave
    c = 0
    F_text = ''

    for f in range(len(text)):
        if text[f] in L_alfabet:
            F_text += L_alfabet[(L_alfabet.index(text[f]) - key[c]) % 26]
            c = (c + 1) % key_length
        elif text[f] in U_alfabet:
            F_text += U_alfabet[(U_alfabet.index(text[f]) - key[c]) % 26]
            c = (c + 1) % key_length
        elif text[f] in special_caracter:
            F_text += text[f]
        else:
            F_text += text[f]  # Per spazi e altri caratteri non presenti nelle liste
    
    return F_text