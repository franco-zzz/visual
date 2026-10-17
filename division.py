def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

if __name__ == "__main__":
    print("División de 2 números:")
    print(f"20 / 4 = {division(20, 4)}")
