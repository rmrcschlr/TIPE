def liste_places(valeur, liste) :
    places = []
    for i in range(len(liste)) :
        if liste[i] == valeur :
            places.append(i)
    return places

class Horaires :
    
    def __init__(self, departs_terminus) :
        self.departs_terminus = departs_terminus
        self.liste = []
        for indice_ligne in range(len(RESEAU.liste_lignes)) :
            ligne = []
            for indice_arret in RESEAU.ligne_arrets(indice_ligne) :
                arret = array([])
                if indice_arret in RESEAU.ligne_terminus(indice_ligne) :
                    arret = array(departs_terminus[indice_ligne][RESEAU.ligne_terminus(indice_ligne).index(indice_arret)][:])
                ligne.append(arret)
            self.liste.append(ligne)
        self.remplir_horaires()
    # Horaires -> int list list list -> unit
    
    def remplir_horaires(self) :
        for indice_ligne in range(len(self.liste)) :
            for indice_arret in range(len(self.liste[indice_ligne])) :
                if array_equal(self.liste[indice_ligne][indice_arret], []) :
                    compteur = 0
                    trajet = 0
                    while array_equal(self.liste[indice_ligne][indice_arret - compteur], []) :
                        trajet += RESEAU.matrice_segments[RESEAU.ligne_arrets(indice_ligne)[indice_arret - compteur - 1]][RESEAU.ligne_arrets(indice_ligne)[indice_arret - compteur]]
                        compteur += 1
                    self.liste[indice_ligne][indice_arret] = self.liste[indice_ligne][indice_arret - compteur] + trajet
    # Horaires -> unit
    
    def horaires_ligne(self, indice_ligne) :
        return self.liste[indice_ligne]
    # Horaires -> int -> int array list
    
    def horaires_arret(self, indice_arret) :
        liste = []
        for indice_ligne in range(len(self.liste)) :
            for indice in liste_places(indice_arret, RESEAU.ligne_arrets(indice_ligne)) :
                indice_suivant = indice + 1
                if indice_suivant == len(RESEAU.ligne_arrets(indice_ligne)) :
                    indice_suivant = 0
                temp = (RESEAU.ligne_arrets(indice_ligne)[indice_suivant], self.liste[indice_ligne][indice]) # le premier element est la direction du bus
                liste.append(temp)
        return liste
    # Horaires -> int -> (int, int array) list
    
    def horaire_suivant(self, indice_arret, heure) :
        result = []
        liste = self.horaires_arret(indice_arret)
        for indice in range(len(liste)) :
            compteur = 0
            horaire = liste[indice][1][compteur]
            while horaire < heure and compteur < len(liste[indice][1]) - 1 :
                compteur += 1
                horaire = liste[indice][1][compteur]
            if compteur != len(liste[indice][1]) :
                result.append((liste[indice][0], horaire))
        return result
    # Horaires -> int -> int -> (int, int) list
