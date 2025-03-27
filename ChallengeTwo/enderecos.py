def possiveis_enderecos(ambiguousIP: str) -> list[str]:
    def is_valid(segment: str) -> bool:
        if not segment:
            return False
        if len(segment) > 1 and segment[0] == '0':
            return False
        return 0 <= int(segment) <= 255

    n = len(ambiguousIP)
    result = []

    if n < 4 or n > 12:
        return []

    for i in range(1, min(4, n - 2)):
        for j in range(i + 1, min(i + 4, n - 1)):
            for k in range(j + 1, min(j + 4, n)):
                p1, p2, p3, p4 = ambiguousIP[:i], ambiguousIP[i:j], ambiguousIP[j:k], ambiguousIP[k:]
                if all(map(is_valid, [p1, p2, p3, p4])):
                    result.append(f"{p1}.{p2}.{p3}.{p4}")

    return sorted(result)


# Testes rápidos
if __name__ == "__main__":
    exemplos = [
        "1903476",
        "255255255255",
        "000",
        "256255255",
        "23458951232345895123234589512323458951232345895123",
        ""
    ]

    for exemplo in exemplos:
        print(f"Entrada: {exemplo}")
        print("Saída:", possiveis_enderecos(exemplo))
        print("-" * 40)
