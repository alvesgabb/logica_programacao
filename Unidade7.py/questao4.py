#Crie uma função chamada analisa_lista que recebe uma lista de números como parâmetro e retorna um dicionário contendo a soma de todos os números, a média dos números e o maior e o menor número da lista.

def analisa_lista(lista):
    return{
        "soma":sum(lista),
        "media":sum(lista)/len(lista),
        "maior":max(lista),
        "menor":min(lista)
    }
numeros=[10,4,9,3,5]
print(analisa_lista(numeros))




