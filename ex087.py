#Aprimore o desafio anterior, mostrando no final:
#A)A soma de todos os valores pares digitados; B)A soma dos valores da terceira coluna;
#C)O maior valor da segunda linha.


sumpar = 0
sumcol = 0
maior2lin = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('-=' * 30)
for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            sumpar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {sumpar}')
for l in range(0, 3):
    sumcol += matriz[l][2]
print(f'A soma dos valores da terceira coluna {sumcol}')
for c in range(0, 3):
    if c == 0:
        maior2lin = matriz[1][c]
    elif matriz[1][c] > maior2lin:
        maior2lin = matriz[1][c]
print(f'O maior valor da segunda linha é {maior2lin}')