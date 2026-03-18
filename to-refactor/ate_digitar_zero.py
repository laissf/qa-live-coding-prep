# Peça números ao usuário até ele digitar 0.
# Depois mostre:
# quantos números foram digitados
# quantos são pares
# quantos são ímpares

lista_numeros = []
lista_num_pares = []
lista_num_impares = []

while True:
    try:
        numero = int(input("Digite um numero:\n"))
        if numero == 0:
            break
        lista_numeros.append(numero)

    except ValueError:
        print("Você não digitou um número. Tente novamente.")

for i in range(len(lista_numeros)):
    if lista_numeros[i] % 2 == 0:
        lista_num_pares.append(lista_numeros[i])
    else:
        lista_num_impares.append(lista_numeros[i])

print ("Total de números digitados:", len(lista_numeros))
print ("Total de números pares:", len(lista_num_pares))
print ("Total de números ímpares:", len(lista_num_impares))