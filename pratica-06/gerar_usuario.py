import requests

def obter_usuario_aleatorio():
    url = 'https://randomuser.me/api/'

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"Nome {nome}\n E-mail {email}\n País {pais}"
    except requests.RequestException:
        return f"Erro ao obter o usuário."

print("Gerando um usuario aleatório...")
usuario = obter_usuario_aleatorio()
print(usuario)