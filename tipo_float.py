"""
Tipo Float

Tipo Real, Decimal

Casas Decimais

OBS: O separador de casas decimais na programação é ponto final e não vírgula;
"""
# Errado do ponto de vista float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer uma dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(valor2)

# Podemos converter um floa para um int(inteiro)
"""
Obs: Quando convertemos valores float pra int, perdemos precisão, 
tudo o que temos depois do ponto é perdido.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com numeros complexos
variavel = 5j
print(type(variavel))
