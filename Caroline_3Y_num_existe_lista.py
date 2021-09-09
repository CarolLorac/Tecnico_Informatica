'''Exercicio 2
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente'''

continuar = 'S'
lista=[2,3]

while continuar == 'S':

    num = int(input("Digite um valor: "))

    if num in lista:
        print ("O número já existe na lista.")

    else:
        lista.append(num)

    continuar = input("\nDeseja continuar? S/N\n")

print("Valores digitados em ordem crescente: ", sorted(lista))

