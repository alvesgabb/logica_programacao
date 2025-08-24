""" Implemente um programa (CRUD) para gerenciar o controle de alunos de uma turma. O programa deve ser modularizado e conter as seguintes funções:
adicionar_aluno(turma, nome, idade)
Adiciona um novo aluno ao dicionário chamado turma, onde:
A chave é o nome do aluno.
O valor é a idade.
listar_alunos(turma)
Exibe todos os alunos cadastrados, mostrando o nome e a idade.
remover_aluno(turma, nome)
Remove um aluno do dicionário, dado o nome.
No programa principal:
Inicialize um dicionário vazio chamado turma.
Apresente um menu para o usuário escolher:
1: Adicionar um aluno.
2: Listar todos os alunos.
3: Remover um aluno.
4: Sair. """
import funcoes

turma={}

while True:
 print('Digite "1" para adicionar um aluno(a)')  
 print('Digite "2" para listar todos os alunos')
 print('Digite "3" para remover um aluno(a)')
 print('Digite "0" para sair')

 escolha=(input('Escolha uma opção: '))

 if escolha=='1':
  nome=(input('Nome:'))
  idade=(input('Idade:'))
  funcoes.adicionar_aluno(turma,nome,idade)
  print(f'Aluno(a) {nome} adicionado com sucesso!')

 elif escolha=='2':
  funcoes.listar_alunos(turma)

 elif escolha=='3':
  nome=(input('Digite o nome do aluno(a) que deseja remover:'))
  funcoes.remover_aluno(turma,nome)

 elif escolha =='0':
  print('Saindo do programa....')
  break

 else:
  print('Opção inválida.Tente novamente!')
  

