def conversor_moeda(valor, taxa):
    return valor * taxa

valor_em_dolares = 100  # Valor em dólares
taxa_de_cambio = 5.06  # Taxa de câmbio para converter dólares para reais

resultado = conversor_moeda(valor_em_dolares, taxa_de_cambio)

print(f"{valor_em_dolares} dólares equivalem a {resultado} reais.")
