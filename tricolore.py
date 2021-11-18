#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:17:34 2021

@author: rachid.emziane
"""

def tricolore(n):
    a=str(n)
    for i in a:
        i=int(i)
        if i!=1 and i!=4 and i!=9:
            return False
    return True


def tous_les_tricolores(N):
    L=[]
    for i in range(N):
        if tricolore(i)==True:
            L.append(i)
    return L

print(tous_les_tricolores(1000))
