"""1. Crie um programa que solicite ao usuário que insira 10 palavras. Armazene essas palavras em uma lista. Depois: a) Exiba a lista na ordem inversa. b) Substitua todas as palavras que começam com a letra "a" por ***. c) Exiba a lista modificada. """
lista=[]
for c in range(0,10):
    palavras=(input('Digite uma palavra:'))
    lista.append(palavras)
print(list(reversed(lista)))
nova_lista = [item.replace("a", "***") for item in lista]
print(nova_lista)

print('-'*12)


""" 2.Escreva um programa que leia os nomes e as notas de 5 alunos e armazene esses dados em um dicionário, onde a chave seja o nome do aluno e o valor seja a nota. Depois: a) Exiba de maneira organizada o nome e a nota de cada aluno. b) Calcule e exiba de maneira organizada a média da turma. c) Identifique e exiba o nome do aluno de maior nota. """
alunos={}
for i in range(5):
    nome=(input(f'Digite a nota do {i+1} aluno: '))
    nota=float(input(f'Digite a nota de {nome}:'))
    alunos [nome]= nota
print ('\n--- Notas dos alunos---')
for nome, nota in alunos.items():
    print(f'{nome}:{nota:.2f}')

media=sum (alunos.values()) / len(alunos)
print(f'\nMédia da turma: {media:.2f}')

maioraluno=max(alunos, key=alunos.get)
print(f'\nAluno com maior nota: {maioraluno}')
(f'{alunos[maioraluno]:.2f}')
print('\nDicionario completo:', alunos)


print('-'*12)


# 3.Diferencie tuplas de listas e dicionários.
""" As listas são representadas por colchetes '[]', são mútaveis e servem para guardar uma sêquencia de valores em ordem. 
As tuplas são representadas por '()', são imútaveis e támbem servem para guardar valores em ordem, mas só para consulta.
Os dicionários são representados por '{}', guarda o valor no formato chave: valor (tipo um mini banco de dados) e as chaves não podem se repertir. """

print('-'*12)

""" 4.Elabore um programa que: 
Dada a seguinte tupla de frutas:
frutas = ("banana", "maçã", "uva", "laranja", "maçã", "melancia", "uva")
Pergunte ao usuário o nome de uma fruta. Informe quantas vezes essa fruta aparece na tupla.
Se a fruta estiver presente, mostre o índice da primeira ocorrência. Caso contrário, exiba uma mensagem informando que a fruta não foi encontrada.
 """

frutas=('banana', 'maçã', 'uva', 'laranja', 'maçã', 'melancia', 'uva')
fruta=(input('Qual fruta você gostaria de obter informações? '))
quantidade=frutas.count(fruta)
if quantidade>0:
   print(f"A fruta {fruta} aparece {quantidade} na tupla")
   indice= frutas.index(fruta)
   print(f'A primeira ocorrência está no índice {indice}')
else:
    print(f'A fruta {fruta} não foi encontrada na tupla')
    