#######################################################################################
####    THE FOLLOWING FILE CONTAINS ALL THE NECESSARY FUNCTIONS RELATED TO JETS    ####
####                        													   ####
####						 Author: Jorge Marinez Garrido					       ####
####					   														   ####
####						Universidad Carlos III de Madrid					   ####
#######################################################################################

#Function to compute Nusselt Number for Round Nozzle
def roundNozzle(Re, Pr, H, r, D):

	c = (D/r)

	G = c * (1 - 1.1*c)/(1+0.1*(H/D-6)*c)

	return 2*G*(Re**0.5)*((1+0.005*Re**0.55)**0.5)*Pr**(0.42)

#Function to compute Nusselt Number for Slot Nozzle
def slotNozzle(Re, Pr, H, x, W, Dh):

	m = 0.695 - ((x/Dh)+(H/Dh)**1.33 + 3.06)**(-1)

	return (3.06/((x/W) + (H/W) + 2.78))*(Re**m)*(P**0.42)