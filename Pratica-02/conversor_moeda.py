valor_em_reais = 100
taxa_dolar = 5.70
taxa_euro = 6.40

valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro

print(f"O valor de R$ {valor_em_reais} convertido em dólar é: $ {valor_em_dolar:.2f}")
print(f"O valor de R$ {valor_em_reais} convertido em euro é: EUR {valor_em_euro:.2f}")
