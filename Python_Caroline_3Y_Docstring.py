'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se essa pessoa tem voto NEGADO,
OPCIONAL ou OBRIGATÓRIO nas eleições.
Crie uma docstring explicando a sua função.'''

print("Programa VOTO ELEIÇÕES\n")

def voto(ano_nasc):
         '''A função voto() retorna se a votação do usuário nas eleições é negada,
         obrigatória ou opcional'''
         
         ano = int(input("Digite o ano atual: "))

         idade = ano - ano_nasc

         if idade<16:
             print("Voto negado!!")
             
         elif idade>=16 and idade<18:
             print ("Voto opcional!!")
             
         else:
             print("Voto obrigatório!!")

             
ano_nasc = int(input("Digite seu ano de nascimento: "))
voto(ano_nasc)
         
