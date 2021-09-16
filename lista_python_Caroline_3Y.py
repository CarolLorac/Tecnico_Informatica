'''Crie um programa que vai ler vários números (quantidade indefinida) e colocar em uma lista. Depois
disso, exiba:
 Quantos números foram digitados
 A lista de valores, ordenados de forma decrescente
 Verificar se o valor 5 foi digitado e está ou não na lista'''

num = list()

for i in range(0,5):
    num.append(int(input('Digite um valor: ')))


print ("Quantidade de números digitados: ", len(num))


num.sort(reverse = True)
print ("Ordem descrescente: ", num)


if num.count(5) == 0:
    print ("Número 5 não foi digitado.")
    
else:
    print ("Número 5 foi digitado.")

