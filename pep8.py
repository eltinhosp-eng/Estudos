"""
PEP8 - Python Enhancement Proposal

São propostas e melhorias para a linguagem Python

import this

A ideia de PEP8 é que possamos escrever códigos Python de forma Pythonica.

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass

class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços paa identação! (Não use a tecla Tab)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco;
- Separa funções e definições da classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;


[5] - Imports devem ser sempre feitos em linhas separaas;

# Import  Errado
import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções

# Não faça:
funcao( algo[ 1 ], { outro: 2 })

# Faça:

funcao(algo[1], {outro: 2})

[7] - Termine sempre uma instrução com uma nova linha.
"""
import this






