"""
RANGES
-> precisamos conhecer o loop for para poder usar os range.
-> precisamos conhecer o range para trabalhar melhor com loop for.

Ranges são utilizados para gerar seuqncias numéricas, não de forma aleatória,
maas sim de maneira especifica.

Formas gerais:

# Exemplo forma 1
range(valor_de_parada)
OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1).

# Exemplo forma 2
range(valor_de_inicio / valor_de_parada)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário e passo de 1 em 1).

# Exemplo forma 3
range(valor_de_inicio / valor_de_parada / passo)

"""
# Exemplo forma 1
# for num in range(11):
#    print(num)

# Exemplo forma 2
num = int(input('Digite um valor: '))
for num in range(num + 1):
    print(num)


# Exemplo forma #
for num in range(1, 11, 2):
    print(num)




















