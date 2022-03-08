from random import randint
def main():
    main_menu()

def main_menu():
    print('Insert 0 to Insert glyphs')
    print('Insert 1 to Insert cyphers')
    print('Insert 2 to Covert cyphers to glyphs')
    print('Insert 3 to Covert glyphs to cyphers')
    print('Insert 4 to Print')
    print('Insert 5 to Exit')
    x = int(input())
    if x == 5:
        print('Hell awaits you')
    if x > 0 and x < 3:
        seq = load(x)
    if x == 2:
        cypher, glyph = src_cyp(seq, [], [], -1)
        seq_gly = cyp_to_gly(seq, cypher, glyph)
    if x == 3:
        seq_cyp = gly_to_cyp(seq, cypher, glyph)
    if x == 4:
        pres(seq)

def pres(seq):
    print(seq)
    
def load(x):
    if x == 0:
        seq = insert_glyphs([])
        print('Glyphs entered correctly')
    elif x == 1:
        seq = insert_cyphers([])
        print('Cyphers entered correctly')
    return seq

def insert_glyphs(seq):
    phrases = ['Inserisci un intero che Dio ti guarda', 'Certo che sei proprio deficiente, inserisci un intero!', "Ti meriti solo l'inferno", 'La prossima volta che non inserisci un intero di sicuro ti accettano la 104']
    rows = int(input('Da quante righe é composto il disegno?: '))
    while type(rows) != int:
        rows = int(input(phrases[randint(0, len(phrases))]))
    for i in range(rows):
        print('Inserisci la riga', i+1, ': ')
        row = input()
        seq.append(list(row))
    return seq

def insert_cyphers(seq):
    rows = int(input('Da quante righe é composto il disegno?: '))
    for i in range(rows):
        print('Inserisci la riga', i+1, ': ')
        row = input()
        seq.append(list(row))
    return seq

def src_cyp(seq, cypher, glyph, count):
    for i in range(len(seq)):
        for j in range(len(seq[i])):
            if seq[i][j] in glyph:
                continue
            else:
                glyph.append(seq[i][j])
                count += 1
                cypher.append(count)
    return cypher, glyph

def gly_to_cyp(seq, cypher, glyph):
    for i in glyph:
        for j in range(len(seq)):
            for k in range(len(seq[j])):
                if seq[j][k] == i:
                    seq[j][k] = cypher.index(j)
    return seq

def cyp_to_gly(seq, cypher, glyph):
    for i in cypher:
        for j in range(len(seq)):
            for k in range(len(seq[j])):
                if seq[j][k] == i:
                    seq[j][k] = glyph[i]
    return seq
main()