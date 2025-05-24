def converter_temperatura(valor, origem, destino):
    origem = origem.lower()
    destino = destino.lower()

    if origem == "c":
        celsius = valor
    elif origem == "f":
        celsius = (valor - 32) * 5 / 9
    elif origem == "k":
        celsius = valor - 273.15
    else:
        return "Unidade de origem inválida."

    
    if destino == "c":
        return celsius
    elif destino == "f":
        return (celsius * 9 / 5) + 32
    elif destino == "k":
        return celsius + 273.15
    else:
        return "Unidade de destino inválida."

valor = int(input("Digite o valor da temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ")
destino = input("Digite a unidade de destino (C, F ou K): ")

resultado = int(converter_temperatura(valor, origem, destino))

print(f"A conversão de {valor}°{origem.upper()} em °{destino.upper()} é igual a: {resultado}")