#Crie um programa principal que importe um arquivo de módulo com as funções dos exercícios anteriores e utilize-as para realizar as seguintes operações:
#calcular a média de uma lista de números, imprimir a tabuada de um número informado pelo usuário e imprimir os valores de uma lista de números que são maiores que um valor informado pelo usuário.
import funcoes

#média de uma lista de números
lista=[1,2,5,6,7]
print(f'A média da lista de números é:', funcoes.media_lista(lista))

#imprimir a tabuada de um número
numero=int(input('Digite aqui um número para consultar a sua tabuada:'))
funcoes.tabuada(numero)

#imprimir os valores de uma lista de números que são maiores que um valor informado pelo usuário.
list_2=[10,20,30,40,50]
valor=int(input('Digite um valor:'))
print(f'Números maiores que {valor}, são', funcoes.maiores_que(list_2,valor))








