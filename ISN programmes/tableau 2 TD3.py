# Créé par aurian.durand, le 18/11/2015 en Python 3.2
n=input("Entrez un n positif")
n=int(n)
ligne=[]
tableau=[]

#construction première ligne
for i in range(1,n+1,1):
    ligne.append(i)

tableau.append(ligne)

#construction des lignes de la table

for j in range(1,n+1,1):
    ligne=[]
    ligne.append(str(j))
    for i in range(1,n+1,1):
        ligne.append(i*j)
    tableau.append(ligne)


for a in range(1,n+1,1):
    print(tableau[i])

