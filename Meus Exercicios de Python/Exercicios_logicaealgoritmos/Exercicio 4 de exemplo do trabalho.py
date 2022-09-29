listaEstudantes = []
#---------- COMEÇO cadastrarEstudante ----------
def cadastrarEstudante(ra):
    print("Bem-vindo ao CADASTRAR de estudantes")
    print(" O RA do estudante a ser cadastrado é: {}" .format(ra))
    nome = input("Digite o nome do estudante: ")
    turma = input("Digite a turma do estudante: ")
    dicionarioEstudante = {'ra': ra,
                           'nome': nome,
                           'turma': turma}
    listaEstudantes.append(dicionarioEstudante.copy())

#----------- FIM cadastrarEstudante ------------

#---------- COMEÇO consultarEstudante ----------
def consultarEstudante():
    while True:
        try:
            print("Bem-vindo ao CONSULTA de estudantes")
            opConsultar = int(input("Entre com a opção Desejada:\n"
                                    "1 - Consultar Todos os Estudantes\n"
                                    "2 - Consultar por RA\n"
                                    "3 - Consultar por Turma\n"
                                    "4 - Retornar\n"
                                    ">> "))
            if opConsultar == 1:
                print("Bem vindo ao Consultar TODOS")
                for estudante in listaEstudantes: #selecionar cada dicionário da minha lista (cada estudante da lista de estudantes)
                    for key, value in estudante.items(): #selecionar cada conjunto (chave : valor) do dicionários
                        print("{} : {}" .format(key, value))
            elif opConsultar == 2:
                print("Bem vindo à Consulta por RA")
                entrada = int(input("Digite o RU que deseja consultar: "))
                for estudante in listaEstudantes:
                    if(estudante['ra']) == entrada:
                        for key, value in estudante.items():
                            print("{} : {}" .format(key,value))
                    else:
                        print("Você digitou um RA inexistente. Tente novamente")
            elif opConsultar == 3:
                print("Bem vindo à Consulta por TURMA")
                entrada = input("Digite a turma que deseja consultar: ")
                for estudante in listaEstudantes:
                    if(estudante['turma']) == entrada:
                        for key, value in estudante.items():
                            print("{} : {}" .format(key,value))
                    else:
                        print("Você digitou uma Turma inexistente. Tente novamente!")
            elif opConsultar == 4:
                print("Retornando ao Menu Principal")
                break
            else:
                print("Opção inválida. Tente novamente")
                continue
        except ValueError:
            print("Você digitou um valor não aceito. Tente novamente")

#---------- FIM consultarEstudante -------------

#----------- COMEÇO removerEstudante -----------
def removerEstudante():
    print("Bem-vindo ao REMOVER estudantes")
    entrada = int(input("Digite o RA do estudante que deseja remover: "))
    for estudante in listaEstudantes:
        if (estudante['ra'] == entrada):
            listaEstudantes.remove(estudante)
        else:
            print("Você digitou um RU inválido. Tente novamente.")

#------------ FIM removerEstudante -------------

#----------------- COMEÇO MAIN -----------------
print("Bem-vindo ao PROGRAMA CONTROLE DE ESTUDANTES de Dayana Alves de Souza")
registroAcademico = 0
while True:
    try:
        opcao = int(input("Digite a opção desejada:\n"
                        "1 - Cadastrar Estudante\n"
                        "2 - Consultar Estudante\n"
                        "3 - Remover Estudante\n"
                        "4 - Sair\n"
                        ">> "))
        if opcao == 1:
            registroAcademico += 1
            cadastrarEstudante(registroAcademico)
        elif opcao == 2:
            consultarEstudante()
        elif opcao == 3:
            removerEstudante()
        elif opcao == 4:
            print("Encerrando o programa")
            break
        else:
            print("Opção Inexistente! Tente novamente!")
            continue
    except ValueError:
        print("Você digitou um valor não aceito. Tente novamente")

#------------------ FIM MAIN ------- ------------