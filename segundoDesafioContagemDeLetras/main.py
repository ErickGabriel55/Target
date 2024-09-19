"""2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;"""

# Lista de strings com letras "a"
listaString = ['abcdeswaTYioA', 'abacAxi', 'mangaba', 'lArAnjA', 'abcde']

# Loop for para percorrer e contar cada palavra/string por vez
for strings in listaString:
    lowerStrings = strings.lower() # Transforma todas em minusculas
    contagem = lowerStrings.count('a') # Faz a contagem
    print(f'A letra a apreceu {contagem} vezes em {strings}') # Exibe para o usuário
