print ("Hello, World!")
nome = "Laís"
idade = 30
tempo_trabalho = 6.5
estuda = True

nome1 = input ("Qual seu nome?\n")
print (f"Seja bem vindo(a), {nome1}")

while True:
    try:
        numero = int(input ("Digite um número:\n"))

        if numero % 2 == 0:
            print(f"{numero} é par")
        else:

            print(f"{numero} é impar")
        break
    except ValueError:
        print ("Você não digitou um número inteiro")