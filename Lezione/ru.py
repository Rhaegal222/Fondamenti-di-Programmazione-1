n = int(input())
lista = []
uguali = False
esistono2uguali = False

for i in range(n):
    lista.append([])
    for j in range(n):
        lista[i].append(int(input()))

for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):
        uguali = True
        for k in range(len(lista)):
            if lista[i][k] != lista[j][k]:
                uguali = False
                break
        if uguali:
            esistono2uguali = True
    
for i in range(len(lista)):
    print()
    for j in range(len(lista)):
        print(lista[i][j], ' ', end = '')
print()

print('OK' if esistono2uguali else 'NO')

