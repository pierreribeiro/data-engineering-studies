"""""
# Exercício 1: Crie um programa que solicite ao usuário dois números inteiros e exiba a soma deles.
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

soma = numero_1 + numero_2
print("A soma é:", soma)

# Exercício 2: Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero = int(input("Digite um número: "))
resto = numero % 5
print("O resto da divisão por 5 é:", resto)

# Exercício 3: Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

resultado = numero_1 * numero_2
print("O resultado da multiplicação é:", resultado)

# Exercício 4: Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

resultado = numero_1 // numero_2
print("O resultado da divisão é:", resultado)
""" ""
# Exercício 5: Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("Digite um número: "))
quadrado = numero**2
print("O quadrado do número é:", quadrado)

# Exercício 6: Escreva um programa que receba dois números flutuantes e realize sua adição.

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

soma = numero_1 + numero_2
print("A soma dos números é:", soma)

# Exercício 7: Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
media = (numero_1 + numero_2) / 2
print("A média dos números é:", media)

# Exercício 8: Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
potencia = base**expoente
print("O resultado da potência é:", potencia)

# Exercício 9: Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("A temperatura em Fahrenheit é:", fahrenheit)

# Exercício 10: Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math

raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio**2
print("A área do círculo é:", area)

# Exercício 11: Crie um programa que converta um valor em metros para centímetros.
