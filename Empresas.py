'''Algortimo para cadastrar empresas e gravar em um arquivo json'''

import json

#cadastrar empresas
def cadastro():
    empresas = []
    empresa = {}
    while True:
        #dados da empresa
        id = int(input('ID da empresa: '))
        for valor in empresas: #verificando se o ID já existe
            if valor['id'] == id:
                print('ID já cadastrado')
                break
        else:
            nome = input('Nome da empresa: ')
            ano = int(input('Ano de fundação: '))
            porte = input('Porte: ')
            ramo = input('Ramo de atividade: ')

            #armazenando dados em uma lista de dicionarios
            empresa = {'id': id, 'nome': nome, 'ano': ano, 'porte': porte, 'ramo': ramo}
            empresas.append(empresa)
            print (f'A empresa {nome} foi cadastrada com sucesso')
            opcao = input('Deseja cadastrar outra empresa? (s/n): ')
            if opcao == 'n' or opcao == 'N':
                break
    return empresas


#listar todas as empresas
def listar(empresas):
    print('Listagem de empresas\n')
    for empresa in empresas:
        print('_' * 20)
        print(f'ID: {empresa["id"]}')
        print(f'Nome: {empresa["nome"]}')
        print(f'Ano de fundação: {empresa["ano"]}')
        print(f'Porte: {empresa["porte"]}')
        print(f'Ramo de atividade: {empresa["ramo"]}')
        print('_' * 20)
    

#pesquisar uma empresa pelo ID
def pesquisar(empresas):
    print('Pesquisa de empresas')
    id = int(input('ID da empresa: '))
    for empresa in empresas:
        if empresa['id'] == id:
            print (f'Nome: {empresa["nome"]}')
            print (f'Ano de fundação: {empresa["ano"]}')
            print (f'Porte: {empresa["porte"]}')
            print (f'Ramo de atividade: {empresa["ramo"]}\n')    
            break
    else:
        print('Empresa não encontrada')


#alterar os dados de uma empresa
def alterar(empresas):
    print('Alteração de empresas')
    id = int(input('ID da empresa: '))
    for empresa in empresas:
        if empresa['id'] == id:
            print (f'Nome: {empresa["nome"]}')
            print (f'Ano de fundação: {empresa["ano"]}')
            print (f'Porte: {empresa["porte"]}')
            print (f'Ramo de atividade: {empresa["ramo"]}')
            opcao = input('Deseja alterar os dados da empresa? (S/N): ')
            if opcao == 's' or opcao == 'S':
                nome = input('Nome da empresa: ')
                ano = int(input('Ano de fundação: '))
                porte = input('Porte: ')
                ramo = input('Ramo de atividade: ')
                empresa['nome'] = nome
                empresa['ano'] = ano
                empresa['porte'] = porte
                empresa['ramo'] = ramo
                print('Dados alterados com sucesso\n')
                break
            if opcao == 'n' or opcao == 'N':
                print('Alteração cancelada\n')
                break
        else:
            print('Empresa não encontrada\n')


#excluir uma empresa
def excluir(empresas):
    print('Exclusão de empresas')
    id = int(input('ID da empresa: '))
    for empresa in empresas:
        if empresa['id'] == id:
            opcao = input(f'Deseja excluir a empresa {empresa["nome"]} (S/N): ')
            if opcao == 's' or opcao == 'S':
                empresas.remove(empresa)
                print('Empresa excluída com sucesso\n')
                break
            if opcao == 'n' or opcao == 'N':
                print('Exclusão cancelada\n')
                break
        else:
            print('Empresa não encontrada\n')


#gravar os dados em um arquivo json
def gravar(empresas):
    #abrir o arquivo para escrita
    arquivo = open('empresas.json', 'w')
    #converter a lista de dicionarios em uma string json
    json.dump(empresas, arquivo)
    #fechar o arquivo
    arquivo.close()
    print('Dados gravados com sucesso')
    

#menu
def menu():
    opcao = 0
    while opcao != 7:
        print('Menu de opções:')
        print('1 - Cadastrar empresas')
        print('2 - Listar todas as empresas cadastradas')
        print('3 - Pesquisar uma empresa pelo ID')
        print('4 - Alterar os dados de uma empresa')
        print('5 - Excluir uma empresa')
        print('6 - Gravar os dados em um arquivo json')
        print('7 - Sair')
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            empresas = cadastro()
        elif opcao == 2:
            listar(empresas)
        elif opcao == 3:
            pesquisar(empresas)
        elif opcao == 4:
            alterar(empresas)
        elif opcao == 5:
            excluir(empresas)
        elif opcao == 6:
            gravar(empresas)
        elif opcao == 7:
            print('Fim do programa')
        else:
            print('Opção inválida')

menu()
