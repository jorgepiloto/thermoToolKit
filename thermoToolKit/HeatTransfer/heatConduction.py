#######################################################################################
#### THE FOLLOWING FILE CONTAINS ALL THE NECESSARY FUNCTIONS RELATED TO CONDUCTION ####
####                        													  ####
####						 Author: Jorge Marínez Garrido					      ####
####					   														  ####
####						Universidad Carlos III de Madrid					      ####
#######################################################################################

#Import some usefull mathematical tools:
from numpy import log
from numpy import pi

#######################################################################################
####    FUNCTIONS TO COMPUTE THE FLUX: CARTESSIAN, CYLINDRICAL AND SPHERICAL       ####
#######################################################################################

#This function gets the heat flux for cartesian coordinates:
def fluxCondCart(t, k, A, Tmax, Tmin): 

	R = resCond(t,k,A)

	return (Tmax-Tmin)/R


#This function gets the heat flux for cylindrical coordinates
def fluxCondCyl(k, l, r1, r2, Tmax, Tmin):

	R = resCyl(r1, r2, l, k)

	return (Tmax-Tmin)/R

#This function gets the heat flux for spherical coordinates
def fluxCondEsph(k, r1, r2, Tmax, Tmin):

	R = resSheric(r1, r2, k)

	return (Tmax-Tmin)/R

########################################################################################
#### FUNCTIONS TO COMPUTE THERMAL RESISTANCE: CARTESSIAN, CYLINDRICAL AND SPHERICAL ####
########################################################################################

def resCart(t,k, A):

	return t/(k*A)

def resCyl(r1, r2, l, k):

	return log(r2/r1)/(2*pi*k*l)

def resSheric(r1, r2, k):

	return (1/r1 - 1/r2)/(4*pi*k)



