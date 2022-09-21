#Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar:
#adição (+)
#subtração (-)
#multiplicação (*)
#divisão (/)
#Exiba na tela o resultado da operação desejada (exercício da apostila aula 3)
print('CALCULADORA:')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione qualquer tecla para sair')

op = input('Qual operação deseja fazer? ')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

if (op == '+'): #deve-se colocar o sinal entre aspas simples para o computador perceber que é um simbolo, do contrário ele vai fazer uma operação com ele.
    res = (x + y)
    print('Resultado: {} + {} = {}' .format(x, y, res))
elif (op == '-'):
    res = (x - y)
    print('Resultado: {} - {} = {}' .format(x, y, res))
elif (op == '*'):
    res = (x * y)
    print('Resultado: {} * {} = {}' .format(x, y, res))
elif (op == '/'):
    res = (x / y)
    print('Resultado: {} / {} = {}' .format(x, y, res))
else:
    print('Operação inválida')

print('Encerrando o programa...')