nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print("Produto: ", nome_produto)
print(f"Preço Original: R$ {preco_original:.2f}")
print("Desconto: ", porcentagem_desconto,"%")
print(f"Valor de desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")