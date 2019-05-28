def indexs(valeur, liste) :
    places = []
    for i in range(len(liste)) :
        if liste[i] == valeur :
            places.append(i)
    return places

class Horaires :
    
    def __init__(self, reseau, mega_matrice) :
        self.reseau = reseau
        self.liste = []
        for indice_ligne in range(len(reseau.liste_lignes)) :
            ligne = []
            for indice_arret in reseau.ligne_arrets(indice_ligne) :
                arret = array([])
                if indice_arret in reseau.ligne_terminus(indice_ligne) :
                    arret = array(mega_matrice[indice_ligne][reseau.ligne_terminus(indice_ligne).index(indice_arret)][:])
                ligne.append(arret)
            self.liste.append(ligne)
        #self.remplir_horaires(reseau)
    # Horaires -> Reseau -> list of list of list of int -> Horaires
    
    def remplir_horaires(self, reseau) :
        for indice_ligne in range(len(self.liste)) :
            for indice_arret in range(len(self.liste[indice_ligne])) :
                if array_equal(self.liste[indice_ligne][indice_arret], []) :
                    compteur = 0
                    trajet = 0
                    while array_equal(self.liste[indice_ligne][indice_arret - compteur], []) :
                        trajet += self.reseau.matrice_segments[self.reseau.ligne_arrets(indice_ligne)[indice_arret - compteur - 1]][self.reseau.ligne_arrets(indice_ligne)[indice_arret - compteur]]
                        compteur += 1
                    self.liste[indice_ligne][indice_arret] = self.liste[indice_ligne][indice_arret - compteur] + trajet
    # Horaires -> unit
    
    def horaires_ligne(self, indice_ligne) :
        return self.liste[indice_ligne]
    # Horaires -> int -> list of array of int
    
    def horaires_arret(self, indice_arret) :
        liste = []
        for indice_ligne in range(len(self.liste)) :
            for indice in indexs(indice_arret, self.reseau.ligne_arrets(indice_ligne)) :
                indice_suivant = indice + 1
                if indice_suivant == len(self.reseau.ligne_arrets(indice_ligne)) :
                    indice_suivant = 0
                temp = (self.reseau.ligne_arrets(indice_ligne)[indice_suivant], self.liste[indice_ligne][indice]) # le premier element est la direction du bus
                liste.append(temp)
        return liste
    # Horaires -> int -> list of (int, array of int)
    
    def horaires_arret_vers_arret(self, indice_arret_init, indice_arret_final) :
        liste = self.horaires_arret(indice_arret_init)
        compteur = 0
        while liste[compteur][0] != indice_arret_final and compteur < len(liste) :
            compteur += 1
        if compteur != len(liste) :
            result = liste[compteur][1]
        else :
            result = []
        return result
    
    def horaire_suivant(self, indice_arret, heure) :
        result = []
        liste = self.horaires_arret(indice_arret)
        for indice in range(len(liste)) :
            compteur = 0
            horaire = liste[indice][1][compteur]
            while horaire < heure and compteur < len(liste[indice][1]) :
                compteur += 1
                horaire = liste[indice][1][compteur]
            if compteur != len(liste[indice][1]) :
                result.append((liste[indice][0], horaire))
        return result
    # Horaires -> int -> int -> list of (int, int)
    
    def horaire_suivant_vers_arret(self, indice_arret_init, indice_arret_final, heure) :
        liste = self.horaires_arret_vers_arret(indice_arret_init, indice_arret_final)
        compteur = 0
        horaire = liste[compteur]
        while horaire < heure and compteur < len(liste) :
            compteur += 1
            horaire = liste[compteur]
        if compteur != len(liste) :
            result = horaire
        else :
            result = -1
        return result
    
