#Calculando descontos
valor = float(input('Qual é o preço do produto? R$'))
desc = valor-(valor*0.05)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(valor, desc))