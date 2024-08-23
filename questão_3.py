# Impressão do menu
print('---------Olá, meu nome é Erickson(4640380)---------')
print('------------Este programa irá auxiliar-------------')
print('---------        nas suas vendas        -----------\n')


servico = ''
#criar menu
def escolha_serviço ():
    print('Menu de serviço.')
    print('DIG - Digitalização R$ 0,75')
    print('ICO - Impressão Colorida R$ 1,00')
    print('IPB - Impressão Preto e Branco R$ 0,50')
    print('FOT - Fotocópia R$ 0,25')
    
    while True:
        servico = input('Escolha o tipo de serviço: ').upper()
        if servico != 'DIG' and servico != 'ICO' and servico != 'IPB' and servico != 'FOT':
            print('Serviço Inválido. Tente Novamente.')
            continue
        else:
            break
    
    return servico


def num_paginas():
    while True:
        try:
            num_paginas = int(input("Entre com o número desejado de páginas: "))
            if num_paginas >= 20000:
                print('Limite de páginas ultrapassado. Favor inserir um número abaixo de 20 mil.')
                continue
            else:
                break
        except ValueError:
            print("Por favor, digite um número válido.")

    return num_paginas



def servico_extra():
    print('Serviços extras!!!')
    print('1 - Encadernação Simples - R$ 15,00')
    print('2 - Encadernação Capa Dura - R$ 40,00')
    print('3 - Sem Adicional')

    while True:
        try:
            servico_extra = input('Deseja adicionar um serviço extra? (Digite o número correspondente ao serviço ou "3" para Sem Adicional): ')
            servico_extra = int(servico_extra)

            if servico_extra not in [1, 2, 3]:
                print("Opção inválida. Digite 1, 2 ou 3.")
                continue

            break
        except ValueError:
            print("Por favor, digite apenas numeros.")
    return servico_extra


def calcular_desconto_paginas(x,y):
    # x é a quantidade de pagina
    # y é o valor total
    if x < 20:
        return y
    elif 20 <= x < 200:
        return float(y * 0.85)
    elif 200 <= x < 2000:
        return float(y * 0.80)
    elif 2000 <= x < 20000:
        return float(y * 0.75)

# valor dos serviços
valor_dig = 0.75
valor_ico = 1.00
valor_ipb = 0.50
valor_fot = 0.25

#programa princpal
servico = escolha_serviço()
quantidade = num_paginas()
adicional = servico_extra()
if adicional == 1:
    adicional_final = 15
elif adicional == 2:
    adicional_final = 40
else:
    adicional_final = 0 

valor_total = 0

if servico == 'DIG':
    valor_total = quantidade * valor_dig
elif servico == 'ICO':
    valor_total = quantidade * valor_ico
elif servico == 'IPB':
    valor_total = quantidade * valor_ipb
else:
    valor_total = quantidade * valor_fot

valor_final = float(calcular_desconto_paginas(quantidade,valor_total))
valor_final2 = float(valor_final + adicional_final)
print('O valor final das impressões: R$ {:.2f} + R$ {:.2f} de adicional'.format(valor_final,adicional_final))
print('Valor total a pagar: R$ {:.2f}'.format(valor_final2))






