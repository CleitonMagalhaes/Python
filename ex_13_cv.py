#Reajuste salarial
salario = float(input('Qual é o salário do Funcionário? R$'))
nvalor = salario+(salario*0.15)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, nvalor))