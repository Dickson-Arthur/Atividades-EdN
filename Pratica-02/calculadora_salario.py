numero_funcionario = int(input("Insira o número do funcinário: "))
horas_trabalhadas = int(input("Insira a quantidade de horas trabalhadas do funcinário: "))
valor_por_hora = float(input("Insira o valor por hora trabalhada: "))

salario = horas_trabalhadas * valor_por_hora

print("Número do funcionário: ",numero_funcionario)
print(f"Salário = R$ {salario:.2f}")