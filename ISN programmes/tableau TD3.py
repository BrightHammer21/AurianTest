# Créé par aurian.durand, le 14/10/2015 en Python 3.2
ligne=[]
n=input("Entre n un entier positif")
r,c,a=0,0,1
n=int(n)
while r!=n:
    ligne.append(a)
    r=r+1
    a=a+1
print(ligne)
##tableau=[ligne]*n
####print(tableau)
##while c<n:
##    print(tableau[c])
##    c=c+1
