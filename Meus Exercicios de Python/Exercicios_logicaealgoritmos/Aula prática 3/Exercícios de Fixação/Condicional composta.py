# a) Se ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso contrário, escreva: "Definitivamente não é um ano bissexto'
if(ano % 4 == 0):
    print('Pode ser um ano bissexto!')
else:
    print('Definitivamente não é um ano bissexto!')

# b) Se ambas as variáveis booleanas cima e baixo forem True, escreva: "Decida-se!". caso contrário, escreva: "Você escolheu um caminho"
if(cima and baixo == True):
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')