import math

def calcular_delta(a, b, c):
    return (b ** 2) - (4 * a * c)

def calcular_raizes(a, b, c):
    delta = calcular_delta(a, b, c)

    if delta < 0:
        print("A equação não possui raízes reais.")
        return None
    elif delta == 0:
        x = -b / (2 * a)
        print(f"A equação possui uma raiz real: x = {x}")
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"A equação possui duas raízes reais: x1 = {x1}, x2 = {x2}")
        return x1, x2

def main():
    print("Calculadora da Fórmula de Bhaskara")
    
    a = float(input("Digite o valor de 'a': "))
    b = float(input("Digite o valor de 'b': "))
    c = float(input("Digite o valor de 'c': "))

    # Verifica se é uma equação de segundo grau
    if a == 0:
        print("Isso não é uma equação de segundo grau.")
    else:
        calcular_raizes(a, b, c)

if __name__ == "__main__":
    main()
