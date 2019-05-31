from numpy import *
from time import time

def map(fonction, liste) :
    result = []
    for element in liste :
        result.append(fonction(element))
    return result

def sans(liste, valeur) :
    result = []
    for element in liste :
        if element != valeur :
            result.append(element)
    return result

def element_dans_intervalle(liste, borne_inf, borne_sup) :
    assert liste != []
    longueur = len(liste)
    result = False
    indice = 0
    while (not result) and (indice < longueur) :
        result = result or (borne_inf <= liste[indice] <= borne_sup)
        indice += 1
    return result
    

### Réseau avec 2 lignes et 1 correspondance
"""
liste = ['T1,0', 'T1,1', 'T2,0', 'T2,1', 'C']

matrice = []
for i in range(4) :
    matrice.append((i * [-1]) + [0] + ((3 - i) * [-1]))
matrice[0].append(1)
matrice[1].append(2)
matrice[2].append(3)
matrice[3].append(4)
matrice.append([1, 2, 3, 4, 0])

RESEAU = Reseau(liste, matrice)

RESEAU.ajouter_ligne('L1', ['T1,0', 'C', 'T1,1', 'C'], ['T1,0', 'T1,1'])
RESEAU.ajouter_ligne('L2', ['T2,0', 'C', 'T2,1', 'C'], ['T2,0', 'T2,1'])

CADENCEMENTS = Cadencements(RESEAU)
CADENCEMENTS.ajouter_frequence(0, 0, 29, 2)
CADENCEMENTS.ajouter_frequence(1, 0, 29, 3)
CADENCEMENTS.ajouter_frequence(0, 30, 59, 5)
CADENCEMENTS.ajouter_frequence(1, 30, 59, 7)

### Réseau avec 3 lignes et 1 correspondance

liste = ['T1,0', 'T1,1', 'T2,0', 'T2,1', 'T3,0', 'T3,1', 'C']

matrice = []
for i in range(6) :
    matrice.append((i * [-1]) + [0] + ((5 - i) * [-1]))
matrice[0].append(1)
matrice[1].append(2)
matrice[2].append(3)
matrice[3].append(4)
matrice[4].append(5)
matrice[5].append(6)
matrice.append([1, 2, 3, 4, 5, 6])

RESEAU = Reseau(liste, matrice)

RESEAU.ajouter_ligne('L1', ['T1,0', 'C', 'T1,1', 'C'], ['T1,0', 'T1,1'])
RESEAU.ajouter_ligne('L2', ['T2,0', 'C', 'T2,1', 'C'], ['T2,0', 'T2,1'])
RESEAU.ajouter_ligne('L3', ['T3,0', 'C', 'T3,1', 'C'], ['T3,0', 'T3,1'])

CADENCEMENTS = Cadencements(RESEAU)
CADENCEMENTS.ajouter_frequence(0, 0, 29, 2)
CADENCEMENTS.ajouter_frequence(1, 0, 29, 3)
CADENCEMENTS.ajouter_frequence(2, 0, 29, 5)
CADENCEMENTS.ajouter_frequence(0, 30, 59, 7)
CADENCEMENTS.ajouter_frequence(1, 30, 59, 11)
CADENCEMENTS.ajouter_frequence(2, 30, 59, 13)

### Réseau avec 3 lignes et 2 correspondances

liste = ['T1,0', 'T1,1', 'T2,0', 'T2,1', 'T3,0', 'T3,1', 'C1,2', 'C1,3']

matrice = []
for i in range(6) :
    matrice.append((i * [-1]) + [0] + ((5 - i) * [-1]))
matrice[0].append(1)
matrice[0].append(-1)
matrice[1].append(-1)
matrice[1].append(2)
matrice[2].append(3)
matrice[2].append(-1)
matrice[3].append(4)
matrice[3].append(-1)
matrice[4].append(-1)
matrice[4].append(5)
matrice[5].append(-1)
matrice[5].append(6)
matrice.append([1, -1, 3, 4, -1, -1, 0, 7])
matrice.append([-1, 2, -1, -1, 5, 6, 7, 0])

RESEAU = Reseau(liste, matrice)

RESEAU.ajouter_ligne('L1', ['T1,0', 'C1,2', 'C1,3', 'T1,1', 'C1,3', 'C1,2'], ['T1,0', 'T1,1'])
RESEAU.ajouter_ligne('L2', ['T2,0', 'C1,2', 'T2,1', 'C1,2'], ['T2,0', 'T2,1'])
RESEAU.ajouter_ligne('L3', ['T3,0', 'C1,3', 'T3,1', 'C1,3'], ['T3,0', 'T3,1'])

CADENCEMENTS = Cadencements(RESEAU)
CADENCEMENTS.ajouter_frequence(0, 0, 29, 2)
CADENCEMENTS.ajouter_frequence(1, 0, 29, 3)
CADENCEMENTS.ajouter_frequence(2, 0, 29, 5)
CADENCEMENTS.ajouter_frequence(0, 30, 59, 7)
CADENCEMENTS.ajouter_frequence(1, 30, 59, 11)
CADENCEMENTS.ajouter_frequence(2, 30, 59, 13)
"""
### Réseau avec 3 lignes et 3 correspondances

