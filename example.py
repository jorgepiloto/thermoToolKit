# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 23:29:17 2018

@author: Horus
"""

import thermoToolKit  

print("""
    Bienvenido al programa de ejemplo de THERMO TOOL KIT
    A continuación se le introducirá un ejemplo   
""")

### EJEMPLO DEL USO DE LA HERRAMIENTA "INTERPOLATE"
xa = float(input("Valor para Xa: "))
x = float(input("Valor para X: "))
xb = float(input("Valor para Xb: "))
ya = float(input("Valor para Ya: "))
yb = float(input("Valor para Yb: "))
    
print("The value of Y is {}".format(thermoToolKit.interpolate(xa,x,xb,ya,yb)))