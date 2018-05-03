from thermoToolKit.ForcedConvection.externalConvection import turbUniSurfHeat

#Temperatures and fluxes
Tinf = -10 
q_flux = 150

#Geometrical data
L = 5 #Characteristic length
v = 900 * (1000/3600) #Speed in m/s

#Properties of the air
ro = 0.9
cp = 1000
mu = 1.32e-5
kair = 0.018

Re = (ro*v*L)/mu #Reynolds Number
Pr = cp*mu/kair #Prandtls Number

if Re>5e5:
	print("Turbulent")
else:
	print("Laminar")

print("Re: {}	Pr: {}".format(Re, Pr)) #This case is turbulent over a flat plane

Nu = turbUniSurfHeat(Re, Pr) #Compute Nusselt Number using ThermoToolKit
print("Nu: {}".format(Nu))

h = Nu*kair/L #we get the convection coefficient
print("h: {}".format(h))

delta_t = q_flux/h
print("|(Tinf - Ts)| = {}".format(delta_t))

