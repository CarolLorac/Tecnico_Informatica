#CAROLINE DE SOUZA 3Y
#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente desse angulo. (usar a biblioteca math)

import math

ang = int(input("Digite um ângulo: "))
num = math.radians(ang)

print("O valor do seno de {} é {:.2f}".format(ang,math.sin(num)))
print("O valor do cosseno de {} é {:.2f}".format(ang,math.cos(num)))
print("O valor da tangente de {} é {:.2f}".format(ang,math.tan(num)))
