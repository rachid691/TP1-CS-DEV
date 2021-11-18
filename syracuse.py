#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:54:54 2021

@author: rachid.emziane
"""

def syracus(N):
    
    while N!=1:
        if N%2==0:
            N=N/2
        else:
            N=N*3 +1

def altitude(N):
    
    maximum=N
    while N!=1:
        if N%2==0:
            N=N/2
        else:
            N=N*3 +1
        if N>maximum:
            maximum=N
    return maximum

def tpsdevol(N):
    k=0
    while N!=1:
        if N%2==0:
            N=N/2
        else:
            N=N*3 +1
        k+=1
    return k


tvol=0
alt=0
maxTVol=0
maxAlt=0
for i in range(1,1000):
    if maxTVol<tpsdevol(i):
        maxTVol=tpsdevol(i)
        tvol=i
    if maxAlt<altitude(i):
        maxAlt=altitude(i)
        alt=i
        
print(tvol,alt)
        
