from Funcoes.Funcoes_Dicionarios import *

usuarios = {}
opcao = perguntar()
while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        inserir(usuarios)
    elif opcao == 'P':
        pesquisar(usuarios, input('Qual login deseja pesquisar? ').upper())
    elif opcao == 'E':
        excluir(usuarios, input('Qual login deseja excluir? ').upper())
    elif opcao == 'L':
        listar(usuarios)
    opcao = perguntar()