with open("economic-indicators.csv","r") as boston:
    total_voos=0
    maior = 0
    total_passageiros = 0
    media_hotel = 0
    ano_usuario = input('Qual ano você quer verificar, 2013 ou 2014?: ')
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(',')
        total_voos += float(lista[3])
        if float(lista[2])>float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        if ano_usuario == lista[0]:
            total_passageiros += float(lista[2])
            if float(lista[4])> float(media_hotel):
                media_hotel = lista[4]
                mes_hotel = lista[1]
    print("O total de voos é: ", total_voos)
    print(f'O máximo de passageiros em um mês foi: {maior} e ocorreu no mês {mes} do ano {ano}!')
    print(f'O total de passageiros no ano {ano_usuario} foi de {total_passageiros}')
    print(f'A maior media diaria de um hotel foi de {media_hotel} no mes {mes_hotel}')