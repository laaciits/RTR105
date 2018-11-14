# -*- coding: utf-8 -*-
from math import sin
# S0, S1, S2, S3 -> S

x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = sin(x/2)
print("sin(%.2f) = %.2f"%(x,y))

a0 = (-1)**0*x**(2*0+1)/(2*0+1)*2**(2*2*0+1)
S = a0
print("a0 = %.2f S0 = %.2f"%(a0,S))

a1 = (-1)**1*x**(2*1+1)/(2*1+1)*2**(2*1+1)
#S1 = (a0) + a1
#S1 = S0 + a1
S = S + a1
print("a1 = %.2f S1 = %.2f"%(a1,S))

a2 = (-1)**2*x**(2*2+1)/(2*2+1)*2**(2*2+1)
#S2 = (a0 + a1) + a2
#S2 = S1 + a2
S = S + a2
print("a2 = %.2f S2 = %.2f"%(a2,S))

a3 = (-1)**3*x**(2*3+1)/(2*3+1)*2**(2*3+1)
#S3 = (a0 + a1 + a2) + a3
#S3 = S2 + a3
S = S + a3
print("a3 = %.2f S3 = %.2f"%(a3,S))
