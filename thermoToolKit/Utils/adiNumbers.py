#######################################################################################
####  THE FOLLOWING FILE CONTAINS ALL THE NECESSARY FUNCTIONS RELATED ADINUMBERS   ####
####                        													   ####
####						 Author: Jorge Marinez Garrido					       ####
####					   														   ####
####						Universidad Carlos III de Madrid					   ####
#######################################################################################


#######################################################################################
####    FUNCTIONS TO COMPUTE DIFFERENT NON-DIMENSIONAL NUMBERS USED IN PROBLEMS    ####
#######################################################################################

def reynolds(ro, v, L, mu):

	return (ro*v*L)/mu

def prandlt(mu, cp, k):

	return (mu*cp)/k

def nusselt(h, Dh, k):

	return (h*Dh)/k