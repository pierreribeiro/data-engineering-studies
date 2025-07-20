"""
# exemplo_00.py
print("Hello, World!")
print("This is an example Python script for data engineering studies.")
print("Olá" + " " + "Turma!")
input("Digite seu nome: ")
print(
    "Olá, "
    + input("Digite seu nome: ")
    + "! Bem-vindo ao Bootcamp de Python para Dados."
)

print(len(input("Digite seu nome: ")))

val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))
print("A soma dos valores é:", val1 + val2)
print("A soma dos valores é:", val1 + val2, "e a média é:", (val1 + val2) / 2)

print(type(val1))
"""

print(len(input("Digite o seu nome: ")))

nome = input("Digite o seu nome: ")
nome_size = len(nome)
print(f"Olá, {nome}! Seu nome tem {nome_size} caracteres.")
