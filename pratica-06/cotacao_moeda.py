import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave not in dados:
            print("Moeda não encontrada. Verifique o código e tente novamente.")
            return

        cotacao = dados[chave]

        print(f"\nCotação de {moeda} em relação ao Real (BRL):")
        print(f"Valor Atual: R$ {cotacao['bid']}")
        print(f"Valor Máximo: R$ {cotacao['high']}")
        print(f"Valor Mínimo: R$ {cotacao['low']}")
        print(f"Última atualização: {cotacao['create_date']}")

    except requests.RequestException as e:
        print("Erro ao conectar à API:", e)

def main():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip()
    if moeda:
        consultar_cotacao(moeda)
    else:
        print("Código da moeda não pode ser vazio.")

if __name__ == "__main__":
    main()
