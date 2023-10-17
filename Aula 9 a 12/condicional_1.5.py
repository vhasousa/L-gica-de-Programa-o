#Algoritmo para verificar se o voto é obrigatório ou opcional
idade = int(input("Qual é sua idade? "))

if idade < 18 or idade > 69:
    print("Voto é opcional")
else:
    print("Voto é obrigatório")
    