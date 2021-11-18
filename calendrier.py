"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def bis(annee):
    if annee%4 !=0 :
        return False
    elif annee%1000 ==0 and annee%400 !=0:
        return False
    else:
        return True

def nombrejour(annee,mois):
    M31=[1,3,5,7,8,10,12]
    if mois==2:
        if bis(annee)==True:
            return 29
        else:
            return 28
    for i in M31:
        return 31
    return 30

def datevalide(jour,mois,annee):
    njour=nombrejour(annee,mois)
    if  jour>njour:
        return False
    else:
        return True

jour=int(input("Numéro du jour?"))
mois=int(input("Numéro du mois?"))
while mois<=0 and mois>12:
    mois=int(input("Numéro du mois entre 1 et 12?"))
annee=int(input("Numéro de l'année?"))
if datevalide(jour,mois,annee)==True:
    print("date valide")
else:
    print("date non valide")

