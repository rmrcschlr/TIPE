def voisin(M,t,interdit):
    voisin=[]
    for i in range(len(M[t])):
        if M[t][i] != -1 and not(i in interdit):
            voisin.append(i)
    return voisin
# int list list-> int -> int list-> int list

def colonne(mat,c):
    L=[]
    for i in range(len(mat)):
        L.append(mat[i][c])
    return L
# a' list list-> int -> a' list

def sans_0(K):
    k=[]
    for i in K:
        if i != 0:
            k.append(i)
    return k
# int list-> int list

def Dijkstra_adapte(matrice, horaires, arret_init, arret_final, heure_depart) :
    # liste : [horaire à l'arret, chemin] pour tous les arrets
    liste = [ [0,[]] for i in range(len(matrice)) ]
    # Initialise la liste
    liste[arret_init][0] = heure_depart
    liste[arret_init][1] = [arret_init]
    # arretsInterdits : liste des arrets déjà passés
    arrets_interdits = []
    arret_actuel = arret_init
    # Parcourir jusqu'à l'arret final
    while arret_actuel != arret_final :
        arrets_interdits.append(arret_actuel)
        liste_voisins = voisin(matrice, arret_actuel, arrets_interdits)
        # 
        horaires_arret_actuel = horaires.horaire_suivant(arret_actuel, liste[arret_actuel][0])
        # Pour tous les voisins
        for arret_voisin in liste_voisins :
            indice = 0
            while horaires_arret_actuel[indice][0] != arret_voisin :
                indice += 1
            horaire_vers_voisin = horaires_arret_actuel[indice][1]
            if liste[arret_voisin][0] == 0 :
                liste[arret_voisin][0] = horaire_vers_voisin + matrice[arret_actuel][arret_voisin]
                liste[arret_voisin][1] = liste[arret_actuel][1][:]
            else:
                if horaire_vers_voisin + matrice[arret_actuel][arret_voisin] < liste[arret_voisin][0]:
                    liste[arret_voisin][1] = liste[arret_actuel][1][:]
                liste[arret_voisin][0] = min(horaire_vers_voisin + matrice[arret_actuel][arret_voisin], liste[arret_voisin][0])
        liste[arret_actuel][0] = 0
        arret_plus_proche = colonne(liste,0).index(min(sans_0(colonne(liste, 0))))
        liste[arret_plus_proche][1] += [arret_plus_proche]
        arret_actuel = arret_plus_proche
    return liste[arret_final]
# int list list -> Horaires -> int -> int -> int -> (int, int list)
