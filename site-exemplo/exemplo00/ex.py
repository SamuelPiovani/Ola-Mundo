from random import randint
from time import sleep

#Fução usando uma lista para sortear 5 números aleatorios
def sorteia(lista):
    sleep(1)
    print('5 Números sorteados:', end=' ')
    for cont in range(1, 6):
        n = (randint(1, 10))
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)

#função para somar somente os números pares
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print()
    sleep(1)
    print(f'A soma dos números pares é de {soma}!')

#escrevendo na  tela os números sorteados e a soma dos números pares
numeros = list()
sorteia(numeros)
somapar(numeros)
