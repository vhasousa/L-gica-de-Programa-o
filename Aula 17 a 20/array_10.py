minha_lista = [1, 2, -4, 6, -7, 8, 9, -11, 10]

#Contabiliza quantidade de elementos positivos
contador = 0

for x in minha_lista:
    if x > 0:
        contador = contador + 1

print(contador)