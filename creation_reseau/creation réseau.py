import os as os
from numpy import inf

os.chdir("E:\TIPE")
f=open("Horaires.csv",'r')
txt = f.read()

txt = txt.split("\n")
for i in range(len(txt)):
    txt[i] = txt[i].split(",")

for i in range(len(txt)):
    txt[i][0]=int(txt[i][0])
    txt[i][3]=int(txt[i][3])
    txt[i][5]=txt[i][5].split("h")
    txt[i][5]=60*int(txt[i][5][0])+int(txt[i][5][1])

arrets = []

for i in range(len(txt)):
    if  not( txt[i][1] in arrets):
        arrets.append(txt[i][1])
        
itinerances = [ [] for i in range(len(arrets))]

for i in range(len(itinerances)):
    for j in range(len(txt)):
        if arrets[i] == txt[j][1] and not((int(txt[j][0])*int(txt[j][3])) in itinerances[i]):
            itinerances[i].append(int(txt[j][0])*int(txt[j][3]))
            
arrets_non_sym = []
            
for i in range(len(itinerances)):
    for j in range(len(itinerances[i])):
        if not([arrets[i],i] in arrets_non_sym)and not(-itinerances[i][j] in itinerances[i]):
            arrets_non_sym.append([arrets[i],i])

lignes = [[] for i in range(18)]

for i in range(1,len(txt)):
    if txt[i][3]!=txt[i-1][3] or itinerances[arrets.index(txt[i][1])]!=itinerances[arrets.index(txt[i-1][1])]:
        lignes[txt[i][0]].append(txt[i][1])
        
arrets_opti =[]

for i in range(len(lignes)):
    for j in range(len(lignes[i])):
        if not(lignes[i][j] in arrets_opti):
            arrets_opti.append(lignes[i][j])
            
matrice_adj = [ [ inf for i in range(len(arrets_opti)) ] for j in range(len(arrets_opti)) ]

txt_par_ligne = []

i=0
while i < len(txt)-1 :
    L=[txt[i]]
    while (i < len(txt)-1)and(txt[i][0]*txt[i][3] == txt[i+1][0]*txt[i+1][3]) :
        L.append(txt[i+1])
        i+=1
    txt_par_ligne.append(L)
    L=[]
    i+=1
  
for k in range(len(txt_par_ligne)):
    s=0
    j = arrets_opti.index(txt_par_ligne[k][0][1])
    for i in range(1,len(txt_par_ligne[k])):
        s += (-txt[i-1][5]+txt[i][5])
        if txt_par_ligne[k][i][1] in arrets_opti :
            temp = arrets_opti.index(txt_par_ligne[k][i][1])
            matrice_adj[j][temp]=s
            j=temp
            s=0
            
lignes2 = lignes.copy()

for i in range(len(lignes)):
    l=[]
    for j in range(1,len(lignes[i])):
        if lignes[i][j-1] == lignes[i][j] or not(lignes[i][j] in arrets_opti):
            l.append(j-1)
    print(l)
    for k in range(len(l)):
        del lignes2[i][l[k]-k]