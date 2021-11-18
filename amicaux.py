#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:35:56 2021

@author: rachid.emziane
"""

def amicaux(n,m):
    L1=[]
    L2=[]
    for i in range(1,n+1):
        if n%i==0:
            L1.append(i)
    for i in range(1,m+1):
        if m%i==0:
            L2.append(i) 
    Sn=0
    for i in L1:
        Sn+=i
    Sm=0
    for i in L2:
        Sm+=i
    if Sn==Sm==(n+m):
        return True
    else:
        return False
    
    
print (amicaux(220,284 ))
    
