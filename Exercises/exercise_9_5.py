from math import pi

t = 0.01 #Thickness of a fin
R2 = 0.08 #External radius
R1 = 0.04 #Internal radius
e = 9.1 #Efectivennes
h = 550 #COnvection coefficient

#COMPUTING THE PROBLEM

Acb = (2*pi*R1)*t #Area contact base
Af = (2*pi*R2*t) + 2*(pi*(R2**2-R1**2)) #Area of the fins

n = (e*Acb)/(Af) #Compujting the efficiency
print("Eficiencia = {}".format(n)) #Print the solution

R2c = R2+(t/2) #Computing R2c
L = R2-R1 #Computing L
Lc = L+(t/2) #Computing Lc
Ap = Lc*t #Computing Ap
ratio = R2c/R1
print("Ratio = {}".format(ratio))

x = 0.8 #This is an appx value for the X-Axis looking at the tables
k = (Lc**3/x**2)*(h/Ap) #Solving the value of k
print("k = {}".format(k)) #Print the solution
