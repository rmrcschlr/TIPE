class Horaires :
    
    def __init__(self, reseau, mega_matrice) :
        self.liste = []
        for indice_ligne in range(len(reseau.liste_lignes)) :
            ligne = []
            for indice_arret in reseau.ligne_arrets(indice_ligne) :
                arret = []
                if indice_arret in reseau.ligne_terminus(indice_ligne) :
                    arret = mega_matrice[indice_ligne][reseau.ligne_terminus(indice_ligne).index(indice_arret) + 1][1:]
                ligne.append(arret)
            self.liste.append(ligne)
    # Horaires -> Reseau -> list of list of list of int -> Horaires
    
    def remplir_horaires(self) :
        for indice_ligne in range(len(self.liste)) :
            for indice_arret in range(len(self.liste[indice_ligne])) :
                if self.liste[indice_ligne][indice_arret] == [] :
                    compteur = 1
                    trajet = 0
                    while self.liste[indice_ligne][indice_arret - compteur] == [] :
                        compteur += 1
                        trajet += reseau.matrice_segments[indice_arret - compteur][indice_arret - compteur + 1]
                    self.liste[indice_ligne][indice_arret] = self.liste[indice_ligne][indice_arret - compteur] + trajet
    # Horaires -> unit
    