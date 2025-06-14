""" 1.Crie duas variáveis chamadas nome e idade. Atribua a elas seu nome e idade e use o print para exibir a seguinte frase:
"Meu nome é [nome] e eu tenho [idade] anos." """

nome= 'Gabriele'
idade= 18

print (f'Meu nome é {nome} e eu tenho {18} anos.')
print ('-'*12)
#2. Atribua os valores 5 e 10 às variáveis a e b. Troque os valores entre elas e imprima os resultados finais.

a=5
b=10

print('a=',b)
print('b=',a)
print ('-'*12)
#3. Crie uma constante chamada PI com valor 3.14159 e imprima o valor da área de um círculo de raio 4.

PI= 3.14159
raio=4
area= PI*(raio**2)
print (f'O valor da área de um círculo de raio {raio} é:{area}')
print ('-'*12)
#4. Crie três variáveis: uma do tipo inteiro, uma do tipo float e uma do tipo string. Use type() para imprimir o tipo de cada uma.

v1= 25
v2= 87.87
v3= 'Hello word'

print (type(v1))
print (type(v2))
print (type(v3))
print ('-'*12)

#5. Calcule o valor da expressão 10 + 5 * 2 - 3 ** 2 e explique o resultado com base na ordem de precedência.
valor= 10+5*2-3**2
print (f'O resultado foi {valor}, porque a ordem de precedência foi a seguinte: primeiro foi calculado o expoente (3²=9), depois a multiplicação (5x2=10) e depois a adição e subtração da esquerda para a direita (10+10=20) e (20-9=11)')

print ('-'*12)

#6. Crie uma variável chamada celsius e atribua a ela um valor em graus Celsius (por exemplo, 25). Em seguida, converta essa temperatura para Fahrenheit usando a fórmula correspondente que você pode encontrar em uma busca simples na internet. Armazene o resultado em uma variável chamada fahrenheit e exiba a seguinte mensagem com print: "A temperatura de [celsius]°C em Fahrenheit é [fahrenheit]°F"
celsius= 25
fahrenheit= (celsius*9/5)+32
print (f'A temperatura de {celsius}°C em Fahrenheit é {fahrenheit}°F')
print ('-'*12)

#7. Crie um programa que verifique se duas variáveis x e y são diferentes e maiores que zero.
x=10
y=8
print (f'{x} e {y} são diferentes? {x!=y}')
print (f'{x} é maior que 0? {x>0}')
print (f'{y} é maior que 0? {y>0}')
print ('-'*12)

#8. Avalie a expressão (5 > 3) and (2 < 1) e explique o resultado.
print (f'A expressão (5>3 and 2<1) é verdadeira? {5>3 and 2<1}')
print ('a expressão só seria verdadeira se 5 fosse maior que três e 2 fosse menor que 1 ao mesmo tempo, mas como 2 não é menor que 1, a condição completa é falsa. ')
print ('-'*12)

#9. Crie uma variável chamada altura_str e atribua a ela o valor "1.75" (uma string). Em seguida, converta essa variável para o tipo float e armazene o resultado em uma nova variável chamada altura_float. Por fim, use o print para exibir a mensagem: "A altura convertida é: [altura_float]"
altura_str= '1.75'
altura_float= float (altura_str) 
print (f'A altura convertida é {altura_float}')
print('-'*12)

#10. Crie dois conjuntos: alunos_python e alunos_java. Coloque 3 nomes em cada e:Mostre os alunos que fazem as duas linguagens.Mostre os alunos que fazem só Python,Mostre todos os alunos (sem repetição).
alunos_python= {'Alice', 'Arthur', 'Italo'} 
alunos_java= {'Julia', 'Arthur', 'Carla'}
print (f' Alunos que fazem a mesma linguagem:', alunos_python & alunos_java)
print (f' Alunos que fazem só Python:', alunos_python-alunos_java )
print (f' Todos os alunos:',alunos_java|alunos_python)
