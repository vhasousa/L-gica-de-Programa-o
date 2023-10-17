minha_lista = [1, 2, 4, 6, 7, 8, 9, 11, 10]

#Localizar maior elemento na lista
maior_elemento = 0

for lista in minha_lista:
    if lista > maior_elemento:
        maior_elemento = lista

print(maior_elemento)