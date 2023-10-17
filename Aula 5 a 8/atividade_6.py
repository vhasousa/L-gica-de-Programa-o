#Algorirmo para calcular a média entre 3 notas inseridas pelo usuário
nota1 = int(input("Insira nota do primeiro bimestre: "))
nota2 = int(input("Insira nota do segundo bimestre: "))
nota3 = int(input("Insira nota do terceiro bimestre: "))

media = (nota1 + nota2 + nota3)/3

print(f"A média do aluno é {round(media,2)}")
