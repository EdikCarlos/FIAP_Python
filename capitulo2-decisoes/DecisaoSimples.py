nome = input('Nome do paciente: ')
idade = int(input('Idade: '))
prioridade = 'NÃO'
if idade >= 65:
    prioridade = 'SIM'

print(f'Paciente {nome} será atendido em breve, tem prioridade? {prioridade}')