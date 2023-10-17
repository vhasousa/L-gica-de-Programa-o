idade = int(input("Informe a idade do cliente: "))

if idade < 12 :
    print(f"R$10,00")
elif idade >=12 and idade <= 65:
    print(f"R$20,00")
else:
    print(f"R$15,00")
