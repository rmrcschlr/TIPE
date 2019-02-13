from numpy import *

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

def map(fonction, liste) :
    result = []
    for element in liste :
        result.append(fonction(element))
    return result

def aplatir(liste) :
    liste_aplatie = []
    for element1 in liste :
        if type(element1) == list :
            for element2 in element1 :
                liste_aplatie.append(element2)
        else :
            liste_aplatie.append(element1)
    return liste_aplatie

def sans(liste, valeur) :
    result = []
    for element in liste :
        if element != valeur :
            result.append(element)
    return result

class CSP :
    
    def __init__(self, noms = [], domaine = [], liste_contraintes = [], liste_couts = []) :
        self.liste = []
        if domaine != [] :
            self.ajoute_variables(noms, domaine)
        self.contraintes = []
        for contrainte in liste_contraintes :
            self.ajoute_contrainte(contrainte[0], contrainte[1])
        self.couts = []
        for cout in liste_couts :
            self.ajoute_cout(cout[0], cout[1])
    # CSP -> string list -> int array -> CSP
    
    def noms(self) :
        result = []
        for i in range(len(self.liste)) :
            result.append(self.liste[i][1])
        return result
    # CSP -> string
    
    def ajoute_variable(self, nom, domaine) :
        assert nom not in self.noms(), "La variable existe déjà"
        self.liste.append([0, nom, domaine]) # le O est l'arite de la variable
    # CSP -> string -> int array -> unit
    
    def ajoute_variables(self, noms, domaine) :
        assert noms != [] and domaine != []
        if type(noms) is not list :
            self.ajoute_variable(noms, domaine)
        else :
            if type(domaine[0]) is int :
                for i in range(len(noms)) :
                    self.ajoute_variable(noms[i], domaine)
            elif type(domaine[0]) is not int and len(noms) == len(domaine) :
                for i in range(len(noms)) :
                    self.ajoute_variable(noms[i], domaine[i])
            else :
                print("Les domaines ne sont soit pas du bon type, soit leur nombre est different de celui des noms")
    # CSP -> string list -> int array list -> unit
    
    def ajoute_contrainte(self, contrainte, variables) :
        self.contraintes.append([contrainte, variables])
    # CSP -> fun( ints -> bool ) -> str list-> unit
    
    def contraintes_sur_variable(self, variable) :
        result = []
        for i in range(len(self.contraintes)) :
            if variable in self.contraintes[i][1] :
                result.append(i)
        return result
    # CSP -> string -> int list
    
    def arite(self, variable) :
        return len(self.contraintes_sur_variable(variable))
    # CSP -> string -> int
    
    def trie_variables_statique(self) :
        for i in range(len(self.liste)) :
            self.liste[i][0] = self.arite(self.liste[i][1])
        self.liste.sort()
        self.liste.reverse()
    # CSP -> unit
    
    def ajoute_cout(self, cout, variables) :
        self.couts.append([cout, variables])
    # CSP -> fun( ints -> (int or float) ) -> str list -> unit
    
    def couts_sur_variable(self, variable) :
        result = []
        for i in range(len(self.couts)) :
            if variable in self.couts[i][1] :
                result.append(i)
        return result
    # CSP -> string -> int list

def cout_affectation(csp, affectation) :
    cout_total = 0
    for cout in csp.couts :
        if inclus(aplatir(cout[1]), list(affectation.keys())) :
            valeurs = []
            for i in range(len(cout[1])) :
                if type(cout[1][i]) is list :
                    temp = []
                    for j in range(len(cout[1][i])) :
                        temp.append(affectation[cout[1][i][j]])
                    valeurs.append(temp)
                else :
                    valeurs.append(affectation[cout[1][i]])
            cout_total += cout[0](*valeurs)
    return cout_total
# CSP -> int dict -> int

def cout_suivant(csp, affectation, variable, valeur) :
    assert valeur in variable[2]
    cout_initial = cout_affectation(csp, affectation)
    for cout in csp.couts :
        if variable[1] in cout[1] and inclus(sans(cout[1], variable[1]), list(affectation.keys())) :
            valeurs = []
            for i in range(len(cout[1])) :
                if cout[1][i] == variable[1] :
                    valeurs.append(valeur)
                elif type(cout[1][i]) is list :
                    temp = []
                    for j in range(len(cout[1][i])) :
                        temp.append(affectation[cout[1][i][j]])
                    valeurs.append(temp)
                else :
                    valeurs.append(affectation[cout[1][i]])
            cout_initial += cout[0](*valeurs)
    return cout_initial
# CSP -> int dict -> [int, str, int array] -> int -> int

def domaine_trie(csp, affectation, variable) :
    liste = []
    for i in variable[2] :
        liste.append([cout_suivant(csp, affectation, variable, i), i])
    liste.sort()
    temp = array(liste)
    if len(temp) == 1 :
        result = array([temp[0, 1]])
    else :
        result = temp[:, 1]
    return result
# CSP -> int dict -> [int, str, int array] -> int array

def affectation_consistante(csp, affectation) :
    condition = True
    i = 0
    while condition and i < len(csp.contraintes) :
        if inclus(aplatir(csp.contraintes[i][1]), list(affectation.keys())) :
            valeurs = []
            for j in range(len(csp.contraintes[i][1])) :
                if type(csp.contraintes[i][1][j]) is list :
                    temp = []
                    for k in range(len(csp.contraintes[i][1][j])) :
                        temp.append(affectation[csp.contraintes[i][1][j][k]])
                    valeurs.append(temp)
                else :
                    valeurs.append(affectation[csp.contraintes[i][1][j]])
            #if not(csp.contraintes[i][0](*valeurs)) :
                #print(csp.contraintes[i][1])
                #print(*valeurs)
            condition = condition and csp.contraintes[i][0](*valeurs)
        i += 1
    return condition
# CSP -> int dict -> bool

def anticipation(csp, affectation) :
    condition = True
    i = 0
    while condition and i < len(csp.liste) :
        condition = condition and csp.noms()[i] in affectation
        i += 1
    if condition :
        return (True, affectation)
    i = len(affectation)
    csp.liste[i][2] = domaine_trie(csp, affectation, csp.liste[i])
    variable_i = csp.liste[i]
    for valeur_i in variable_i[2] :
        liste_domaines_temporaires = []
        j = i + 1
        condition_valeur_i = True
        while condition_valeur_i and j < len(csp.liste) :
            variable_j = csp.liste[j]
            liste_domaines_temporaires.append([])
            for valeur_j in variable_j[2] :
                affectation_temporaire = affectation.copy()
                affectation_temporaire[variable_i[1]] = valeur_i
                affectation_temporaire[variable_j[1]] = valeur_j
                if affectation_consistante(csp, affectation_temporaire) :
                    liste_domaines_temporaires[j - i - 1].append(valeur_j)
            if liste_domaines_temporaires[j - i - 1] == [] :
                condition_valeur_i = False
            j += 1
        if [] not in liste_domaines_temporaires :
            affectation[variable_i[1]] = valeur_i
            for j in range(len(liste_domaines_temporaires)) :
                csp.liste[j + i + 1][2] = liste_domaines_temporaires[j]
            if anticipation(csp, affectation)[0] :
                return (True, affectation)
    return (False, affectation)
# CSP -> int dict -> (bool, int dict)

def solution_par_anticipation(csp) :
    #csp.trie_variables_statique()
    affectation = {}
    return anticipation(csp, affectation)
# CSP -> (bool, int dict)
