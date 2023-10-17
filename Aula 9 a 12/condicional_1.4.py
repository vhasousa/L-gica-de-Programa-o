#Algoritmo para verificar se a pessoa é menor de idade, maior de idade ou está na terceira idade
idade = int(input("Qual é sua idade? "))

if idade < 18:
    print("Você é menor de idade")
elif idade < 60:
    print("Você é maior de idade")
else:
    print("Terceira idade")
    