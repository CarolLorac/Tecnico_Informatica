'''1. Crie uma tupla preenchida com com os 20 primeiros colocados da tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os últimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabética
d) Em que posição na tabela esta o time da Chapecoense
Tabela:
1 Corinthians    11 Goias
2 Santos         12 Botafogo
3 São Paulo      13 Internacional
4 Coritiba       14 Fortaleza
5 Palmeiras      15 Atletico - MG
6 Gremio         16 Bragantino
7 Flamengo       17 Ceara
8 Bahia          18 Sport Recife
9 Fluminense     19 Vasco da Gama
10 Chapecoense   20 Athletico PR'''


print("EXERCICIO 1")

time = ("Corinhians","Santos","São Paulo","Coritiba","Palmeiras"
        ,"Gremio","Flamengo","Bahia","Fluminense","Chapecoense"
        ,"Goias","Botafogo","Internacional","Fortaleza"
        ,"Atletico - MG","Bragantino","Ceara","Sport Recife"
        ,"Vasco da Gama","Athletico PR")


print("\n1) Os 5 primeiros colocados são: ", time[:5])

print("\n2) Os últimos 4 colocados da tabela são: ", time[(len(time)-4):])

print("\n3) Times em ordem alfabética: ", sorted(time))

print("\n4) A chapecoense está na posição ", time.index("Chapecoense")+1," da tabela.")



'''2. Crie um programa que tenha uma tupla única para um cardápio de restaurante com nomes de
produtos e seus respectivos preços na sequencia. (inserir 6 produtos)
No final mostre uma listagem de preços organizando os dados de forma tabular. '''


print("\n\n\nEXERCICIO 2\n")


produtos = ("Lanche", 20, "Pizza", 54.90, "Batata frita", 25, "Cachorro quente",
            9.90, "Strogonoff", 30, "Comida japonesa", 59.90)


print(f'{"CARDÁPIO":^40}')


for pos in range (0, len(produtos)):

    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')

    else:
        print(f'R${produtos[pos]: 7.2f}')

