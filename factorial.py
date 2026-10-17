def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para negativos")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    print("Factorial:")
    print(f"5! = {factorial(5)}")
