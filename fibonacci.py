def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    secuencia = [0, 1]
    for i in range(2, n):
        secuencia.append(secuencia[i - 1] + secuencia[i - 2])
    return secuencia

if __name__ == "__main__":
    print("Sucesión de Fibonacci:")
    print(f"Primeros 10 términos: {fibonacci(10)}")
