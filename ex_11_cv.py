#Calculo de area e tinta em litros
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
tinta = area/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.03f}m².'.format(largura,altura,area))
print('Para pintar essa parede, você precisará de {:.03f}l de tinta.'.format(tinta))