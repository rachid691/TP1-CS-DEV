#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:29:51 2021

@author: rachid.emziane
"""

def multiplication(B,C):
    A=[]
    m=0
    k=0
    while k<len(B):
        m=0
        for i in B:
            aii=0
            
            ind=0
            indC=0
            
            for j in C:
                
                aii+=i[ind]*j[indC+k]
                ind+=1
            indC+=1
            if len(A) !=len(B):
                A.append([aii])
            else:
                A[m].append([aii])
                m+=1
        k+=1
    return A

def affichage(A):
    for i in A:
        print (i)
        
B=[[1,2,3],[2,3,3],[4,5,6]]
C=[[6,8,3],[7,4,3],[2,1,0]]
A=multiplication(B, C)
affichage(A)

            
