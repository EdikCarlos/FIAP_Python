n = int(input('Digite um numero para ver sua tabuada: '))
vezes = int(input('Digite por quantos números você quer que esse número seja multiplicado: '))

for i in range(1, vezes+1, 1):
    print(f'{n} x {i} = {n*i}')