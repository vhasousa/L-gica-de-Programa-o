#Algoritmo para converter real em dólar
real = float(input("Digite o valor em reais: "))

dolar = 5.05

cambio = real / dolar



print(f"R${real} é equivalente a {round(cambio,2)} USD")
