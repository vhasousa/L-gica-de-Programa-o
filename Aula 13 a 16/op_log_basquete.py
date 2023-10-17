#Algoritmo para verificar categoria de jogadores de basquete
atleta = input("Informe o nome do atleta: ")
idade = int(input("Informe a idade do atleta: "))

if idade > 9 and idade < 13:
    print(f"O atleta {atleta} com {idade} anos fará parte da categoria Sub-11")
elif idade > 12 and idade < 15:
    print(f"O atleta {atleta} com {idade} anos fará parte da categoria Sub-13")
elif idade > 14 and idade < 17:
    print(f"O atleta {atleta} com {idade} anos fará parte da categoria Sub-15")
elif idade > 16 and idade < 19:
    print(f"O atleta {atleta} com {idade} anos fará parte da categoria Sub-18")
else:
    print(f"O atleta {atleta} com {idade} anos está fora da idade permitida")