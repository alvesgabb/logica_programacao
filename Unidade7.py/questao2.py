#Escreva uma função que receba uma lista de números e um valor inteiro n, e retorne uma nova lista com os n primeiros valores da lista original.

def funcao_lista(lista,n):
    nova_lista=lista[:n]
    return nova_lista


lista=[1,4,5,7,9,9]
n=5
resultado=funcao_lista(lista,n)
print(resultado)
    

