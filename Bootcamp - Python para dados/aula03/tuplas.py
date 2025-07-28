"""_summary_"""

lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")

print(sorted(lanche))  # Ordena a tupla e retorna uma lista

l_lanche = list(sorted(lanche))  # Converte a tupla em uma lista
print(l_lanche)

l_lanche[1] = "Refrigerante"  # Modifica o segundo item da lista
print(l_lanche)
lanche = tuple(l_lanche)  # Converte a lista de volta para tupla
print(lanche)

for comida in lanche:
    print(f"Eu vou comer {comida}")

# lanche[1] = "Refrigerante"  # Tuplas são imutáveis, então isso causará um erro
# print(lanche)

for i in range(len(lanche)):
    print("Usando o for com range+len")
    print(f"Eu vou comer {lanche[i]}")

for indice, comida in enumerate(lanche):
    print("Usando o for com enumerate")
    print(f"Eu vou comer {comida} na posição {indice}")
