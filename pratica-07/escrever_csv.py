import csv

def escrever_csv(nome_arquivo, dados):
    with open (nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
        for linha in dados:
            escritor.writerow(linha)
    print(f"Dados salvos em {nome_arquivo}")        

dados = [
    ['Ana', 28, 'Rio de Janeiro'],
    ['Bento', 36, 'São Paulo'],
    ['José', 27, 'Vitória'],
    ['Juliano', 25,'Nova York']
]

if __name__ =="__main__":
    nome_arquivo = input("Digite o nome do arquivo csv: ")
    escrever_csv(nome_arquivo, dados)