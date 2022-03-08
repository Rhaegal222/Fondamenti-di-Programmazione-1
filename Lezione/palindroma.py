x = list(input())
cond = True
for i in range(len(x)//2):
    if x[i] != x[len(x)-1-i]:
        cond = False
print('è palindroma' if cond else 'non è palindroma')