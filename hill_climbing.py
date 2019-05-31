def map(fonction, liste) :
    result = []
    for element in liste :
        result.append(fonction(element))
    return result

def prive(liste1, liste2) :
    result = []
    for element in liste1 :
        if element not in liste2 :
            result.append(element)
    return result

def copier(liste) :
    result = []
    for sous_liste in liste :
        temp = []
        for tableau in sous_liste :
            nouveau_tableau = copy(tableau)
            temp.append(nouveau_tableau)
        result.append(temp)
    return result
# int array list list -> int array list list

def voisins(horaires) :
    result = []
    for indice_ligne in range(len(horaires.departs_terminus)) :
        for indice_terminus in range(len(horaires.departs_terminus[indice_ligne])) :
            condition1, condition2 = horaires.changement_depart_terminus(indice_ligne, indice_terminus, 0)
            if condition1 :
                voisin = copier(horaires.departs_terminus)
                voisin[indice_ligne][indice_terminus][0] += 1
                result.append(Horaires(voisin))
            if condition2 :
                voisin = copier(horaires.departs_terminus)
                voisin[indice_ligne][indice_terminus][0] -= 1
                result.append(Horaires(voisin))
            for indice_depart in range(1, len(horaires.departs_terminus[indice_ligne][indice_terminus])) :
                condition1, condition2 = horaires.changement_depart_terminus(indice_ligne, indice_terminus, indice_depart)
                if condition1 :
                    voisin = copier(horaires.departs_terminus)
                    voisin[indice_ligne][indice_terminus][indice_depart] += 1
                    result.append(Horaires(voisin))
                if condition2 :
                    voisin = copier(horaires.departs_terminus)
                    voisin[indice_ligne][indice_terminus][indice_depart] -= 1
                    result.append(Horaires(voisin))
    return result
# Horaires -> Horaires

def eval(horaires) :
    somme = 0
    for indice_ligne in range(len(horaires.liste)) :
        for terminus in RESEAU.ligne_terminus(indice_ligne) :
            for heure in horaires.liste[indice_ligne][RESEAU.ligne_arrets(indice_ligne).index(terminus)] :
                for autre_terminus in prive(RESEAU.liste_terminus(), RESEAU.ligne_terminus(indice_ligne)) :
                    somme += Dijkstra_adapte(RESEAU.matrice_segments, horaires, terminus, autre_terminus, heure)[0] - heure
    return somme
# Horaires -> int

def hill_climbing(horaires) :
    horaires_actuels = horaires
    horaires_prochains = horaires
    eval_prochain = eval(horaires_actuels)
    eval_actuel = eval_prochain + 1
    while eval_prochain < eval_actuel :
        horaires_actuels = horaires_prochains
        eval_actuel = eval_prochain
        liste_voisins = voisins(horaires_actuels)
        eval_prochain = eval(liste_voisins[0])
        indice_min = 0
        for indice, voisin in enumerate(liste_voisins) :
            eval_voisin = eval(voisin)
            if eval_voisin < eval_prochain :
                eval_prochain = eval_voisin
                indice_min = indice
        horaires_prochains = liste_voisins[indice_min]
        print(eval_prochain)
    return horaires_actuels.departs_terminus
# Horaires -> int list list list
