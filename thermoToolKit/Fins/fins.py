#######################################################################################
####    THE FOLLOWING FILE CONTAINS ALL THE NECESSARY FUNCTIONS RELATED TO FINS    ####
####                        													   ####
####						 Author: Jorge Marinez Garrido					       ####
####					   														   ####
####						Universidad Carlos III de Madrid					   ####
#######################################################################################

#Import some useful tools
from math import pi, sqrt, cosh, sinh, tanh

#######################################################################################
####    		FIN PROPERTIES: EFFECTIVNESS, EFFICIENCY AND PARAMETER 'm'         ####
#######################################################################################

#Function to compute Effectiveness
def effectivness(qf, h, Acb, Tb, Tinf):

	return qf/(h*Acb*(Tb-Tinf))

#Function to compute Efficiency
def efficinecy(qf, h, Af, Tb, Tinf):

	return qf/(h*Af*(Tb-Tinf))

#Function to compute  m
def m(h, P, kf, Ac):

	return sqrt((h*P)/(Ac*kf))


#######################################################################################
####    		HEAT FOR FINS: CONVECTIVE, ADIABATIC, FIXED OR INFINITE            ####
#######################################################################################

#Function to compute Teta_b
def teta_b(Tb, Tinf):

	return (Tb-Tinf)

#Function to compute Teta_l
def teta_l(Tl, Tinf):

	return (Tl-Tinf)

#Function to check if fin is infinite
def checkFin(h, P, kf, Ac, L):

	m = m(h, P, kf, Ac)
	val = L*m

	if val > 2.65:
		print(val)
		return True

	else:
		print(val)
		return False

#Heat for an infinite fin
def infiniteFin(h, P, kf, Ac, Tb, Tinf):		

	return teta_b(Tb, Tinf)*sqrt(h*P*kf*Ac)

#Heat for a fin with fixed Temperature at the tip
def fixedTipFin(h, P, kf, Ac, L, Tb, Tinf):

	m = m(h, P, kf, Ac)

	return teta_b(Tb,Tinf)*sqrt(h*P*kf*Ac)*(cosh(m*L) - (teta_l/teta_b))/sinh(m*L)

#Heat for adiabatic fin
def adiabaticFin(h, P, kf, Ac, L, Tb, Tinf):

	m = m(h, P, kf, Ac)

	return teta_b(Tb, Tinf)*sqrt(h*P*kf*Ac)*tanh(m*L)

#Heat for a convective tip fin
def convectiveFin(h, P, kf, Ac, L, Tb, Tinf):

	m = m(h, P, kf, Ac)

	return teta_b(Tb, Tinf)*sqrt(h*P*kf*Ac)*((sinh(m*L)+(h/(m*k))*cosh(m*L))/(cosh(m*L)+(h/(m*k)*sinh(m*L))))


#######################################################################################
####    				ANNULAR AND STRAIGHT FINS PROPERTIES		               ####
#######################################################################################

#This function allow the user to know in which line of the graph is located the data [1, 2, 3 or 5]
def getAnnularRatio(r1, r2, t):

	r2_c = r2 + t/2
	Lc = (r2-r1) + t/2
	Ap = Lc*t 

	return r2_c/r1

#This function allows the user to get the value for the X axis on the graph
def getAnnularAxis(r1, r2, t, h, kf):

	Lc = (r2-r1) + t/2
	Ac = Lc*t

	return Lc**(3/2)*(h/(kf*Ac))**0.5
