while True:
    try:
        nota1 = int(input("Nota 1: "))
        if nota1 < 0 or nota1 > 100:
            print("Insira notas entre 0 e 100")
        else:
            break
    except:
        print("Valor inserido é inválido. Tente somente número inteiros!")