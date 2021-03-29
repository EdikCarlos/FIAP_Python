from Funcoes.Funcoes_Arquivos import *

inventario={}

opcao = chamarMenu()

while opcao > 0 and opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        print(persistir(inventario))
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            lista = linha.split(';')
            print(f'DATA: {lista[1]}')
            print(f'DESCRIÇÃO: {lista[2]}')
            print(f'DEPARTAMENTO: {lista[3]}')
            print('*****************')

    opcao = chamarMenu()