# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:10:20 2021

@author: rachid.emziane
"""

def mesImpots(revenu):
    if revenu<=10084:
        return 0
    elif 10085<=revenu<=25710:
        return (revenu-10084)*0.11
    elif 25711<=revenu<73516:
        return (revenu-25711)*0.3+(25710-10084)*0.11
    elif 73517<=revenu<=158122:
        return (revenu-73517)*0.41+(73516-25711)*0.3+(25710-10084)*0.11
    else:
        return (revenu-158122)*0.45+(158122-73517)*0.45+(73516-25711)*0.3+(25710-10084)*0.11

        
revenu=int(input("Quel est votre salaire?"))
a=mesImpots(revenu)
print("Impot="+str(a))
