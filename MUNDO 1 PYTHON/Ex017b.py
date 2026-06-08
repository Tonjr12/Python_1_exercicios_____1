'''import math
co = float(input("digite o valor do cateto oposto: "))
ca = float(input("digite o valor do cateto adjacente: "))
hipotenusa = math.hypot(co,ca)
print('a hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

from math import hypot
co = float(input("digite o valor do cateto oposto: "))
ca = float(input("digite o valor do cateto adjacente: "))
hipotenusa = hypot(co,ca)
print('a hipotenuisa vai medir {:.2f}'.format(hipotenusa))
