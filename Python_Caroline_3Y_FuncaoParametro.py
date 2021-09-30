'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome
de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.
Crie uma docstring explicando a sua função.'''

def ficha (nome='', gols=0):
    '''A função ficha tem como objetivo informar a filha de um jogador de futebol,
    indicando seu nome e a quantidade de gols marcada.'''
    print ("Jogador: ", nome)
    print ("Quantidade de gols marcados: ", gols)

nome = input("Digite o nome do jogador: ")
gols = int(input("Digite a quantidade de gols marcados: "))

ficha(nome, gols)
