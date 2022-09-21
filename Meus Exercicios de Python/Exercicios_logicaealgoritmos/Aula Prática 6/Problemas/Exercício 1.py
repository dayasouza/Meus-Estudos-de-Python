palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
    print('\nPalavra: {}. Vogais: '. format(palavra.upper()), end='') #Imprime todas em maiúscula
    for letra in palavra:
        if letra.lower() in 'aeiou': #tudo em minuscula
            print(letra.upper(), end=' ') #imprime tudo em maiuscula