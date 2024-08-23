
#tuplas

linguagens = ('rust', 'TyperScript', 'python', 'kotlin', 'go', 'julia', 'dart', 'c#', 'javascript',)

# codigo " for " para fazer varredura e lista

for i in range(0, len(linguagens), 1):
    # o primeiro iterador ser como numeração para o indice, e o proximo serve para identificar a posição do item na tupla)
    print(i+1, '-', linguagens[i])

# apenas os tres primeiros
    print(linguagens[:3])
    print(linguagens[-5:])


############   varredura para achar valor ######## (tuplas)

i=0
#encontrando valor na tupla
while linguagens[i] != 'python':
    i += 1
#aqui ele encontrou em uma posição anterior e adicionou mais 1 para indicar o indice do valor procurado
print( 'Encontrado python na {} posição'.format(i+1))

print('')
print('')
print('')
print('')
print('#'*100)
print('')
print('')
print('')
print('')
print('#'*50, 'Manipulando lista', '#'*50)

mochila = ['Machado', 'Camisa', 'Laranja', 'Abacate', 'Ovos']
mochila.append('Uva') #adicionando item no final da fila
mochila.insert(1,'Morango')#inserindo na posição especificada

#criando uma copia
x = [1,2,3,4,5]
y = x[:] #Usa o indicador [:] para que possa ser feito a alteração sem alterar as duas, entap cria uma copia mas com edição diferente

#tipo de varredura dupla undo o primeiro for identa o item da lista e o segundo faz a iteração do item dentro do item


for item in mochila:
    for letra in item:
        print(letra,end='')#o end esta impedindo de quando identar a letra passe para proxima sem pular de linha
    print()

#daria pra fazer deta forma tbm

i=0  
for i in range(0, len(mochila), 1):
    for j in range(0, len(mochila), 1):
        print(mochila[j], end='')
    print()
print("")
print("")
print("")
print("")
print("")
print("")

#crinado um tipo de cadastro

#lista do mercado

mercado = []

for i in range(3): #aqui vai cadatrar 3 itens
    nome = input("prodto: ")
    quan = int(input('quantidade: '))
    valor = float(input('valor: '))
    mercado.append([nome, quan, valor])#o importante da chave aqui é que esta criando uma lista dentro da lista em cada repetição

print(mercado)

#como identificar cada item na lista
print(mercado[2][0])# aqui pegaria cafe
