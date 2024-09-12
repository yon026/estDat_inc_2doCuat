"""
Crear un programa que permita registrar las inscripciones
de los alumnos de una universidad privada. Debe incluir un
título principal, pedir los datos personales (nombre, edad,
fecha de nacimiento). Crear una variable que muestre True o
False si posee título secundario (ese dato no se pide al 
usuario, se escribe en el programa). Además se deberá 
ingresar el monto de matrícula y calcular la cuota (valor 
de la matrícula + $ 1000). 
La materia "Python I" tiene un arancel especial, cuyo valor 
$ 12000 por cuatrimestre.
Mostrar el costo mensual y calcular un descuento del 15% 
de la cuota para aquellos que paguen en efectivo.
Finalmente se deberán imprimir todos los datos pedidos.
Ejemplo:

Ingrese su nombre: Luis Fernández
Ingrese su edad: 33
Ingrese su fecha de nacimiento dd/mm/yyyy : 25/08/1990
Ingrese monto de la matricula: 3400
Posee titulo?: si

==========================================================
========== Universidad de Python - Inscripciones =========
==========================================================

DATOS DE INGRESO:
Nombre completo: Luis Fernández 
Fecha de nacimiento y edad: 25/08/1990 (33)
Posee titulo: True
Matricula: 3400.0
Cuota mensual: 4400.0
Arancel mensual materia 'PythonI': 3000.0
Arancel mensual materia 'PythonI' con descuento: 2550.0

"""
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
fechaNacimiento = input("Ingrese su fecha de nacimiento dd/mm/yyyy : ")
montoMatricula = float(input("Ingrese monto de la matricula: "))
consulta = ""

while True:
    consulta = input("Posee titulo?: ")
    if consulta == "si":
        titulo = True
        print("")
        break
    elif consulta == "no":
        titulo = False
        print("")
        break
    else:
        print("Dato mal ingresado intente nuevamente")

materiaPyth0n = 12000
cuotaMensual = montoMatricula + 1000
arancelMensualPython = 3000.0
arancelMensualPythonDescuento = arancelMensualPython * 0.85 

print("==========================================================\n========== Universidad de Python - Inscripciones =========\n==========================================================\n")

print(f"DATOS DE INGRESO:\nNombre completo: {nombre} \nFecha de nacimiento y edad: {fechaNacimiento} ({edad})\nPosee titulo: {titulo}\nMatricula: {montoMatricula}\nCuota mensual: {cuotaMensual}\nArancel mensual materia 'PythonI': {arancelMensualPython}\nArancel mensual materia 'PythonI' con descuento: {arancelMensualPythonDescuento}")

