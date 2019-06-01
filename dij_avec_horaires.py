from numpy import inf

def sans(liste, valeur) :
    result = []
    for element in liste :
        if element != valeur :
            result.append(element)
    return result

def voisin(matrice, arret, liste):
    voisin=[]
    for i in sans(liste, arret) :
        if matrice[arret][i] != inf :
            voisin.append(i)
    return voisin
# int list list-> int -> int list -> int list

def indice_minimum(liste, liste_indices) :
    indice_min = liste_indices[0]
    min = liste[liste_indices[0]]
    for indice in liste_indices[1:] :
        if liste[indice] < min :
            indice_min = indice
            min = liste[indice]
    return indice_min
# int list -> int list -> int 

def Dijkstra_adapte(matrice, horaires, arret_init, heure_depart) :
    heures = [inf] * len(matrice)
    heures[arret_init] = heure_depart
    predecesseurs = [i for i in range(len(matrice))]
    arrets_non_passes = sans([i for i in range(len(matrice))], arret_init)
    arret_actuel = arret_init
    while arrets_non_passes != [] :
        liste_voisins = voisin(matrice, arret_actuel, arrets_non_passes)
        horaires_arret_actuel = horaires.horaire_suivant(arret_actuel, heures[arret_actuel])
        for arret_voisin in liste_voisins :
            indice = 0
            while horaires_arret_actuel[indice][0] != arret_voisin :
                indice += 1
            horaire_vers_voisin = horaires_arret_actuel[indice][1]
            if heures[arret_voisin] > horaire_vers_voisin + matrice[arret_actuel][arret_voisin] :
                heures[arret_voisin] = horaire_vers_voisin + matrice[arret_actuel][arret_voisin]
                predecesseurs[arret_voisin] = arret_actuel
        arret_plus_proche = indice_minimum(heures, arrets_non_passes)
        arret_actuel = arret_plus_proche
        arrets_non_passes.remove(arret_plus_proche)
    return heures
# int list list -> Horaires -> int -> int -> int -> int list
