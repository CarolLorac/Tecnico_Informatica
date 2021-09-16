'''Exercício: Contando vogais em tupla:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos), depois disso, você deve
mostrar, para cada palavra, quais são suas vogais.'''

print("VOGAIS DE CADA NOME", end='')

nomes = ("Ana","Bia","Carol","Giovanna","Eloise","Kathleen","Gabi","Paula","Cecilia","Lari")

for n in nomes:
    print("\n")
    print("*" * 25)
    print(n.upper())
    print("vogais:")

    if n.count('a') >= 1:
        print('a ', end='')

    if n.count('e') >= 1:
        print('e ', end='')

    if n.count('i') >= 1:
        print('i ', end='')

    if n.count('o') >= 1:
        print('o ', end='')

    if n.count('u') >= 1:
        print('u', end='')





