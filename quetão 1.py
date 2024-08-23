
print("-------Olá, meu nome é Erickson(4640380)-------")
print("----------Este programa irá auxiliar-----------")
print("-------No seu desconto, nas suas vendas -------")

produto = float(input("Digite aqui o valor do produto (ex: 120.22): "))
quantidade = int(input("Digite a quantidade do produto: "))
total = float(produto*quantidade)

if total >= 2500 and total < 6000:
  desc_4 =float(total - (total*0.04))
  print("O valor do seu produto com desconto é: {:.2f}(desconto de 4%)".format(desc_4))
elif total >= 6000 and total < 10000:
  desc_7 = float(total - (total*0.07))
  print("O valor do seu produto com desconto é: {:.2f}(desconto de 7%)".format(desc_7))
elif total >= 10000:
  desc_11 = float(total - (total*0.11))
  print("O valor do seu produto com desconto é: {:.2f}(desconto de 11%)".format(desc_11))
else:
  print("O valor do seu produto sem desconto é: {:.2f}".format(total))