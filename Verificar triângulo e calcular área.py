# Programa que verifica se 3 lados formam um triângulo e calcula a área
import math

a = int(input("Digite o lado a: "))
b = int(input("Digite o lado b: "))
c = int(input("Digite o lado c: "))

# Verifica se formam triângulo (regra: o maior lado < soma dos outros dois)
if a > b + c or b > a + c or c > a + b:
    print(f"Não formam triângulo. Lados digitados: {a}, {b}, {c}")
else:
    # Calcula área usando a fórmula de Herão
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Formam um triângulo! Área: {area:.2f}")
