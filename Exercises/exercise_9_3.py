from thermoToolKit.HeatTransfer.heatConvection import resConv, fluxConv
from thermoToolKit.Utils.utils import resParallel

#DATA PROVIDED IN THE EXERCISE:

At = 1.2 #Total area of the surface
Tb = 100 #Temperature of the surface
N = 20 #Number of fins
Tinf = 20 #Temperature of the fluid

h = 100 #Convection coefficient
k = 400 #Conduction of the fin

e = 2.5 #Efectivenness of the fin
Af = 0.1 #Area of the fin
Acb = 0.02 #Contact area between the fin and the base

#COMPUTATIONS REQUIRED FOR THE EXERCISE

Abase = At - N*Acb #Area of the base without the fins
Rbase = resConv(h, Abase) #Convection resistance of the base 
print("Rbase = {}".format(Rbase)) #Print solution

Rfin = 1/(e*h*Acb) #Resistance of one fin
print("Rfin = {}".format(Rfin)) #Print solution

Rfin_tot = Rfin/N #Total resistance of the N fins

Reqv = resParallel(Rbase, Rfin_tot) #Total Equivalent Resistance of the circuit
print("Reqv = {}".format(Reqv)) #Print Soution

q = (Tb- Tinf)/(Reqv) #Compute heat transfered
print("q = {}".format(q)) #Print total heat

qbase = fluxConv(h, Abase, Tb, Tinf)
qf = (q - qbase)/N

n = qf/(h*Af*(Tb-Tinf)) #compute
print("Efficinecy = {}".format(n)) #Print solution
