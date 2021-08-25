'''1. Escreva um programa que tenha uma função chamada maior(), que receba vários parâmetros com
valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
2. Escreva um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e
somapar(). A primeira função vai sortear 5 numeros e vai coloca los dentro da lista e a segunda
função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint

#EXERCICIO 1

print( '-' * 40)
print('EXERCÍCIO 1\n')

def maior(*num):
    maiorNum=0
    print(num)
    for i in num:
        if i > maiorNum:
            maiorNum = i

    print(f'O maior número é {maiorNum}')

maior(1,2,70,4)


#EXERCICIO 2

print('\n')
print( '-' * 40)
print('EXERCÍCIO 2\n')


num = list()

def sorteio():
    for i in range(0,5):
        n = randint(1,10)
        num.append(n)
    print(f'Valores sorteadors: {num}')


def somapar():
    soma =  0
    for i in num:
        if i%2 == 0:
            soma = soma + i

    print(f'A soma dos valores pares da lista {num} é {soma}')


sorteio()
somapar()
            
