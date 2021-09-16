'''Exercicio 1 – Utilizar For
1. Um cinema possui capacidade de 10 lugares e está sempre com ocupação total. Certo dia,
cada espectador respondeu a um questionário, no qual constava:
 Sua idade
 Sua opinião em relação ao filme, seguindo as seguintes notas:
Nota Significado
A Ótimo
B Bom
C Regular
D Ruim
E Péssimo
Elabore um programa que, lendo esses dados, calcule e exiba:
a) A quantidade de respostas ótimo
b) A diferença percentual entre respostas bom e regular
c) A média de idade das pessoas que responderam ruim
d) A porcentagem de respostas péssimo e a maior idade que utilizou esta opção
e) A diferença de idade entre a maior idade que respondeu ótimo e a maior idade que
respondeu ruim.'''

print ('EXERCÍCIO 1')

c=1
contA=0
contB=0
contC=0
contD=0
contE=0
acum_id=0
maiorE = 0
maiorA = 0
maiorD = 0



print (' nota      significado')
print ('  A          ótimo    ')
print ('  B          bom      ')
print ('  C          regular  ')
print ('  D          ruim     ')
print ('  E          péssimo  ')


for c in range(1,11):
    c=c+1

    idade = int(input('\nDigite sua idade: '))

    opn = input('Digite sua opinião sobre o filme: ').upper()

    if opn == 'A':
        contA=contA+1

        if idade > maiorA:
            maiorA = idade


    elif opn == 'B':
        contB=contB+1


    elif opn == 'C':
        contC=contC+1


    elif opn == 'D':
        contD=contD+1
        acum_id=acum_id+idade
        
        if idade > maiorD:
            maiorD = idade
        
    else:
        contE=contE+1

        if idade > maiorE:
            maiorE = idade
        

conta1 = contB - contC
conta2 = maiorA - maiorD

media_idD = acum_id/contD

porc = (100*conta1)/10
porc_pes = (100 * contE)/10

print ('\nA quantidade de ótimo é ', contA)
print ('A diferença percentual entre respostas bom e regular é ', porc,'%')
print ('A média de idade das pessoas que responderam ruim é ',media_idD)
print ('A porcentagem de respostas péssimo é de ', porc_pes,'% e a maior idade que utilizou esta opção é ', maiorE)
print ('A diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim é de ',conta2,' anos')

                            
print ('===' *5)


'''Exercicio 2 – Utilizar While
2. Faça um programa que calcule a média de salários de uma empresa, pedindo ao usuário o
nome dos funcionários e os salários e devolvendo a média, o salário mais alto e o salário
mais baixo. Use nome = “fim” para encerrar a leitura.'''

print ('EXERCÍCIO 2')

resp = 'S'
cont=0
acum_sal = 0
maior=0
menor = 9999

while resp == 'S':

    cont = cont+1
    
    nome = input('Digite o nome: ')
    sal = float(input('Digite o salário:'))

    acum_sal = acum_sal + sal

    if sal < menor:
        menor = sal

    else:
        maior = sal
                

    resp = input('Deseja continuar? S/N: ').upper()



media = acum_sal/cont
print('\nO salário mais alto é R$',maior, ' e o salário mais baixo é R$', menor)
print('A média dos salários é ', media)
print('\nfim')





