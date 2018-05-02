# ThermoToolKit

ThermoToolKit is a library that contains a set of usefull functions to compute different interesting thermodynamic properties such us thermal resistances, heat fluxes or even experimental ones.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

For version 1.0, no additional modules are required. Is advisable to run this code in python 3.X. The author of this package is currently using "Python 3.6" with Anaconda.

```
Python 3.6
```

### Installing

The following step by step series of examples will help you to easily install this package: 

```
pip install thermoToolKit-1.0.tar.gz
```

This should be all. If not working on Python3, try with:

```
pip3 install thermoToolKit-1.0.tar.gz
```

For LINUX users, it is advisable to use sudo (SuperUser Privileges), in case not working.

## Examples Using ThermoToolKit

This is an example for user to check the powers of 'ThermoToolKit'

### Convection Coefficient for cross flow over a cylinder

A cylindrical fin is made of stainless steel with kf=16 W/mK. The fin diameter is 5mm
and length is 10 cm. Air at 27 ºC, 1 atm, and velocity 50 m/s cross-flow the fin. The
base of the fin is maintained at 127 ºC.

* Calculate the average convection heat transfer coefficient for 	 the fin surface and the heat rate from the fin.

<p align="center">
  <img width="460" height="170" src="http://www.thermopedia.com/content/5637/TUBES_CROSSFLOW_OVER_FIG1.gif">
</p>


We first import the useful modules from thermoToolKit

```
#ThermoToolKit
from thermoToolKit.ForcedConvection.externalConvection import flowCylinder
from thermoToolKit.Fins.fins import infiniteFin

#PROBLEMS DATA
Tinf = 27 #Air temperature
Tb = 127 #Temperature of the base
Tm = (Tinf + Tb)/2 #Temperature for properties
print("Tm for properties of the air is {}ºC or {}K".format(Tm, Tm+273))

#AIR PROPERTIES
ro = 0.995
mu = 208.2e-7
cp = 1009
kair = 30e-3
Pr = 0.7

#GEOMETRIC PROPERTIES
v = 50 
L = 0.1
D = 0.005

#Computing Reynolds
Re = (ro*v*D)/mu
print("Re: {}".format(Re))

#Computing Nusselt
Nu = flowCylinder(Re, Pr, 'Circle')
print("Nu: {}".format(Nu))

#Compute Convection Coefficient
h = Nu*kair/D
print("h: {}".format(h))

#Compute now the heat for the Fin
kf = 16
qf = infiniteFin(h, kf, D, Tb, Tinf)
print("qf: {}".format(qf))
```

As a result for previous code, we obtain the following output

```
Tm for properties of the air is 77.0ºC or 350.0K
Re: 11947.646493756003
C: 0.193   m: 0.618
Nu: 56.71315700147356
h: 340.27894200884134
qf: 4.097815603250402

```


## Future Versions

In following versions, it would be interesting to add some "physical units", so user could check if computations are done well

## Built With

* Python 3.6 (Anaconda)
* Sublime Text 3 

## Authors

* **Jorge Martinez** -Aerospace Engineering Student- 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details