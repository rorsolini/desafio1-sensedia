import os

pasta = 'C://Users/usr/Downloads/desafio' #colocar o caminho da pasta do desafio e inverter as barras de \\ para //
def filtro(txt):
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.lower().find(txt.lower()) > -1:
                print(arquivo)

def delete(txt):
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.lower().find(txt.lower()) > -1:
                os.remove(diretorio + '\\' + arquivo)
                    



numero = ''
while numero != '0':
    print('------------------------ \n\n')
    numero = input('O que deseja filtrar: \n1 - Calls \n2 - Metrics \n3 - Data \n4 - Cliente \n5 - Sair \nInforme o número: ')
    print('------------------------ \n\n')
    
    if numero == '1':
        print('Filtrando arquivos por CALLS:')
        filtro('calls')

    elif numero == '2':
        print('Filtrando arquivos por METRICS:')
        filtro('metrics')

    elif numero == '3':
        print('Filtrando arquivos por DATA:')
        ano = input('Informe o ano: ')
        mes = input('Informe o mes: ')
        dia = input('Informe o dia: ')

        data = ano + '_' + mes.zfill(2) + '_' + dia.zfill(2)
        filtro(data)

    elif numero == '4':
        print('Filtrando arquivos por CLIENTE:')
        cliente = input('Informe o nome do cliente que deseja filtrar (exemplo: cliente1, cliente2...cliente10): ')
        if cliente != '':
            filtro (cliente)
            delete(cliente)

        else:
            print('Opção inválida para filtro!')
   
    elif numero == '5':
        print('Saindo do Sistema...')
        break        

    else:
        print('Opção Inválida! Favor inserir opção novamente \n')
