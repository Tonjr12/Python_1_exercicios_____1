'''import math
agulo = float(input('digite o angulo que você deseja: '))
seno = math.sin(math.radians(agulo))
print('o seno de {:.2f}'.format(seno))
cosseno = math.cos(math.radians(agulo))
print('o cosseno de {:.2f}'.format(cosseno))
tangente = math.tan(math.radians(agulo))
print('a tangente de {:.2f}'.format(tangente))'''


from math import radians, sin, cos, tan
agulo = float(input('digite o angulo que você deseja: '))
seno = sin(radians(agulo))
print('o seno de {:.2f}'.format(seno))
cosseno = cos(radians(agulo))
print('o cosseno de {:.2f}'.format(cosseno))
tangente = tan(radians(agulo))
print('a tangente de {:.2f}'.format(tangente))
