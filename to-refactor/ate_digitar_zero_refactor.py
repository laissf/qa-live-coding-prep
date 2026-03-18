# Peça números ao usuário até ele digitar 0.
# Depois mostre:
# quantos números foram digitados
# quantos são pares
# quantos são ímpares

total, impares, pares = 0, 0, 0
while True:
    try:
        numero = int(input("Digite um número inteiro ou zero para sair:\n"))
        if numero == 0:
            break
        if numero < 0:
            print("Número negativo não é permitido. Tente novamente.")
            continue
        total += 1

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    except ValueError:
        print("Você não digitou um número. Tente novamente.")

print("Total:", total)
print("Pares:", pares)
print("Ímpares:", impares)