import copy

taquin = [
    [1,2,3],
    [8,0,4],
    [7,6,5]
]
derange = [
    [2,8,3],
    [1,6,4],
    [7,0,5]
]
void = 0
gn = 0

def copyOf(liste1,liste2):
    liste2 = [row[:] for row in liste1]
    return liste2

def aff(matrice):
    for x in range(len(matrice)):
        print('')
        print('---------------')
        for i in range(len(matrice[x])):
            print("|",matrice[x][i],"|" + '',end = '')
    print('\n---------------')

def findVoid(taquin):
    indice = []
    for x in range(len(taquin)):
        for i in range(len(taquin[x])):
            if taquin[x][i] == void:
                indice.append((taquin.index(taquin[x])))
                indice.append((taquin[x].index(taquin[x][i])))
    return indice
    
def hn(derange, taquin):
    hn = 0
    for x in range(len(derange)):
        for i in range(len(derange[x])):
            if derange[x][i] != taquin[x][i] and derange[x][i] != 0:
                hn += 1
    return hn

def fn(g,h):
    return g + h

def replace(l,g):
    possibility = 0
    liste = []
    liste = copyOf(l,liste)
    indice = findVoid(l)
    gauche = indice[1] - 1
    droit = indice[1] + 1
    haut = indice[0] - 1
    bas = indice[0] + 1

    if gauche > -1:
        wait = liste[indice[0]][gauche]
        liste[indice[0]][indice[1]] = wait
        liste[indice[0]][gauche] = void
        aff(liste)
        print('*Gn =', g)
        print('*Hn =',hn(liste, taquin))
        print('*Fn =',fn(g,hn(liste, taquin)))

        liste[indice[0]][gauche] = wait
        liste[indice[0]][indice[1]] = void

    if haut > -1:
        wait = liste[haut][indice[1]]
        liste[indice[0]][indice[1]] = wait
        liste[haut][indice[1]] = void
        aff(liste)
        print('*Gn =', g)
        print('*Hn =',hn(liste, taquin))
        print('*Fn =',fn(g,hn(liste, taquin)))

        liste[haut][indice[1]] = wait
        liste[indice[0]][indice[1]] = void

    if droit < 3:
        wait = liste[indice[0]][droit]
        liste[indice[0]][indice[1]] = wait
        liste[indice[0]][droit] = void
        aff(liste)
        print('*Gn =', g)
        print('*Hn =',hn(liste, taquin))
        print('*Fn =',fn(g,hn(liste, taquin)))

        liste[indice[0]][droit] = wait
        liste[indice[0]][indice[1]] = void
    
    if bas < 3:
        wait = liste[bas][indice[1]]
        liste[indice[0]][indice[1]] = wait
        liste[bas][indice[1]] = void
        aff(liste)
        print('*Gn =', g)
        print('*Hn =',hn(liste, taquin))
        print('*Fn =',fn(g,hn(liste, taquin)))

        liste[bas][indice[1]] = wait
        liste[indice[0]][indice[1]] = void
    print('____________________ fin Gn =',g)

#test du programme taquin
listCopy = []
listCopy = copyOf(derange,listCopy)
            
aff(derange)
print('*Gn =', gn)
print('*Hn =',hn(derange, taquin))
print('*Fn =',fn(gn,hn(derange, taquin)))
print('____________________ fin Gn =',gn)

replace(listCopy,1)
