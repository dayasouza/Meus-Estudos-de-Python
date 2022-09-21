cadastro = {'nome':[], 'sexo':[], 'ano':[]}
cadastros = 0


while True:

    terminar = input('Deseja cadastrar uma pessoa? [S/N]: ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':

        print('Digite S para SIM ou N para NÃO')

        continue

    nome = input('Qual nome deseja cadastrar? ')
    sexo = input('Informe o sexo [M/F]: ')
    ano = int(input('Informe a data de nascimento: '))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

    cadastros += 1


print('Foram feitos {} cadastros' .format(cadastros))

print(cadastro, end=' ')
