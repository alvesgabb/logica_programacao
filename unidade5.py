""" 01.Escreva um programa que imprima a tabuada (Multiplicação) de um número inteiro informado pelo usuário. Imprima a tabuada de maneira organizada """
n=int(input('Digite aqui um número inteiro para ver sua tabuada:'))
for c in range(1,11):
    print(f'{n} x {c} = {n*c}')

print("-"*15)

# 02. Escreva um programa que calcule o fatorial de um número inteiro informado pelo usuário.
n=int (input('Digite aqui um número inteiro para saber seu fatorial:'))
fatorial=1
for c in range(1,n+1):
    fatorial*=c
print(f'O fatorial de {n} é {fatorial}')

print('-'*12)

#03. Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números primos dessa sequência.
while True:
    numeros=input('Digite um número inteiro(ou sair para encerrar):')
    if numeros.lower()=='sair':
        break
    numero=int(numeros)
    if numero>1:
        eh_primo=True
        divisor=2
        
        while divisor<numero:
            if numero%divisor==0:
              eh_primo=False
              break
            divisor+=1
        if eh_primo:
            print(numero,'é primo')

print('-'*12)

#04. Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números ímpares dessa sequência.

n=(input("Digite numeros inteiros separados por espaço:"))
n=n.split()
for c in n:
    if int (c)%2!=0:
        print(c)

print('-'*12)

#05. Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima a quantidade de números negativos.
cont_negativos=0

while True:
    entrada=(input("Digite um número inteiro (ou sair para encerrar): "))
    if entrada.lower()=="sair":
        break
    numero=int(entrada)
    if numero<0:
        cont_negativos+=1
    print("Quantidade de números negativos digitados", cont_negativos)


print('-'*12)

#06. Jogo de Adivinhação Crie um jogo onde o programa escolhe um número aleatório entre 1 e 100. O jogador deve tentar adivinhar o número. Obs. Pesquisa como importar e usar o módulo random para gerar o número aleatório em questão.
# A cada tentativa, o programa deve dizer se o número é maior ou menor que a tentativa.
# O jogo termina quando o jogador adivinhar o número correto.

import random
numero_secreto= random.randint(1,100)
print("Tente adivinhar o número que estou pensando (entre 1 e 100)")
while True:
    palpite=int(input("Digite seu palpite:"))

    if palpite< numero_secreto:
        print('Muito baixo!Tente novamente.')
    elif palpite>numero_secreto:
        print ('Muito alto.Tente novamente')
    else:
        print("Parabéns!Você acertou!!!")
        break

print('-'*12)

#07. Número de Vogais Peça ao usuário para inserir uma frase. Usando um laço for conte e exiba quantas vogais existem na frase. Lembre de verificar a documentação do módulo String em busca de métodos que facilitem a verificação da letra ser vogal.
import string
vogais="aeiouAEIOU"
frase=input("Digite uma frase:")
contador=0
for letra in frase:
    if letra in vogais:
        contador+=1
print(f"A frase tem {contador} vogais")