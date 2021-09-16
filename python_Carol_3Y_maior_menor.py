'''1.Crie um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
maior e o menor valor digitado e as suas respectivas posições na lista.'''

valores = [int(input("Digite o primeiro valor: ")),
           int(input("Digite o segundo valor: ")),
           int(input("Digite o terceiro valor: ")),
           int(input("Digite o quarto valor: ")),
           int(input("Digite o quinto valor: "))]


maior = max(valores)
menor = min(valores)


print("O maior valor é ",maior," e está na posição ", valores.index(maior), " da lista.")
print("O menor valor é ",menor," e está na posição ", valores.index(menor), " da lista.")

    
