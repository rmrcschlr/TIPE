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

def prive(liste1, liste2) :
    result = []
    for element in liste1 :
        if element not in liste2 :
            result.append(element)
    return result

def array_in(array, list) :
    result = False
    i = 0
    while not(result) and i < len(list) :
        result = array_equal(array, list[i])
        i += 1
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
    # CSP -> string list -> int array -> [fun( ints -> bool ) ; str list] list -> [fun( ints -> float ); str list] list -> CSP
    
    def noms(self) :
        result = []
        for i in range(len(self.liste)) :
            result.append(self.liste[i][0])
        return result
    # CSP -> string list
    
    def indice_variable(self, nom) :
        return self.noms().index(nom)
    # CSP -> string -> int
    
    def ajoute_variable(self, nom, domaine) :
        assert nom not in self.noms(), "La variable existe déjà"
        self.liste.append([nom, domaine])
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
    
    def ajoute_contrainte(self, contrainte, noms) :
        self.contraintes.append([contrainte, noms])
    # CSP -> fun( ints -> bool ) -> str list -> unit
    
    def contraintes_sur_variable(self, nom) :
        result = []
        for i in range(len(self.contraintes)) :
            if nom in self.contraintes[i][1] :
                result.append(i)
        return result
    # CSP -> string -> int list
    
    def variables_liees(self, nom) :
        result = []
        for i in self.contraintes_sur_variable(nom) :
            contrainte = self.contraintes[i]
            variables = aplatir(contrainte[1])
            for j in variables :
                if j != nom :
                    indice = self.indice_variable(j)
                    if indice not in result :
                        result.append(indice)
        return result
    # CSP -> string -> int list
    
    def ajoute_cout(self, cout, noms) :
        self.couts.append([cout, noms])
    # CSP -> fun( ints -> float ) -> str list -> unit
    
    def couts_sur_variable(self, nom) :
        result = []
        for i in range(len(self.couts)) :
            if nom in self.couts[i][1] :
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

def cout_suivant(csp, affectation, cout_initial, variable, valeur) :
    assert valeur in variable[1]
    cout_total = cout_initial
    for indice_cout in csp.couts_sur_variable(variable[0]) :
        cout = csp.couts[indice_cout]
        if inclus(sans(cout[1], variable[0]), list(affectation.keys())) :
            valeurs = []
            for i in range(len(cout[1])) :
                if cout[1][i] == variable[0] :
                    valeurs.append(valeur)
                elif type(cout[1][i]) is list :
                    temp = []
                    for j in range(len(cout[1][i])) :
                        if cout[1][i][j] == variable[0] :
                            temp.append(valeur)
                        else :
                            temp.append(affectation[cout[1][i][j]])
                    valeurs.append(temp)
                else :
                    valeurs.append(affectation[cout[1][i]])
            cout_total += cout[0](*valeurs)
    return cout_total
# CSP -> int dict -> [str, int array] -> int -> int

def domaine_trie(csp, affectation, variable) :
    liste = []
    for i in variable[1] :
        cout_initial = cout_affectation(csp, affectation)
        liste.append([cout_suivant(csp, affectation, cout_initial, variable, i), i])
    liste.sort()
    temp = array(liste)
    if len(temp) == 0 :
        result = array([])
    elif len(temp) == 1 :
        result = array([temp[0, 1]])
    else :
        result = temp[:, 1]
    return result
# CSP -> int dict -> [str, int array] -> int array

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
            condition = condition and csp.contraintes[i][0](*valeurs)
        i += 1
    return condition
# CSP -> int dict -> bool

def domaine_restreint(csp, affectation, variable) :
    result = []
    affectation_temp = affectation.copy()
    for i in variable[1] :
        affectation_temp[variable[0]] = i
        if affectation_consistante(csp, affectation_temp) :
            result.append(i)
    return array(result)
# CSP -> int dict -> [str, int array]

def anticipation(csp, affectation) :
    condition = True
    i = 0
    while condition and i < len(csp.liste) :
        condition = condition and csp.noms()[i] in affectation
        i += 1
    if condition :
        return (True, affectation)
    affectation_temporaire = affectation.copy()
    i = len(affectation)
    variable_i = csp.liste[i]
    domaine_i_initial = variable_i[1].copy()
    variable_i[1] = domaine_restreint(csp, affectation, variable_i)
    variable_i[1] = domaine_trie(csp, affectation, variable_i)
    for valeur_i in variable_i[1] :
        affectation_temporaire[variable_i[0]] = valeur_i
        liste_domaines_initiaux = []
        liste_domaines_temporaires = []
        condition_valeur_i = True
        liste_prochaines_variables = prive(csp.variables_liees(variable_i[0]), map(csp.indice_variable, affectation.keys()))
        compteur = 0
        while condition_valeur_i and compteur < len(liste_prochaines_variables) :
            j = liste_prochaines_variables[compteur]
            variable_j = csp.liste[j]
            liste_domaines_initiaux.append(variable_j[1].copy())
            domaine_j_temporaire = domaine_restreint(csp, affectation_temporaire, variable_j)
            if domaine_j_temporaire == [] :
                condition_valeur_i = False
            liste_domaines_temporaires.append(domaine_j_temporaire)
            compteur += 1
        if not(array_in(array([]), liste_domaines_temporaires)) :
            affectation[variable_i[0]] = valeur_i
            for compteur in range(len(liste_domaines_temporaires)) :
                j = liste_prochaines_variables[compteur]
                csp.liste[j][1] = liste_domaines_temporaires[compteur]
            if anticipation(csp, affectation)[0] :
                return (True, affectation)
            for compteur in range(len(liste_domaines_temporaires)) :
                j = liste_prochaines_variables[compteur]
                csp.liste[j][1] = liste_domaines_initiaux[compteur]
    variable_i[1] = domaine_i_initial
    return (False, affectation)
# CSP -> int dict -> (bool, int dict)

def solution_par_anticipation(csp) :
    affectation = {}
    return anticipation(csp, affectation)
# CSP -> (bool, int dict)
