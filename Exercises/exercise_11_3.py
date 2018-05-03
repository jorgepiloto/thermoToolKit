from thermoToolKit.ForcedConvection.externalConvection import flowCylinder
from thermoToolKit.Fins.fins import infiniteFin, checkFin
from math import pi 

Tinf = 27 #Air temperature
Tb = 127 #Temperature of the base
Tm = (Tinf + Tb)/2 #Temperature for properties
print("Tm for properties of the air is {}ºC or {}K".format(Tm, Tm+273))

#Properties at that temeperature
ro = 0.995
mu = 208.2e-7
cp = 1009
kair = 30e-3
Pr = 0.7

#Data of the problem
v = 50 #Speed of air
L = 0.1
D = 0.005

#Computing Reynolds
Re = (ro*v*D)/mu
print("Re: {}".format(Re))

#Computing Nusselt
Nu = flowCylinder(Re, Pr, 'Circle')
print("Nu: {}".format(Nu))

h = Nu*kair/D
print("h: {}".format(h))

#Compute now the heat for the Fin
kf = 16
P = pi*D
Ac = pi*(D**2)/4

qf = infiniteFin(h, P, kf, Ac, Tb, Tinf)
print("qf: {}".format(qf))

### FROM NOW PART B OF THE EXERCISE IS SOLVED ###
print("\n\n")

D = 0.008 #Side of the fin
Re = (ro*v*D)/mu
print("Re: {}".format(Re))

Nu = flowCylinder(Re, Pr, 'Square')
print("Nu: {}".format(Nu))

h = Nu*kair/D
print("h: {}".format(h))

#Parameter for compute m*L > 2.65

P = 4*D #Perimeter of the fin
Ac = D**2 #Cross area of the fin

inf_fin = checkFin(h, P, kf, Ac, L) #Boolean if fin is infinite
print(inf_fin) #Print bool variable

qf = infiniteFin(h, P, kf, Ac, Tb, Tinf)
print(qf)