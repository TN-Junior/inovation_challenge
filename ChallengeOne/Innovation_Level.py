def calcular_nivel_de_inovacao(historico: list[int], impulsionadores: set[int], barreiras: set[int]) -> int:
    nivel_inovacao = 0
    for evento in historico:
        if evento in impulsionadores:
            nivel_inovacao += 1
        elif evento in barreiras:
            nivel_inovacao -= 1
    return nivel_inovacao


# Teste com novo exemplo
if __name__ == "__main__":
    entrada = {
        "historico": [100, 200, 300, 100, 400],
        "impulsionadores": {100, 500},
        "barreiras": {200, 600}
    }
    print(calcular_nivel_de_inovacao(**entrada))  # Saída esperada: 1
