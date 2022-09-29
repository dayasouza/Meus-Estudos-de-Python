acumulador = 0 #Muito importante o zero
acumuladorTexto = ''
print('Seja bem vindo ao Salão de Beleza da Dayana Alves de Souza')
print('------------Opções de Serviço-----------')
print('| Código |      Descrição     |  Valor |')
print('|   cc   |   Corte de Cabelo  |  80,00 |')
print('|   pe   | Penteado Elaborado | 220,00 |')
print('|   pi   |       Pintura      | 120,00 |')
print('|   pr   |     Progressiva    | 450,00 |')
print('|   es   |        Escova      | 100,00 |')
print('----------------------------------------')
while True:
    codigo = input('Entre com o código desejado: ')
    if codigo == 'cc':
        acumulador = acumulador + 80 #Acumulador, guarda o valor final do serviço
        acumuladorTexto = acumuladorTexto + '\n|   Corte de Cabelo  |  80,00 |'
    elif codigo == 'pe':
        acumulador = acumulador + 220
        acumuladorTexto = acumuladorTexto + '\n| Penteado Elaborado | 220,00 |'
    elif codigo == 'pi':
        acumulador = acumulador + 120
        acumuladorTexto = acumuladorTexto + '\n|       Pintura      | 120,00 |'
    elif codigo == 'pr':
        acumulador = acumulador + 450
        acumuladorTexto = acumuladorTexto + '\n|     Progressiva    | 450,00 |'
    elif codigo == 'es':
        acumulador = acumulador + 100
        acumuladorTexto = acumuladorTexto + '\n|        Escova      | 100,00 |'
    else:
        print('Código inválido!')
        continue
    print('O valor a ser pago está em: R$ {:.2f}' .format(acumulador))
    resposta = input('Deseja mais algum serviço? (s/n) ')
    if resposta == 's':
        continue
    else:
        print('Os serviços contratados são: ' + acumuladorTexto)
        print('O valor final da conta é: {:.2f}' .format(acumulador))
        break