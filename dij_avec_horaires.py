def voisin(M,t,interdit):
    voisin=[]
    for i in range(len(M[t])):
        if M[t][i] != -1 and not(i in interdit):
            voisin.append(i)
    return voisin
    
# list of list of float -> int -> list of int -> list of int

def colonne(mat,c):
    L=[]
    for i in range(len(mat)):
        L.append(mat[i][c])
    return L
    
# list of list of a' -> int -> list of a'

def sans_0(K):
    k=[]
    for i in K:
        if i != 0:
            k.append(i)
    return k

# list of float -> list of float

def Dijkstra_adapte(matrice, horaires, arret_init, arret_final, heure_depart) :
    liste = len(M) * [[heure_depart, []]]
    liste[arret_init][1]=[arret_init]
    arrets_interdits = []
    arret_actuel = arret_init
    while arret_actuel != arret_final :
        arrets_interdits.append(arret_actuel)
        liste_voisins = voisin(matrice, arret_actuel, arrets_interdits)
        for arret_voisin in listes_voisins :
            if liste[arret_voisin][0] == heure_depart :
                liste[arret_voisin][0] = liste[arret_actuel][0] + matrice[arret_actuel][arret_voisin]
                liste[arret_voisin][1] = liste[arret_actuel][1][:]
            else:
                if liste[arret_actuel][0] + matrice[arret_actuel][arret_voisin] < liste[arret_voisin][0]:
                    liste[arret_voisin][1] = liste[arret_actuel][1][:]
                liste[arret_voisin][0] = min(liste[d][0] + matrice[arret_actuel][arret_voisin], liste[i][0])
        arrets_interdits.append(arret_actuel)
        liste[arret_actuel][0] = 0
        x = colonne(liste,0).index(min(sans_0(colonne(liste,0))))
        liste[x][1] += [x]
        arret_actuel = x
    return l[a]
    
# list of list of float -> int -> int -> float*list of int
