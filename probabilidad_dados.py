from typing import Dict


def calcular_probabilidad(num_lados: int) -> Dict[int, float]:
    """
    Display the probability of each of the numbers rolled by two dice.
    Returns:
        Dict[int, float]: Dictionary with the probability of each outcome.
    """
    num_posibilidades = num_lados**2
    list_dados = list(range(1, num_lados+1))
    list_eventos = [dado_1 + dado_2 for dado_1 in list_dados for dado_2 in list_dados]
    dict_dados = {i: list_eventos.count(i) for i in range(min(list_eventos), max(list_eventos)+1)}
    probabilidad = {key: round((value / num_posibilidades)*100, 2) for key, value in dict_dados.items()}
    return probabilidad


def main():
    "Main Function"
    NUM_LADOS = 6
    result = calcular_probabilidad(NUM_LADOS)
    print(result)


if __name__ == "__main__":
    main()
