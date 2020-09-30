#Importando função de bibliotecas
from math import trunc

num = float(input("Digite um valor númerico: "))
print("O valor digitado foi {:.2f} e seu representativo inteiro é {}." .format(num, trunc(num)))
