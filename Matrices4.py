# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 19:26:21 2025

@author: fg_sa
"""
import numpy as np


a = np.array([[1/30,1/20,1/60]])
b = np.array([[587,233,235]])
c = np.transpose(a)*b
dp = np.floor(c)
d = np.transpose(dp)
comb1 = d[0,0]*d[1,1]*d[2,2]
comb2 = d[0,1]*d[1,2]*d[2,0]
comb3 = d[0,2]*d[1,0]*d[2,1]
comb4 = d[2,0]*d[1,1]*d[0,2]
comb5 = d[2,1]*d[1,2]*d[0,0]
comb6 = d[2,2]*d[1,0]*d[0,1]
comb = np.array([[comb1,comb2,comb3,comb4,comb5,comb6]])
combmax = comb.max() # valor de combinacion maxima
index_max = np.argmax(comb) # posicion de combinacion maxima
print(d)
#print(c)
print(combmax)
space_matp = np.concatenate((b, b, b), axis=0)
space_mat = np.transpose(space_matp)
cont_mat = np.array([[30,0,0],[0,20,0],[0,0,60]])
wasted_mat = space_mat - np.matmul(d,cont_mat)