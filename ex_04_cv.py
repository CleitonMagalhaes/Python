#Tipos de formatos de texto e input
a = input("Digite algo:")
print("O tipo primitivo desse valor é", type(a))
print("É só espaços?", a.isspace())
print("É um número?", a.isnumeric())
print("É alfabético?", a.isalpha())