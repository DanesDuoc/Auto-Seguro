# -*- coding: utf-8 -*-
"""principal_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kvR0DhyQA-CrU0bJgj_0WnhVpO6zpC7G
"""

import funciones_1

print("\n --- ¡Bienvenido a Auto Seguro! ---")
print("\nElige una de las siguientes opciones:\n1.Ingresar y grabar nuevo vehículo\n2.Buscar vehículo\n3.Imprimir certificados\n4.Salir del programa")


while True:
  opcion = int(input("\nIngresa una opción: "))
  if opcion == 1:
    funciones_1.grabar(vehiculos)
  elif opcion == 2:
    funciones_1.buscar(vehiculos)
  elif opcion == 3:
    funciones_1.imprimir_certificados(vehiculos)
  elif opcion == 4:
    funciones_1.salir()
    break