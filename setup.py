from setuptools import setup

setup(
	
	name = "thermoToolKit",
	version = "1.0",
	description = "A small package to compute interesting Thermodynamic properties and solving heat transfer problems",
	author = "Jorge Martinez Garrido",
	author_email = "100349480@alumnos.uc3m.es",
	scripts = [],
	packages = ["thermoToolKit", "thermoToolKit.HeatTransfer", "thermoToolKit.Utils", "thermoToolKit.Fins", "thermoToolKit.ForcedConvection", "thermoToolKit.Utils"]

	)