liste = ['T1,0', 'T1,1', 'T2,0', 'T2,1', 'T3,0', 'T3,1', 'C1,2', 'C1,3', 'C2,3']

matrice = []
for i in range(6) :
    matrice.append((i * [-1]) + [0] + ((5 - i) * [-1]))
matrice[0].append(1)
matrice[0].append(-1)
matrice[0].append(-1)
matrice[1].append(-1)
matrice[1].append(2)
matrice[1].append(-1)
matrice[2].append(3)
matrice[2].append(-1)
matrice[2].append(-1)
matrice[3].append(-1)
matrice[3].append(-1)
matrice[3].append(4)
matrice[4].append(-1)
matrice[4].append(5)
matrice[4].append(-1)
matrice[5].append(-1)
matrice[5].append(-1)
matrice[5].append(6)

matrice.append([1, -1, 3, -1, -1, -1, 0, 7, 8])
matrice.append([-1, 2, -1, -1, 5, -1, 7, 0, 9])
matrice.append([-1, -1, -1, 4, -1, 6, 8, 9, 0])

RESEAU = Reseau(liste, matrice)

RESEAU.ajouter_ligne('L1', ['T1,0', 'C1,2', 'C1,3', 'T1,1', 'C1,3', 'C1,2'], ['T1,0', 'T1,1'])
RESEAU.ajouter_ligne('L2', ['T2,0', 'C1,2', 'C2,3', 'T2,1', 'C2,3', 'C1,2'], ['T2,0', 'T2,1'])
RESEAU.ajouter_ligne('L3', ['T3,0', 'C1,3', 'C2,3', 'T3,1', 'C2,3', 'C1,3'], ['T3,0', 'T3,1'])

CADENCEMENTS = Cadencements(RESEAU)

CADENCEMENTS.ajouter_frequence(0, 0, 29, 15)
CADENCEMENTS.ajouter_frequence(1, 0, 29, 15)
CADENCEMENTS.ajouter_frequence(2, 0, 29, 15)
CADENCEMENTS.ajouter_frequence(0, 30, 59, 10)
CADENCEMENTS.ajouter_frequence(1, 30, 59, 10)
CADENCEMENTS.ajouter_frequence(2, 30, 59, 10)
"""
CADENCEMENTS.ajouter_frequence(0, 0, 29, 2)
CADENCEMENTS.ajouter_frequence(1, 0, 29, 3)
CADENCEMENTS.ajouter_frequence(2, 0, 29, 5)
CADENCEMENTS.ajouter_frequence(0, 30, 59, 7)
CADENCEMENTS.ajouter_frequence(1, 30, 59, 11)
CADENCEMENTS.ajouter_frequence(2, 30, 59, 13)
"""

t1 = time()
Probleme_initial = CSP()

###Rentre les variables et leur domaine dans le CSP

variables_triees = []
for indice_ligne in range(len(RESEAU.liste_lignes)) :
    variables_triees.append([])
    for terminus in RESEAU.ligne_terminus(indice_ligne) :
        variables_triees[-1].append([])
        compteur = 0
        depart, marge = CADENCEMENTS.premier_depart(indice_ligne)
        domaine = arange(depart, depart + marge + 1)
        Probleme_initial.ajoute_variable(RESEAU.nom_ligne(indice_ligne) + ';' + RESEAU.nom_arret(terminus) + ';' + str(compteur), domaine)
        variables_triees[-1][-1].append(RESEAU.nom_ligne(indice_ligne) + ';' + RESEAU.nom_arret(terminus) + ';' + str(compteur))
        Probleme_initial.ajoute_cout(lambda a : a, [RESEAU.nom_ligne(indice_ligne) + ';' + RESEAU.nom_arret(terminus) + ';' + str(compteur)])
        compteur += 1
        cadencement, marge = CADENCEMENTS.prochain_depart(indice_ligne, depart)
        while cadencement != -1 :
            depart = depart + cadencement
            minimum = min(domaine + cadencement) - marge
            maximum = max(domaine + cadencement) + marge
            domaine = arange(minimum, maximum + 1)
            Probleme_initial.ajoute_variable(RESEAU.nom_ligne(indice_ligne) + ';' + RESEAU.nom_arret(terminus) + ';' + str(compteur), domaine)
            variables_triees[-1][-1].append(RESEAU.nom_ligne(indice_ligne) + ';' + RESEAU.nom_arret(terminus) + ';' + str(compteur))
            Probleme_initial.ajoute_contrainte(lambda a, b, cadencement = cadencement, marge = marge : abs(b - cadencement - a) <= marge, [RESEAU.nom_ligne(indice_ligne) + ';' + RESEAU.nom_arret(terminus) + ';' + str(compteur - 1), RESEAU.nom_ligne(indice_ligne) + ';' + RESEAU.nom_arret(terminus) + ';' + str(compteur)])
            Probleme_initial.ajoute_cout(lambda a, b, cadencement = cadencement : abs(b - cadencement - a),[RESEAU.nom_ligne(indice_ligne) + ';' + RESEAU.nom_arret(terminus) + ';' + str(compteur - 1), RESEAU.nom_ligne(indice_ligne) + ';' + RESEAU.nom_arret(terminus) + ';' + str(compteur)])
            compteur +=1
            cadencement, marge = CADENCEMENTS.prochain_depart(indice_ligne, depart)

