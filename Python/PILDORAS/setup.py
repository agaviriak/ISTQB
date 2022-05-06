#Setup para crear modulos de instalación
from setuptools import setup
setup(
name="Funciones matemáticas básicas",
version="1.0",
description="suma, resta, multiplicación y división",
author="AGC",
packages=["paquetes"]
)

#Para instalar ir a la consola en el directorio de este archivo
# c:>python setup.py sdist
# c:> cd dist
# c:> pip3 install <Nombre del paquete>