def supprime_doublons(liste) :
    liste_sans_doublons = [liste[0]]
    for loop1 in range(len(liste)) :
        condition = True
        for loop2 in liste_sans_doublons :
            if liste[loop1] == loop2 :
                condition = False
        if condition :
            liste_sans_doublons.append(liste[loop1])
    return liste_sans_doublons

class Cadencements :
    
    def __init__(self, reseau) :
        self.liste = []
        for i in range(len(reseau.liste_lignes)) :
            self.liste.append([reseau.liste_lignes[i][0]])
    # Cadencements -> Reseau -> unit
    
    def ajouter_ligne(self, nom) :
        self.liste.append([nom])
    # Cadencements -> string -> unit
    
    def ajouter_frequence(self, indice_ligne, debut, fin, freq) :
        self.liste[indice_ligne].append([debut, fin, freq])
    # Cadencements -> int -> int -> int -> int -> unit
    
    def indice_ligne(self, nom) :
        indice = 0
        while indice < len(self.liste) and nom != self.liste[indice][0] :
            indice += 1
        if indice == len(self.liste) :
            return -1
        return indice
    # Cadencements -> string -> int
    
    def nom_ligne(self, indice) :
        return self.liste[indice][0]
    # Cadencements -> int -> string
    
    def freq_ligne(self, indice_ligne) :
        return self.liste[indice_ligne][1:]
    # Cadencements -> int -> list of [int, int, int]
    
    def trier_ligne(self, indice_ligne) :
        self.liste[indice_ligne][1:].sort()
        i = 2
        while i < len(self.liste[indice_ligne]) :
            if self.liste[indice_ligne][i - 1] == self.liste[indice_ligne][i] :
                self.liste[indice_ligne].pop(i)
                i -= 1
            i += 1
    # Cadencements -> int -> unit
    
    def trier(self) :
        for i in range(len(self.liste)) :
            self.trier_ligne(i)
    # Cadencements -> unit
    
    def normaliser(self) :
        self.trier()
        for i in range(len(self.liste)) :
            for j in range(len(self.freq_ligne(i)) - 1) :
                if self.freq_ligne(i)[j][1] >= self.freq_ligne(i)[j + 1][0] :
                    moyenne = (self.freq_ligne(i)[j][1] + self.freq_ligne(i)[j + 1][0]) // 2
                    self.liste[i][j + 1][1], self.liste[i][j + 2][0] = moyenne, moyenne + 1
    # Cadencements -> unit
    
    def prochain_depart(self, indice_ligne, depart_precedent) :
        self.normaliser()
        tranche = 0
        while tranche < len(self.freq_ligne(indice_ligne)) and (self.freq_ligne(indice_ligne)[tranche][0] > depart_precedent or depart_precedent > self.freq_ligne(indice_ligne)[tranche][1]) :
            tranche += 1
        ecart = self.freq_ligne(indice_ligne)[tranche][2]
        if depart_precedent + ecart > self.freq_ligne(indice_ligne)[-1][1] :
            return [-1, -1]
        intervalle = (ecart // 10) + 1
        return [ecart, intervalle]
    # Cadencements -> int -> int -> [int, int]
