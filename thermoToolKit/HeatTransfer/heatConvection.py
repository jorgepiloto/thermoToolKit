#######################################################################################
#### THE FOLLOWING FILE CONTAINS ALL THE NECESSARY FUNCTIONS RELATED TO CONVECTION ####
####                        													  ####
####						 Author: Jorge Marinez Garrido					      ####
####					   														  ####
####						Universidad Carlos III de Madrid					      ####
#######################################################################################


#######################################################################################
####    			   FUNCTIONS TO COMPUTE THE FLUX FOR CONVECTION     		   ####
#######################################################################################

#This function gets the convection flux for cartesian coordinates
def fluxConv(h, A, Tmax, Tmin):

	R = resConv(h, A)

	return (Tmax-Tmin)/R


########################################################################################
#### 			FUNCTIONS TO COMPUTE THERMAL RESISTANCE IN CONVECTION 			    ####
########################################################################################

#This function computes the thermal resistance for convection heat transfer
def resConv(h, A):

	return 1/(h*A)
	