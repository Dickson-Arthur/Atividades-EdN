ano = int(input("Digite o ano para verificar se é bissexto: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f"O Ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")
