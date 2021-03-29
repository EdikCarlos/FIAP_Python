ips={}
resp="S"
while resp=="S":
    ips[(input("Digite os dois primeiros octetos: "),
       input("Digite os dois últimos octetos: "))]=input("Nome da máquina: ").upper()
    resp=input("Digite <S> para continuar: ").upper()

print("Exibindo ip's: ")
for ip in ips.keys():
    print(f'{ip[0]}.{ip[1]}')

print("Exibindo máquinas com o mesmo endereço: ")
pesquisa=input("Digite os dois últimos octetos: ")
for ip,nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if(ip[1]==pesquisa):
        print(nome)
        print('**********************')
    else:
        print('Nenhuma máquina')
        print('**********************')

print('Exibindo as estações das máquinas com o mesmo endereço: ')
rede = input('Digite os dois primeiros octetos: ')
for k, v in ips.items():
    print('Estações: ')
    if(k[0] == rede):
        print(f'{v}')