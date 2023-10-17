nome = input("Informe o nome do aluno: ")

while True:
    try:
        nota1 = float(input("Informe a nota do primeiro bimestre: "))
        break
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        nota2 = float(input("Informe a nota do segundo bimestre: "))
        break
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        nota3 = float(input("Informe a nota do terceiro bimestre: "))
        break
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        nota4 = float(input("Informe a nota do quarto bimestre: "))
        break
    except:
        print("Valor inserido está incorreto")

media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 60 :
    print(f"O aluno {nome} ficou com média de {media} e foi aprovado")
else:
    print(f"O aluno {nome} ficou com média de {media} e foi reprovado")
