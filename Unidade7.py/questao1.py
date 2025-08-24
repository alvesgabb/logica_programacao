#Escreva uma função que receba uma lista de números e retorne o valor mínimo encontrado.

def valor_minimo (lista):
    minimo=min(lista)
    return minimo

lista=[1,2,3,4,-5,]
resposta=valor_minimo(lista)
print(resposta)
