import math

def calcular_area_retangulo(largura, altura):
    return largura * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(raio):
    return math.pi * raio ** 2

def main():
    print("Calculadora de Área de Formas Geométricas")
    
    while True:
        print("Escolha a forma geométrica:")
        print("1. Retângulo")
        print("2. Triângulo")
        print("3. Círculo")
        print("4. Sair")
        
        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            largura = float(input("Digite a largura do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            print(f"A área do retângulo é: {calcular_area_retangulo(largura, altura)}")

        elif escolha == "2":
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            print(f"A área do triângulo é: {calcular_area_triangulo(base, altura)}")

        elif escolha == "3":
            raio = float(input("Digite o raio do círculo: "))
            print(f"A área do círculo é: {calcular_area_circulo(raio)}")

        elif escolha == "4":
            print("Saindo...")
            break

        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
