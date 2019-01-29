def voisin(M,t,interdit):
    voisin=[]
    for i in range(len(M[t])):
        if M[t][i] != -1 and not(i in interdit):
            voisin.append(i)
    return voisin
    
# list of list of float -> int -> list of int -> list of int

def colonne(mat,c):
    L=[]
    for i in range(len(mat)):
        L.append(mat[i][c])
    return L
    
# list of list of a' -> int -> list of a'

def sans_0(K):
    k=[]
    for i in K:
        if i != 0:
            k.append(i)
    return k
    
# list of float -> list of float

def dijkstar(M,d,a):
    l = [ [0,[]] for i in range(len(M)) ]
    l[d][1]=[d]
    inter=[d]
    while d != a:
        print(d)
        dvoisin=voisin(M,d,inter)
        print(len(dvoisin))
        for i in dvoisin:
            if l[i][0]==0:
                l[i][0]=l[d][0]+M[d][i]
                l[i][1]=l[d][1][:]
            else:
                if l[d][0]+M[d][i] < l[i][0]:
                    l[i][1]=l[d][1][:]
                l[i][0]=min(l[d][0]+M[d][i],l[i][0])
        inter.append(d)
        l[d][0]=0
        x=colonne(l,0).index(min(sans_0(colonne(l,0))))
        l[x][1]+=[x]
        d=x
        print(l)
    return l[a]
    
# list of list of float -> int -> int -> float*list of int

m=[[-1,85,217,-1,173,-1,-1,-1,-1,-1],[85,-1,-1,-1,-1,80,-1,-1,-1,-1],[217,-1,-1,-1,-1,-1,186,103,-1,-1],[-1,-1,-1,-1,-1,-1,-1,183,-1,-1],[173,-1,-1,-1,-1,-1,-1,-1,-1,502],[-1,80,-1,-1,-1,-1,-1,-1,250,-1],[-1,-1,186,-1,-1,-1,-1,-1,-1,-1],[-1,-1,103,183,-1,-1,-1,-1,-1,167],[-1,-1,-1,-1,-1,250,-1,-1,-1,84],[-1,-1,-1,-1,502,-1,-1,167,84,-1]]