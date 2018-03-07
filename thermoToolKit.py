### LIBRERÍA DE thermoToolKit

def interpolate(xa, x, xb, ya, yb):
    
    return ((x-xa)/(xb-xa))*(yb-ya) + ya

def compVapQuality(mw, mv):
    
    return mv/(mw+mv)

def getVapQuality(ul, ug, u):
    
    return (u-ul)/(ug-ul)

def getProperty(ul, ug, x):
    
    return x*ug + (1-x)*ug


    
    