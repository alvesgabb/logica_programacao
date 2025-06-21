#Escreva um algoritmo que receba do usuário dois números e retorne a soma, a subtração, a multiplicação e a divisão entre eles.

n1= float (input('Digite um número: '))
n2= float (input('Digite um número: '))
print (f'A soma de {n1} + {n2} é:{n1+n2}')
print (f'A subtração de {n1} - {n2} é:{n1-n2}')
print (f'A divisão de {n1} / {n2} é:{n1/n2}')
print ('-'*12)


#Escreva um algoritmo que receba do usuário a base e a altura de um triângulo, calcule e exiba sua área.
base= float (input('Digite a base do triângulo: '))
altura= float (input('Digite a altura do triângulo:'))
print (f'A área do triângulo é igual a:{base*altura}')
print ('-'*12)


#Faça um Programa que pergunte ao usuário quanto você ganha por hora e o número de horas trabalhadas por dia, considerando que se trabalha 5 dias por semana. Calcule e mostre o total do seu salário ao mês
ganha_por_hora=float (input('Quanto você ganha por hora?'))
horas_por_dia=float (input('Quantas horas por dia você trabalha?'))
ganho_diario= (ganha_por_hora*horas_por_dia)
ganho_semanal= (ganho_diario*5)
ganho_mensal= (ganho_semanal*4)
print (f'Considerando que você trabalha 5 dias por semana, o seu salário mensal é:{ganho_mensal:.2f}')
print ('-'*12)

#Escreva um programa que peça ao usuário para digitar a sua idade e imprima na tela o número de dias que ele viveu até o momento.
idade=int (input('Digite aqui a sua idade:'))
print (f'Você lá viveu {idade*365} dias aproximadamente!')

#Escreva um programa que peça ao usuário para digitar seu nome e sobrenome SEPARADAMENTE e imprima na tela o nome completo.
nome= (input('Digite aqui seu nome:'))
sobrenome= (input('Digite aqui seu sobrenome:'))
print (f'Seu nome completo é {nome} {sobrenome}')
print('-'*12)

#Escreva um programa que peça ao usuário para digitar a temperatura em Fahrenheit e converta para Celsius e Kelvin, imprimindo o resultado na tela.
Fahrenheit= float (input('Digite a temperatura em fahrenheit:'))
celsius= (Fahrenheit-32)*5/9
print (f'A temperatura {Fahrenheit}, convertida para Celsius é:{celsius}°C')
print (f'A temperatura {Fahrenheit} convertida para Kelvein é:{celsius+273.15}K')
print ('-'*12)

#Escreva um programa que informe a quantidade de 1’s que estão em um string. Exemplo: ´ 1011001 -> 4. A string será recebida de um usuário.
string= (input('Digite aqui uma string que contenha "1":'))
print(f'A quantidade de "1" que tem na sua string é:{string.count('1')}')
print('-'*12)


#Escreva um programa que receba do usuário uma palavra e a imprima de trás para frente.
palavra= (input('Digite aqui uma palavra:'))
print (f'A sua palavra escrita de trás para frente é:{palavra[::-1]}')
print ('*'*12)

#Escreva um programa que leia uma string contendo letras de uma frase inclusive os espaços em branco e retire os espaços em branco e depois escreva a string resultante.
frase= (input('Digite aqui uma frase:'))
sem_espaços= frase.replace(' ', '')
print (sem_espaços)
print ('-'*12)

#Escreva um programa que receba duas frases SEPARADAMENTE e imprima de maneira invertida, em adição, troque as letras A por *.
f1= (input('Digite aqui a primeira frase:'))
f2= (input('Digite aqui a segunda frase:'))
f1_palavras= f1.replace('a', '*').replace ('A','*')
f2_palavras= f2.replace('a', '*').replace ('A','*')
print (f1_palavras[::-1])
print (f2_palavras[::-1])

