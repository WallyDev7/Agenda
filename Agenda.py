AGENDA = {}


def mostrar_contatos():
    try:
        print('Mostrando todos os contatos: \n')
        for contato in AGENDA:
            buscar_contatos(contato)
        print('FIM')
    except KeyError:
        print('Nenhum contato encontrado')
    except Exception as erro:
        print('Erro inesperado')
        print(erro)


def buscar_contatos(contato):
        try:
            print('Nome: ', contato)
            print('Telefone: ', AGENDA[contato]['Telefone'])
            print('Email: ', AGENDA[contato]['Email'])
            print('Endereco: ', AGENDA[contato]['Endereco'])
            print('--------------------------------------------')
        except Exception as erro:
            print('Contato nao encontrado')
            print(erro)


def ler_detelhes_contato():
    telefone = input('Digite o nome do telefone: ')
    email = input('Digite o nome do email: ')
    endereco = input('Digite o nome do endereco: ')
    return telefone, email, endereco


def incluir_editar_contatos(contato, telefone, email, endereco):

     
    AGENDA[contato] = {
        'Telefone': telefone,
        'Email': email,
        'Endereco': endereco,  
    }
    print('\nContato {} adicionado/editado com sucesso'.format(contato))


def excluir_contatos(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print('\nContato {} excluido com sucesso'.format(contato)) 
    except KeyError:
        print('Contato nao encontrado')
        print(erro)
    except Exception as erro:
        print('Erro inesperado')
        print(erro)


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['Telefone']
                email = AGENDA[contato]['Email']
                endereco = AGENDA[contato]['Endereco']
                arquivo.write('{},{},{},{}\n'.format(contato, telefone, email, endereco))
        print('Agenda exportada com sucesso!!!')
    except Exception as erro:
        print('Erro: {}'.format(erro))


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

            incluir_editar_contatos(nome, telefone, email, endereco)
    except Exception as erro:
        print('Erro inesperado')
        print(erro)


def salvar():
    exportar_contatos('database.csv')
    

def carregar():
    importar_contatos('database.csv')


def imprimir_menu():
    print('''
------------------------------------------
1 - Mostrar todos os contatos
2 - Buscar contato
3 - Incluir contato
4 - Editar contato
5 - excluir contato
6 - Exportar contatos .csv
7 - Importar contatos .csv
0 - Sair
------------------------------------------
''')

#INICIO DO PROGRAMA

carregar()
while True:
    imprimir_menu()

    opcao = input('Escolha uma opcao: ')

    print('\n--#--#--#--#--#--#--#--#--#--#\n')

    if opcao == '0':
        salvar()
        print('>>>> Fechando programa')
        break

    elif opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('Digite o nome do contato que deseja buscar: ')
        print('\nMostrando o contato do {}:\n'.format(contato))
        buscar_contatos(contato)

    elif opcao == '3':
        contato = input('Digite o nome do contato que deseja incluir: ')

        try:
            AGENDA[contato]
            print('Ja existe um contato com o nome: {}'.format(contato))

        except KeyError:
            telefone, email, endereco = ler_detelhes_contato()
            incluir_editar_contatos(contato, telefone, email, endereco)

    elif opcao == '4':
        contato = input('Digite o nome do contato que deseja editar: ')

        try:
            AGENDA[contato]
            telefone, email, endereco = ler_detelhes_contato()
            incluir_editar_contatos(contato, telefone, email, endereco)
        except KeyError:
            print('Nao foi encontrado um contato com o nome: {}'.format(contato))
    
    elif opcao == '5':
        contato = input('Digite o nome do contato que deseja excluir: ')
        excluir_contatos(contato)
   
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo: ')
        exportar_contatos(nome_do_arquivo)

    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo: ')
        importar_contatos(nome_do_arquivo)

    else:
        print('>>>> Opção inválida')
    print()
