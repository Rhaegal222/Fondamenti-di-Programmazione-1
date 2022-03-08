from random import randint

def cancella(lista):
    nuova = []
    for i in range(len(lista)):
        if lista[i] != '.':
            nuova.append(lista[i])
    return nuova

def scan(lista):
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            lista[i] = '.'
    return lista

def main():
    lista =[randint(0, 10) for i in range(10)]
    lista = scan(lista)
    lista = cancella(lista)
    print(lista)

main()