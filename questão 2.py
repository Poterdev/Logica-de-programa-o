# Impressão do menu
print('---------Olá, meu nome é Erickson(4640380)---------')
print('------------Este programa irá auxiliar-------------')
print('---------        nas suas vendas        -----------\n')
print('***** Tamanho ****  Açai-AC  **** Cupuaçu-CP  *****')
print('*****    P    ****  R$ 11,00 ****   R$ 9,00   *****')
print('*****    M    ****  R$ 16,00 ****   R$ 14,00  *****')
print('*****    G    ****  R$ 20,00 ****   R$ 18,00  *****\n')

total_do_pedido = 0
valor = 0


def validando_sabor ():
    while True:
        # Coletando dados do sabor
        pedido = input('Digite aqui seu pedido Açai(AC) ou Cupuaçu(CP): ').upper()
        #validando dado
        if pedido != 'AC' and pedido != 'CP':
            print('Sabor inválido. Tente novamente.')
            continue
        else:
            break
    return pedido


def validando_tamanho ():
    while True:
        #coletando dado do tamanho
        tamanho = input('Escolha o tamanho desejado (P, M, G): ').upper()
        #validando dados
        if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
            print('Tamanho  inválido. Tente novamente.')
            continue
        else:
            break
    return tamanho

while True:
    pedido = validando_sabor ()
    tamanho =validando_tamanho ()

    #validando valor
    if pedido == 'AC':
        if tamanho == 'P':
            valor = 11
        elif tamanho == 'M':
            valor = 16
        elif tamanho == 'G':
            valor = 20
    elif pedido == 'CP':
        if tamanho == 'P':
            valor = 9
        elif tamanho == 'M':
            valor = 14
        elif tamanho == 'G':
                valor = 18

    
    # Imprimir o valor do pedido e somar
    print('O custo do seu pedido foi de: R$ {:.2f}'.format(valor))
    total_do_pedido += valor
    
    
    # Somando o pedido
    print('Total do pedido foi de: R$ {:.2f}'.format(total_do_pedido))

    #loop de pedidos
    i = input("Deseja mais alguma item(S/N): ").upper()
    if i == 'S':
        continue
    else:
        print("Obrigado pela preferência!!!")
        break
