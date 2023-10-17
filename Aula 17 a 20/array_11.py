minha_lista = [1, 2, -4, 6, -7, 8, 9, -11, 10]

#Cria uma nova lista a partir do array chamado minha_lista somente com elementos pares

pares = []
for x in minha_lista:
    if x % 2 == 0:
        pares.append(x)

print(pares)

