def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def suma_lista(numeros):
    """Devuelve la suma de todos los elementos de una lista."""
    return sum(numeros)


if __name__ == "__main__":
    print("Suma de 2 números:")
    print(f"3 + 5 = {suma(3, 5)}")
    print("Suma de una lista:")
    print(f"suma([1, 2, 3, 4, 5]) = {suma_lista([1, 2, 3, 4, 5])}")
