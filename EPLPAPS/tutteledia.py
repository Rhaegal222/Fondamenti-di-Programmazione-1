from random import randint

def tutte(griglia):
    if len(griglia) < 4:
        print('Dimensione Insufficiente')
        return
    else:
        dimensione = len(griglia)-3

    print('Diagonali principali:')

    if len(griglia) > 4:
        for i in range(1, dimensione):
            for j in range(len(griglia)-i):
                print(griglia[j][i+j], end=' ')
            print()

    for i in range(dimensione):
        for j in range(len(griglia)-i):
            print(griglia[i+j][j], end=' ')
        print()

    print('\nDiagonali secondarie')
    for i in range(3, len(griglia)):
        for j in range(3+(i-2)):
            print(griglia[j][i-j], end=' ')
        print()
        
    if len(griglia) > 4:
        for i in range(1, len(griglia)-3):
            for j in range(len(griglia)-i):
                print(griglia[j+i][len(griglia)-1-j], end=' ')
            print()

def main():
    n = int(input('Inserisci le dimensioni della matrice: '))
    matrice = [[randint(0,9) for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            print(matrice[i][j], end='|')
        print()
    print()
    
    tutte(matrice)
main()