"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre aspas;
"""
nome = input('Qual seu nome: ')
print(f'Seja bem-vindo(a) {nome}.')

idade = input('Qual sua idade? ')
print(f'A(o) {nome} tem {idade} anos e nasceu em {2021 - int(idade)}.')
