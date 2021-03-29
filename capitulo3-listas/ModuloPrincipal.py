from capitulo_3_Funcoes.IndentificacaoDeFuncoes import *

inventario = []

print('***Preenchimento***')
preencherInventario(inventario)
print('***Exibindo***')
exibirInventario(inventario)

print('***Pesquisando***')
localizarPorNome(inventario)
print('***Desconto***')
depreciarPorNome(inventario, 50)

print('***Excluindo***')
print(excluirPorSerial(inventario))
exibirInventario(inventario)

print('***Resumindo***')
resumirValores(inventario)