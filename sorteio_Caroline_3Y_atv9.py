#Uma loja deseja fazer um sorteio para seus clientes.Faça um programa que leia o nome de 10 clientes
#armazene em uma lista e faça o sorteio do ganhador.

print ("Programa que realiza um sorteio para os clientes de uma loja\n")

import random
clientes = list()

for i in range(1,11):
    cli = input("Digite o nome do(a)cliente: ")
    clientes.append(cli)

print("\n CLIENTE SORTEADO(A): ",random.choice(clientes))
    
