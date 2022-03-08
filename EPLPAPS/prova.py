lista = [[['A', '1'], ['A', '2'], ['A', '3'], ['A', '4']], 
        [['B', '1'], ['B', '2'], ['B', '3'], ['B', '4']], 
        [['C', '1'], ['C', '2'], ['C', '3'], ['C', '4']], 
        [['D', '1'], ['D', '2'], ['D', '3'], ['D', '4']]]

lista = [[['A1', 'A2', 'A3', 'A4']],
        [['B1', 'B2', 'B3', 'B4']],
        [['C1', 'C2', 'C3', 'C4']],
        [['D1', 'D2', 'D3', 'D4']]]

lettera = input()
cambio = input()
parola = lettera[:len(lettera)-1]+cambio
print(parola)

print()
numero = int(input())
numero = ' '+str(numero)
print(numero)
cambio = input()
parola = str(cambio)+numero[1:]
print(parola)

n = input()
if n.isdigit():
    print('Fuck!')

lista = []

for i in range(5):
    for j in range(5):
        combinazione = chr(97+i)+str(j+1)
        lista.append(combinazione)

print(lista)
