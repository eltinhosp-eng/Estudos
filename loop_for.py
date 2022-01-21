"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra, end='')


# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)


for indice in enumerate (nome):
    print(indice)


qtd = int(input('Quantas vezes esse loop deve ser impresso? '))
for n in range(1, qtd+1):
    print(f'Imprimindo {n}')


qtd = int(input('Quantas vezes esse loop deve ser impresso? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor '))
    soma = soma + num
print(f'A soma é {soma} ')
"""
valor = int(input('Digite a quantidadde de emojis que vc deseja: '))
soma = 0
# 	U+1F60F
# modificado U0001F60F

for n in range(1, valor+1):
    num = int(input(f'Informe o {n}/{valor} valor '))
    soma = soma + num
print('\U0001F60F' * soma)












