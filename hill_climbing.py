#Solution = #Solution liste de liste

def copier(liste) :
    result = []
    for sous_liste in liste :
        temp = sous_liste.copy()
        result.append(temp)
    return result

def voisin(Solution) :
    result = []
    for indice_ligne in range(len(Solution)) :
        for indice_terminus in range(len(Solution[indice_ligne])) :
            for indice_depart in range(len(Solution[indice_ligne][indice_terminus])) :
                voisin1 = copier(Solution)
                voisin2 = copier(Solution)
                voisin1[indice_ligne][indice_terminus][indice_depart] += 1
                voisin2[indice_ligne][indice_terminus][indice_depart] -= 1
                result.append(voisin1)
                result.append(voisin2)
    return result