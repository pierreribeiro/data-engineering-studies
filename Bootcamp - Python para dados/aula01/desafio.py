nome = str(input("Digite seu nome: "))
salario = float(input("Digite seu salário: "))
bonus = float(input("Digite o valor do bônus: "))

salario_total = 1000 + salario * bonus
print(f"Olá {nome}, o seu valor de bonus foi: {salario_total}")
