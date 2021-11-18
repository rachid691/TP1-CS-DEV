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

