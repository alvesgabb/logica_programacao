def media_lista (lista):
    return sum(lista)/len(lista)


def tabuada (n):
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')


def maiores_que (list_2,valor):
    resultado=[]
    for num in list_2:
        if num >valor:
            resultado.append(num)
    return resultado


#funções das questãoes 1 e 2 que pede na questão 
def funcao_lista(lista,n):
    nova_lista=lista[:n]
    return nova_lista

def valor_minimo (lista):
    minimo=min(lista)
    return minimo

#funções da questão 5

def adicionar_aluno(turma, nome, idade):
    turma[nome]=idade

def listar_alunos(turma):
    if not turma:
        print('Nenhum aluno cadastrado.')
    else:
        print('Alunos cadastrados.')
        for nome, idade in turma.items():
            print(f'{nome} - {idade} anos')

def remover_aluno(turma,nome):
    if nome in turma:
        del turma[nome]
        print(f'Aluno {nome} removido!')
    else:
        print(f'Aluno {nome} não encontrado.')