#raise RuntimeError("Pause")

### Résout le CSP avec critere

ecart_max = 0
for indice_ligne in range(len(CADENCEMENTS.liste)) :
    for freq in range(len(CADENCEMENTS.freq_ligne(indice_ligne))) :
        if CADENCEMENTS.freq_ligne(indice_ligne)[freq][2] > ecart_max :
            ecart_max = CADENCEMENTS.freq_ligne(indice_ligne)[freq][2]
critere = ecart_max + 1

solution_trouvee = True
while solution_trouvee and critere > 0 :
    critere -= 1
    print(critere)
    Probleme_complet = Probleme_initial.copie()
    for indice_arret in range(len(RESEAU.liste_arrets)) :
        liste_variables_arret = []
        for indice_ligne in RESEAU.correspondance(indice_arret) :
            liste_variables_arret.append(variables_triees[indice_ligne])
        for compteur_ligne in range(len(liste_variables_arret)) :
            for compteur_terminus in range(len(liste_variables_arret[compteur_ligne])) :
                tranche_variables = liste_variables_arret[compteur_ligne][compteur_terminus]
                for indice_variable in range(len(tranche_variables) - 1) :
                    temps1 = RESEAU.duree(RESEAU.indice_ligne(tranche_variables[indice_variable].split(';')[0]), RESEAU.indice_arret(tranche_variables[indice_variable].split(';')[1]), indice_arret)
                    for indice_ligne in sans(RESEAU.correspondance(indice_arret), RESEAU.indice_ligne(tranche_variables[0].split(';')[0])) :
                        for indice_terminus in RESEAU.ligne_terminus(indice_ligne) :
                            temps2 = RESEAU.duree(indice_ligne, indice_terminus, indice_arret)
                            if temps2 != -1 :
                                domaine_variable_actuelle = Probleme_complet.domaine_variable(tranche_variables[indice_variable])
                                domaine_reference = arange(domaine_variable_actuelle[0], domaine_variable_actuelle[-1] + critere + 1)
                                variables_utiles = []
                                for nom in variables_triees[indice_ligne][RESEAU.ligne_terminus(indice_ligne).index(indice_terminus)] :
                                    if not(array_equal(intersect1d(domaine_reference, Probleme_complet.domaine_variable(nom)), [])) :
                                        variables_utiles.append(nom)
                                if variables_utiles != [] :
                                    Probleme_complet.ajoute_contrainte(lambda a, b, l, critere = critere, temps1 = temps1, temps2 = temps2 : not(element_dans_intervalle(map((lambda x : x + temps2), l), a + temps1, b + temps1 - 1)) or element_dans_intervalle(map((lambda x : x + temps2 - a - temps1), l), 0, critere), [tranche_variables[indice_variable], tranche_variables[indice_variable + 1]] + [variables_utiles])
    Solution_potentielle = solution_par_anticipation(Probleme_complet)
    solution_trouvee = Solution_potentielle[0]
    if solution_trouvee :
        Solution = Solution_potentielle 

### Affiche la solution dans une liste
t2 = time()
if Solution[0] :
    result = []
    for indice_ligne in range(len(RESEAU.liste_lignes)) :
        ligne = []
        for terminus in RESEAU.ligne_terminus(indice_ligne) :
            arret = []
            compteur = 0
            while RESEAU.nom_ligne(indice_ligne) + ';' + RESEAU.nom_arret(terminus) + ';' + str(compteur) in Solution[1] :
                arret.append(Solution[1][RESEAU.nom_ligne(indice_ligne) + ';' + RESEAU.nom_arret(terminus) + ';' + str(compteur)])
                compteur += 1
            ligne.append(arret)
        result.append(ligne)
print(critere + 1)
print(array(result))
print(array(hill_climbing(Horaires(result))))
print(t2 - t1)
