
tupla = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    entrada = int(input("Digite um número entre 0 e 20: "))
    if 0 <= entrada <= 20:
        print(f"Você digitou o número {tupla[entrada]}")
        break
    else:
        print("Tente novamente. ", end="")
        
