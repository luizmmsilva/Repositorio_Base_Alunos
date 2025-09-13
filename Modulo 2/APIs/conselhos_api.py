# Conselhos
import requests

def obter_conselho():
    """Consulta a API e retorna um conselho em português."""
    url = "https://api.adviceslip.com/advice"
    resposta = requests.get(url)  # Sem try/except
    dados = resposta.json()
    return dados["slip"]["advice"]

def mostrar_conselhos(qtd=5):
    """Exibe vários conselhos numerados."""
    print("💡 Conselhos do Dia:\n")
    for i in range(1, qtd + 1):
        conselho = obter_conselho()
        print(f"{i}. {conselho}")

if __name__ == "__main__":
    mostrar_conselhos(qtd=4)  # Altere para mais ou menos conselhos