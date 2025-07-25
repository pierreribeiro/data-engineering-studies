"""
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


import math

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

raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio**2
print("A área do círculo é:", area)

# Exercício 11: Crie um programa que converta um valor em metros para centímetros.
"""

# Exercício 21: Conversor de Temperatura Escreva um programa que converta a temperatura de Celsius para Fahrenheit.
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError.
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
celsius = input("Digite a temperatura em Celsius: ")
try:
    celsius = float(celsius)
    fahrenheit = (celsius * 9 / 5) + 32
    print("A temperatura em Fahrenheit é:", fahrenheit)
except ValueError:
    print("Por favor, insira um número válido para a temperatura em Celsius.")

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
# Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada
entrada = input("Digite uma palavra ou frase: ")
try:
    if not isinstance(entrada, str):
        raise ValueError("A entrada deve ser uma string.")
    entrada = entrada.replace(" ", "").lower()
    if entrada == entrada[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
except ValueError as e:
    print(e)
