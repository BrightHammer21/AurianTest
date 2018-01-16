# Créé par aurian.durand, le 23/09/2015 en Python 3.2
a=input("Entrez une phrase:\n")
#print(a)
b=0
for i in range(1,len(a)+1):
    if a[i-1]=="a":
        print(i)
        b=b+1
if b==0:
    print("Il n'y a pas de a")