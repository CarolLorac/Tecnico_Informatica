'''EXERCICIO 1
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie 2 listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente'''

continuar = 'S'
par=[]
impar=[]
lista=[]

while continuar == 'S':
    valor = int(input("\nDigite um valor: "))
    lista.append(valor)

    continuar = input("\nDeseja continuar? S/N\n")

for i in range(0,len(lista)):
    if i%2 == 0:
        par.append(lista[i])

    else:
        impar.append(lista[i])


print("\nLista completa:")
for l in range(0,len(lista)):
    print(lista[l])

print("\nNúmeros pares:")
for p in range(0,len(par)):
    print(par[p])

print("\nNúmeros impares:")
for im in range(0,len(impar)):
    print(impar[im])
