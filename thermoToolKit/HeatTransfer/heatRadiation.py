def fluxRad(e, A, Tsur, Ts):
    
    sigma = 5.67e-8
    
    return e*sigma*A*(Tsur**4 - Ts**4)

def resRad(A, F):

	return 1/(A*F)

def resBlackBody(A, e):

	return (1-e)/(A*e)
