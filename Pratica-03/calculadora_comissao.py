nome = input("Informe o nome do vendendor: ")
salario = float(input("Informe o salário fixo do vendedor: "))
vendas = float(input("Informe o valor total em dinheiro das vendas efetuadas no mês: "))

comissao = vendas * 0.15
salario_total = salario + comissao

print(f"O salário total que o {nome} irá receber é: R$ {salario_total}")