def perguntar():
    opcao = input('O que deseja realizar?' +
                  ' <I> - Para inserir um usuário' +
                  ' <P> - Para pesquisar um usuário' +
                  ' <E> - Para Excluir um usuário' +
                  ' <L> - Para listar um usuário: ').upper()
    return opcao

def inserir(dicionario):
    chave = input('Transação número: ').upper()
    dicionario[chave] = [input('Digite o usuário: ').upper(),
                       input('Digite o nome: ').upper(),
                       input('Digite a data de acesso(dd/mm/aaaa): '),
                       input('Digite a hora de acesso: '),
                       input(('Qual a ultima estação acessada: ')).upper()]

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print(f'Nome do usuário: {lista[0]}')
        print(f'Data do último acesso: {lista[1]}')
        print(f'Última estação acessada: {lista[2]}')

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print('Objeto apagado.')

def listar(dicionario):
    for k, v in dicionario.items():
        print('Objeto...')
        print(f'Login: {k}')
        print(f'Dados: {v}')
        print('**********************')