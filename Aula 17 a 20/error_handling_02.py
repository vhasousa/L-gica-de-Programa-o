while True:
    try:
        idade = int(input("Qual a sua idade: "))
        if idade < 0:
            print("Insira um número inteiro positivo")
        else:
            break
    except:
        print("Valor inserido é inválido. Tente somente número inteiros!")
