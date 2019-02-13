def inclus(liste1, liste2) :
    if liste1 == [] or len(liste1) > len(liste2) :
        return False
    liste2_bis = liste2.copy()  
    result = True
    i = 0
    while result and i < len(liste1) :
        result = liste1[i] in liste2_bis
        if result :
            liste2_bis.remove(liste1[i])
        i += 1
    return result

class Reseau :
    
    def __init__(self, arrets, matrice) :
        self.liste_arrets = arrets
        self.liste_lignes = []
        self.matrice_segments = matrice
    # Reseau -> list of str -> list of list of float -> Reseau
    
    def ajouter_arret(self, nom) :
        self.liste_arrets.append(nom)
        for i in range(len(self.liste_arrets)) :
            self.matrice_segments[i].append(-1)
        self.matrice_segments.append((len(self.matrice_segments) * [-1]) + [0])
    # Reseau -> str -> unit
    
    def indice_arret(self, nom) :
        indice = 0
        while indice < len(self.liste_arrets) and nom != self.liste_arrets[indice] :
            indice += 1
        if indice == len(self.liste_arrets) :
            return -1
        return indice
    # Reseau -> string -> int
    
    def nom_arret(self, indice) :
        return self.liste_arrets[indice]
    # Reseau -> int -> str
    
    def ligne_correcte(self, ligne) :
        return (max(ligne[1]) <= len(self.liste_arrets) - 1) and (inclus(ligne[2], ligne[1]))
    # Reseau -> [str, list of int, list of int] -> bool

    def ajouter_ligne(self, nom, arrets, terminus) :
        assert (arrets != [] and terminus != []), "C'est pas une ligne"
        for arret in arrets :
            assert arret in self.liste_arrets
        liste_indices_arrets = []
        for arret in arrets :
            liste_indices_arrets.append(self.indice_arret(arret))
        liste_indices_terminus = []
        for arret in terminus :
            liste_indices_terminus.append(self.indice_arret(arret))
        ligne = [nom, liste_indices_arrets, liste_indices_terminus]
        assert self.ligne_correcte(ligne), "La ligne n'est pas correcte"
        self.liste_lignes.append(ligne)
    # Reseau -> str -> list of str -> list of str -> unit
    
    def indice_ligne(self, nom) :
        indice = 0
        while indice < len(self.liste_lignes) and nom != self.liste_lignes[indice][0] :
            indice += 1
        if indice == len(self.liste_lignes) :
            return -1
        return indice
    # Reseau -> str -> int
    
    def nom_ligne(self, indice) :
        return self.liste_lignes[indice][0]
    # Reseau -> int -> str
    
    def ligne_arrets(self, indice) :
        return self.liste_lignes[indice][1]
    # Reseau -> int -> int list
    
    def ligne_terminus(self, indice) :
        return self.liste_lignes[indice][2]
    # Reseau -> int -> int list
    
    def afficher_ligne(self, indice) :
        result = self.ligne_arrets(indice)[0]
        for indice_arret in self.ligne_arrets(indice)[1:] :
             result += " -> " + self.nom_arret(indice_arret)
        return result
    # Reseau -> int -> str
    
    def changer_temps(self, indice_arret_init, indice_arret_final, temps) :
        self.matrice_segments[indice_arret_init][indice_arret_final] = temps
    # Reseau -> int -> int -> int -> unit
    
    def correspondance(self, indice_arret):
        lignes = []
        for indice_ligne in range(len(self.liste_lignes)) :
                if indice_arret in self.ligne_arrets(indice_ligne) :
                    lignes.append(indice_ligne)
        return lignes
    # Reseau -> str -> int -> list of int
    
    def troncons(self, indice_ligne) :
        liste_troncons = []
        indice_arret = self.ligne_terminus(indice_ligne)[0]
        compteur = self.ligne_arrets(indice_ligne).index(indice_arret)
        for indice_terminus in self.ligne_terminus(indice_ligne) :
            troncon = [indice_arret]
            compteur += 1
            if compteur == len(self.ligne_arrets(indice_ligne)) :
                compteur = 0
            indice_arret = self.ligne_arrets(indice_ligne)[compteur]
            while indice_arret not in self.ligne_terminus(indice_ligne) :
                troncon.append(indice_arret)
                compteur += 1
                if compteur == len(self.ligne_arrets(indice_ligne)) :
                    compteur = 0
                indice_arret = self.ligne_arrets(indice_ligne)[compteur]
            troncon.append(indice_arret)
            liste_troncons.append(troncon)
        return liste_troncons
    # Reseau -> int -> list of list of int
    
    def duree(self, indice_ligne, arret_init, arret_final) :
        troncons_valides = []
        for indice_troncon, troncon in enumerate(self.troncons(indice_ligne)) :
            if (arret_init in self.troncons(indice_ligne)[indice_troncon]) and (arret_final in self.troncons(indice_ligne)[indice_troncon]) and self.troncons(indice_ligne)[indice_troncon].index(arret_init) <= self.troncons(indice_ligne)[indice_troncon].index(arret_final):
                troncons_valides.append(troncon)
        if troncons_valides == [] :
            print("Je ne peux pas calculer la durée pour l'instant")
            return -1
        durees = []
        for troncon in troncons_valides :
            indice = troncon.index(arret_init)
            duree = 0
            while troncon[indice] != arret_final :
                duree += self.matrice_segments[troncon[indice]][troncon[indice + 1]]
                indice += 1
            if (troncon[indice] == arret_final) :
                durees.append(duree)
        try :
            return min(durees)
        except ValueError :
            print("Je ne peux pas calculer la durée pour l'instant")
            return -1
    # Reseau -> int -> str -> str -> int
