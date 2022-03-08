#ho ordinato le funzioni del basso verso l'altro in base all'ordine con il quale vengono chiamate
def generaMatrice(matrice):
    elemento=""
    cont  = 0
    for i in range(5):
        matrice.append([])
        for j in range(5):
            lettera=input("Inserire la lettera: ")
            while lettera!=" " and not(lettera.isalpha()):
                lettera=input("Inserire la lettera: ")

            if lettera == ' ':
                cont += 1
            
            numero=input("Inserire il numero: ")
            while numero!=" " and not(numero.isdigit()):
                numero=input("inserire il numero: ")
            
            if numero == ' ':
                cont += 1

            elemento=lettera+numero
            matrice[i].append(elemento)
    return matrice, cont

def stampa(matrice):
    for i in range(len(matrice)):
        print('|', end='')
        for j in range(len(matrice[i])):
            print(matrice[i][j],end="|")
        print()

def scan(matrice):
    lettere = ['A', 'B', 'C', 'D', 'E']
    numeri = ['1', '2', '3', '4', '5']
    combinazioni = []
    
    for i in lettere:
        for j in numeri:
            combo = i+j
            combinazioni.append(combo)

    # controlla che non ci siano elementi ripetuti nelle righe
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] in combinazioni:
                combinazioni.remove(matrice[i][j])
            else:
                return False

    for i in matrice:
        for j in range(len(i)-1):
            for k in range(j+1, len(i)):
                if i[j][0] == i[k][0]:
                    return False
    
    for i in matrice:
        for j in range(len(i)-1):
            for k in range(j+1, len(i)):
                if i[j][1] == i[k][1]:
                    return False

    # controlla che non ci siano elementi ripetuti nelle colonne
    for i in range(len(matrice)):
        for j in range(len(matrice)-1):
            for k in range(j+1, len(matrice)):
                if matrice[j][i][0] == matrice[k][i][0]:
                    return False
    
    for i in range(len(matrice)):
        for j in range(len(matrice)-1):
            for k in range(j+1, len(matrice)):
                if matrice[j][i][1] == matrice[k][i][1]:
                    return False
    return True

def caricaMatrice(matrice, cont):
    stampa(matrice)
    #controllo che gli elementi vengano inseriti correttamente
    posRiga=int(input("Inserisci una posizione della riga: "))
    while posRiga<0 or posRiga>5:
        posRiga=int(input("Errore, insersci una posizione della riga corretta"))

    posColonna=int(input("Inserisci una posizione della colonna: "))
    while posColonna<0 or posColonna>5:
        posColonna=int(input("Errore, inserisci una posizione della colonna corretta: "))
    
    #Controllo se nella cella è già presente la lettera così ne evito l'inserimento
    if matrice[posRiga][posColonna][0] == ' ':
        lettera=input("Inserire la lettera: ")
        while not(lettera.isalpha()):
            lettera=input("Inserimento non consentito! Inserire la lettera: ")
        matrice[posRiga][posColonna] = lettera+matrice[posRiga][posColonna][1:]
        cont -= 1

    if matrice[posRiga][posColonna][1] == ' ':
        numero=input("Inserire il numero: ")
        while not(numero.isdigit()):
            numero=input("Inserimento non consentito! Inserire il numero: ")
        matrice[posRiga][posColonna] = matrice[posRiga][posColonna][0:1]+numero
        cont -= 1

    if cont <= 0:
        return matrice
    else:
        return caricaMatrice(matrice, cont)

def main():
    #passo la matrice come parametro senza dichiararla prima
    matrice=[['  ', ' 5', 'C ', ' 4', '  '], ['A3', 'B1', '  ', '  ', 'D4'], ['E5', '  ', '  ', 'D ', 'A '], ['  ', '  ', '  ', ' 1', 'B '], ['D1', '  ', '  ', '  ', 'C ']]
    cont = 32
    #matrice, cont=generaMatrice([])
    #unisco le funzioni calcolo combinazioni e combinazioni valide
    #sposto la richiesta di posRiga e posColonna dentro la funzione caricaMatrice
    matrice = caricaMatrice(matrice, cont)
    if scan(matrice):
        stampa(matrice)
        print('Hai Vinto!', end='')
    else:
        stampa(matrice)
        print('Hai Perso!', end='')
    
main()
