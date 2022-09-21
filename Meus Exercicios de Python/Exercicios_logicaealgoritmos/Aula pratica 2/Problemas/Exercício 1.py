# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto
# a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto.
# (exercício da apostila – aula 2)

preco = float(input('Digite o preço de um produto: '))
p = float(input('Digite um percentual de desconto (0-100)%: '))

desconto = preco * (p / 100)
final = preco - desconto

print('O valor do produto é {}. O desconto será de {}%.' .format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}.' .format(desconto, final))