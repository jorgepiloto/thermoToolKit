def fluxRad(e, A, Tsur, Ts):
    
    sigma = 5.67e-8
    
    return e*sigma*A*(Tsur**4 - Ts**4)
