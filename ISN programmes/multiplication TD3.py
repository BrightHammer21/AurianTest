# Créé par aurian.durand, le 04/11/2015 en Python 3.2
n=int(input("entrer un n positif"))
ligne=[]
tab=[]
for i in range(1,n+1,1):
    ligne.append(i)
tab.append(ligne)
print(tab)
for j in range(1,n+1,1):
    tab.append(j)
    j=j*i
    tab.append(ligne)
print(tab)