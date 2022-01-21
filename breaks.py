for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sair do loop.')

while True:
    comando = input('Digite "Sair" para sair: ')
    if comando == "Sair":
        break
