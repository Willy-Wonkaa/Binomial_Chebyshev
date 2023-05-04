from cmath import pi
import math
import numpy as np

from plotrefl import *

# Design of binomial without Z-Method

def binom_design(N, Z0, ZL):

    #Naive approach without Z-method

    Zn = [Z0]

    for k in range(0,N):

        nCk = math.comb(N, k)
        
        Zn_next = Zn[k]*(ZL/Z0)**(nCk/2**N)
        Zn.append(Zn_next)
    
    Zn.append(ZL)
    return Zn

# This design a chebyshev transformer with max. reflection coefficient 0.1
#Manually calculated each factor

def chebyshev_4():
    Zn = [50]
    Zn.append(Zn[0]*1.3)
    Zn.append(Zn[0]*1.942)
    Zn.append(Zn[0]*3.134)
    Zn.append(Zn[0]*4.684)
    Zn.append(300)

    return Zn
 
def z_method(N,Z0,Zl):
    n = 1
    p = [math.sqrt(Z0*Zl)]
    while n != N:
        n += 1
        q = []
        t = 0
        for i in range(len(p)):
            if i == 0:
                t = math.sqrt(Z0*p[i])
            else:
                t = math.sqrt(p[i]*p[i-1])
            q.append(t)
        q.append(math.sqrt(p[-1]*Zl))
        p = q
    p.insert(0,Z0)
    p.append(Zl)
    return p

    


