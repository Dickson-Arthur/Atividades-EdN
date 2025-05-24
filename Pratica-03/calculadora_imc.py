peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso normal.")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obeso")