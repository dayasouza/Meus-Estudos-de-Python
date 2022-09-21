#Faça um algoritmo que receba 3 valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
#Equilátero (três lados iguais)
#Esósceles (dois lados iguais)
#Escaleno (três lados diferentes)
#Lembre-se que, para formar um triângulo nenhum dos lados pode ser igual a 0, e um lado não pode ser maior do que a soma dos outros dois (exercício apostil - aula 3)
A = int(input('Digite o 1° lado do triângulo:'))
B = int(input('Digite o 2º lado do triângulo:'))
C = int(input('Digite o 3º lado do triângulo:'))
if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C ) and (A + C > B) and (B + C > A):
    # Se você chegou até aqui, é porque o triângulo é válido!
        if (A != B) and (A != C) and (B != C):
            print('Triângulo escaleno!')
        else:
            if (A == B) and (A == C) and (B == C):
                print('Triângulo equilátelo!')
            else:
                print('Triângulo isósceles!')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')