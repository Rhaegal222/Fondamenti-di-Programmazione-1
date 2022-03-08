def stampa_matrice(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            print(matrice[i][j], ' ', end='')
        print()
stampa_matrice()