#a função recebe uma lista como parametro?
# a lista pode ser vazia?
# os valores são sempre inteiros?
# podem haver números negativos?
# pode haver númeors não numéricos?

#vou assumir que recebo uma LISTA DE INTEIROS, QUE PODE ESTAR VAZIA E CONTER NÚMEROS NEGATIVOS

#test cases:
#[1,2,3,4] -> 10
#[] -> 0
# [3, 25, -5, 0] -> 23
#[12] -> 12

def soma_lista (lista):
    if lista is None:
        return 0
    else:
       return sum(lista)



