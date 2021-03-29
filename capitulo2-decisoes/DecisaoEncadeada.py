nivel = input('Digite o nível de acesso: ADM, USR ou GUEST: ').upper()
sexo = input('Qual o seu gênero? M ou F?: ').upper()

if nivel == 'ADM':
    if sexo == 'M':
        print('Olá administrador')
    elif sexo == 'F':
        print('Olá administradora')
    else:
        print('Digite apenas M(masculino) ou F(feminino)')

if nivel == 'USR':
    if sexo == 'M':
        print('Olá usuário')
    elif sexo == 'F':
        print('Olá usuária')
    else:
        print('Digite apenas M(masculino) ou F(feminino)')

if nivel == 'GUEST':
    print('Olá visitante')

if nivel != 'USR' and nivel != 'ADM' and nivel != 'GUEST':
    if sexo == 'M':
        print('Olá desconhecido')
    elif sexo == 'F':
        print('Olá desconhecida')
    else:
        print('Digite apenas M(masculino) ou F(feminino)')