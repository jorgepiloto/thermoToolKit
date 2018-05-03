#######################################################################################
#### THE FOLLOWING FILE CONTAINS ALL THE NECESSARY FUNCTIONS RELATED TO EXTERNAL   ####
####                        													   ####
####						 Author: Jorge Marinez Garrido					       ####
####					   														   ####
####						Universidad Carlos III de Madrid					   ####
#######################################################################################

#Importing Adimensional Numbers 
from thermoToolKit.Utils.adiNumbers import reynolds, prandlt, nusselt

#######################################################################################
####    			FUNCTIONS TO COMPUTE EXTERNAL FLOW CONVECTION				   ####
####																			   ####
####					1) Parallel flow over a flat plate						   ####
####					2) Flow across a Sphere									   ####
####					3) Flow across a Cylinder								   ####
####					4) Flow across a tube bank								   ####
####					5) Impining Jets										   ####
####																			   ####
#######################################################################################


#######################################################################################
####    				  PARALLEL FLOW OVER A FLAT PLATE 					       ####
#######################################################################################

ReCritical = 5e10 #We define the critial Rynolds number to check Laminar or Turbulent

def lamiUniSurfTemp(Re, Pr): 

	return 0.664*(Re**0.5)*(Pr**(1/3))

def lamiUniSurfHeat(Re, Pr):

	return 0.906*(Re**0.5)*(Pr**(1/3))

def turbuUniSurfTemp(Re, Pr):

	return 0.0296*(Re**(4/5)*Pr**(1/3))

def turbUniSurfHeat(Re, Pr):

	return 0.0308*(Re**(4/5)*Pr**(1/3))

def mixUniTemp(Re, Pr):

	return (0.037*Re**(4/5)-871)*Pr**(1/3)

def mixUniHeat(Re, Pr):

	return (0.0385*Re**(4/5)-754.5)*Pr**(1/3)


#######################################################################################
####    				  		   FLOW ACROSS A SPHERE 					       ####
#######################################################################################

def flowSphere(Re, Pr, mu, mu_s):

	return 2+(0.4*Re**0.5 + 0.06*Re**(2/3))*Pr**(0.4)*(mu/mu_s)**(1/4)

#######################################################################################
####    				  		  FLOW ACROSS A CYLINDER 					       ####
#######################################################################################

def flowCylinder(Re, Pr, case):
	
	if case is 'Circle':
		
		if 0 < Re < 4:

			C = 0.989
			m = 0.330
			Nu = C*(Re**m)*(Pr**(1/3))
			

		elif 4 < Re < 40:
			C = 0.911
			m = 0.385
			Nu = C*(Re**m)*(Pr**(1/3))
			

		elif 40 < Re < 4000:
			C = 0.683
			m = 0.466
			Nu = C*(Re**m)*(Pr**(1/3))
			

		elif 4000 < Re < 40000:
			C = 0.193
			m = 0.618
			Nu = C*(Re**m)*(Pr**(1/3))

		else:
			C = 0.027
			m = 0.805
			Nu = C*(Re**m)*(Pr**(1/3))

	elif case is 'Square':
		C = 0.102
		m = 0.675
		Nu = C*(Re**m)*(Pr**(1/3))

	elif case is 'Square_tilted':
		C = 0.246
		m = 0.588
		Nu = C*(Re**m)*(Pr**(1/3))

	elif case is 'Hexagon':

		if 5e3 < Re < 1.95e4:
			C = 0.160
			m = 0.638
			Nu = C*(Re**m)*(Pr**(1/3))

		else:
			C = 0.0385
			m = 0.782
			Nu = C*(Re**m)*(Pr**(1/3))

	elif case is 'Hexagon_tilted':
		C = 0.153
		m = 0.638
		Nu = C*(Re**m)*(Pr**(1/3))

	elif case is 'Vertical':
		C = 0.228
		m = 0.731
		Nu = C*(Re**m)*(Pr**(1/3))

	elif case is 'Ellipse':
		C = 0.248
		m = 0.612
		Nu = C*(Re**m)*(Pr**(1/3))

	else:

		C = 0
		m = 0
		Nu = 0

	print("C: {}   m: {}".format(C, m))	

	return Nu