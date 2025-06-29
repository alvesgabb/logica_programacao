'''1) Escreva um programa que leia o nome de um dia da semana e verifique se é um dia útil ou um dia de fim de semana. 
Caso seja um dia útil, imprima "Dia útil". Caso seja um dia de fim de semana, imprima "Fim de semana.'''

dia= (input('Digite aqui um dia da semana:')).lower()
if dia== 'sábado' or dia=='domingo':
 print ('Fim de semana')

else:
 print('Dia útil')


 '''2) Escreva um programa que leia um número inteiro entre 1 e 12 e imprima o nome do mês correspondente. Utilize a estrutura condicional
 de seleção múltipla para resolver o problema. Se o número estiver fora dessa faixa, imprima "Número inválido.'''

mes= int (input('Digite aqui um mês de 1 a 12:'))
if mes== 1:
 print('JANEIRO')

elif mes== 2:
 print('FEVEREIRO')

elif mes== 3:
  print('MARÇO')

elif mes== 4:
 print('ABRIL')

elif mes== 5:
 print ('MAIO')

elif mes== 6:
 print('JUNHO')

elif mes==7:
 print('JULHO')

elif mes== 8:
 print('AGOSTO')

elif mes== 9:
 print ('SETEMBRO')

elif mes== 10:
 print ('OUTUBRO')

elif mes== 11:
 print('NOVEMBRO')

elif mes== 12:
 print('DEZEMBRO')

else:
 print('NÚMERO INVÁLIDO')


'''3) Escreva um programa que receba o salário de uma pessoa e diga quanto ela pagará apenas de Imposto de Renda.
Considere as seguintes faixas de incidência do imposto:'''
""" até R$ 2.259,20 – isento;
de R$ 2.259,21 a R$ 2.826,65 – 7,5%;
de R$ 2.826,66 a R$ 3.751,05 – 15%
de R$ 3.751,06 a 4.664,68 – 22,5%; e
acima de R$ 4.664,68 – 27,5%.
 """

salario=float (input('Digite aqui o seu sálario:'))
if salario<=2259.20:
 print ('Isento')
elif salario>=2259.21 and salario <=2826.65:
 print (f'Você deverá pagar: {salario*0.075} de imposto')
elif salario>= 2826.66 and salario <=3751.05:
 print(f'Você deverá pagar: {salario*0.15} de imposto')
elif salario>=3751.06 and salario <=4664.68:
 print (f'Você deverá pagar: {salario*0.0225} de imposto')
else:
 print(f'Você deverá pagar: {salario*0.275} de imposto')
 


'''4) Escreva um programa que peça ao usuário um número entre 1 e 100. O programa deve verificar:
Se o número é divisível por 3, exiba "Número divisível por 3".
Se o número é divisível por 5, exiba "Número divisível por 5".
Se o número é divisível por 3 e 5, exiba "Número divisível por 3 e por 5.".
Caso contrário, exiba "Número comum".'''

numero= int(input('Digite aqui um número de 1 a 100:'))

if numero%3==0 and numero%5==0:
 print ('NÚMERO DIVÍSIVEL POR 3 E 5.')

elif numero%3==0:
 print('NÚMERO DIVISÍVEL POR 3.')

elif numero%5==0:
 print(' NÚMERO DIVISÍVEL POR 5.')

else:
 print('NÚMERO COMUM')


'''5) Crie um programa que receba uma senha e verifique sua validade com base nas seguintes condições:
Deve ter pelo menos 8 caracteres.
Deve conter pelo menos uma letra maiúscula.
Deve conter pelo menos um número.
Não pode conter espaços em branco.'''

senha= (input('Digite a senha:'))
tem_maiuscula=False
tem_numero=False
tem_espaço=False

for caractere in senha:
 if caractere.isupper():
  tem_maiuscula=True
 if caractere.isdigit():
  tem_numero=True
 if caractere==' ':
  tem_espaço=True 
tem_8_caracteres=len(senha)>=8

if tem_8_caracteres and tem_maiuscula and tem_numero and not tem_espaço:
   print('Senha válida')
else:
  print('Senha inválida.Verifique os seguintes critérios:')
if not tem_8_caracteres:
  print('A senha deve ter pelo menos 8 caracteres.')
if not tem_maiuscula:
  print('A senha deve conter pelo menos uma letra maiuscula.')
if not tem_numero:
   print('A senha deve ter pelo menos um número.')
if tem_espaço:
    print('A senha não deve conter espaços.')

