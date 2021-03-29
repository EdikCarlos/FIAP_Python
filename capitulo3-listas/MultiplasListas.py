equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamentos.append(input("Departamento: "))
  resposta = input("Digite 'S' para continuar: ").upper()

for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print(f"Valor........:  R${valores[indice]}")
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])
  print('**********************************')

depressiar = input(" Digite o nome do equipamento que deseja diminuir 10% : ")
for i in range(0, len(equipamentos)):
    if depressiar == equipamentos[i]:
        print("Valor Antigo..: ", valores[i])
        valores[i] =valores[i] - (valores[i] * 10 / 100)
        print("Valor Novo..: ", valores[i])
        print('**********************************')

danificado = int(input("Digite o numero de serial do equipamento danificado: "))
for i in range(0, len(seriais)):
    if danificado == seriais[i]:
        deletado = equipamentos[i]
        del equipamentos[i]
        del seriais[i]
        del valores[i]
        del departamentos[i]
        print(f'Item {deletado} deletado com sucesso!!!')
        break


