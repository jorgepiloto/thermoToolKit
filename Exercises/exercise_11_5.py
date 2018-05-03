from thermoToolKit.ForcedConvection.impiningJets import roundNozzle
from thermoToolKit.HeatTransfer.heatConvection import fluxConv
from math import pi

#Properties of the Nozzle
Tn = 500
v = 70
D = 0.001
H = 0.005

#Properties of surface
r = 0.005/2
Ts = 25

#Properties of the air at Tm
Tm = (Tn+Ts)/2
print("Tm for properties of the air is {}ºC or {}K".format(Tm, Tm+273))

ro = 0.6329
cp = 1040
mu = 288.4e-7
kair = 43.9e-3
Pr = 0.683

#Compute Reynolds
Re = (ro*v*D)/mu
print("Re: {}".format(Re))

#Compute Nusselt
Nu = roundNozzle(Re, Pr, H, r, D)
print("Nu: {}".format(Nu))

#Compute convection coefficient
h = Nu*kair/D
print("h: {}".format(h))

A = pi*r**2 #Area of the surface
q = fluxConv(h, A, Ts, Tn)
print("q: {}".format(q))
