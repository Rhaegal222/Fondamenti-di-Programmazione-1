from random import randint

def controllo_facile(griglia):
    cont = 1
    for i in range(len(griglia)):
        for j in range(len(griglia)-i):
            for k in range(i, len(griglia)):
                if j == k-i and j + 1 < len(griglia) and k + 1 < len(griglia) and griglia[j][k] == griglia[j+1][k+1]:
                    cont += 1
        if cont >= 4:
            return False
        else:
            cont = 1

    cont = 1
    for i in range(len(griglia)):
        for j in range(len(griglia)-i):
            for k in range(len(griglia)-1-i, -1, -1):
                if j + k == len(griglia)-1-i and j+1 < len(griglia) and k - 1 >= 0 and griglia[j][k] == griglia[j+1][k-1]:
                    cont += 1
                    break
        if cont >= 4:
            return False
        else:
            cont = 1

#matrice = [[randint(0, 1) for j in range(10)] for i in range(10)]

#matrice = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
matrice = [[1, 1, 0, 0, 0], [1, 0, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 0], [0, 1, 1, 0, 0]]

for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        print(str(matrice[i][j])+'|', end='')
    print()

print(controllo_facile(matrice))