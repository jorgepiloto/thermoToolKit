#######################################################################################
#### THE FOLLOWING FILE CONTAINS ALL THE NECESSARY FUNCTIONS RELATED TO EXTERNAL   ####
####                        													   ####
####						 Author: Jorge Marinez Garrido					       ####
####					   														   ####
####						Universidad Carlos III de Madrid					   ####
#######################################################################################

ReCritical = 5e10 #We define the critial Rynolds number to check Laminar or Turbulent

#######################################################################################
####    			FUNCTIONS TO COMPUTE EXTERNAL FLOW CONVECTION				   ####
#######################################################################################

def lamiUniSurfTemp(Re, Pr):

	return 0.664*(Re**0.5)*(Pr**(1/3))

def lamiUniSurfHeat(Re, Pr):

	return 0.906*(Re**0.5)*(Pr**(1/3))

def turbuUniSurfTemp(Re, Pr):

	return


