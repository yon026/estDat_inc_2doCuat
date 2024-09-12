"""
La universidad ahora pide un programa que permita cargar las notas de dos exámenes y
obtener el promedio. Además deberá determinar si el alumno aprobó el último examen
(nota mayor o igual a 7), en caso contrario informar que desaprobó.
Además se desea saber si el alumno mejoró, empeoró o mantuvo su desempeño entre
ambos parciales. Para ello se deberá informar "Mejoró su desempeño" si la nota del
segundo parcial es mayor que la del primero, "Mantuvo la nota" si ambas notas son
iguales o "Empeoró su desempeño" si la nota del primer parcial es mayor que la del
segundo.
Finalmente, la universidad desea saber si el alumno promocionó la materia (promedio
mayor o igual a 7), debe rendir final (promedio mayor o igual a 4) o debe recursar.

Ejemplo:
Ingrese la nota del primer parcial: 7
Ingrese la nota del segundo parcial: 9
El promedio de las notas es:  8.0
Aprobó el segundo parcial
Progreso del 1er al 2do parcial: Mejoró su desempeño
Promocionó la materia
"""

primerParcial = float(input("Ingrese la nota del primer parcial: "))
segundoParcial = float(input("Ingrese la nota del segundo parcial: "))
promedio = (primerParcial+segundoParcial) / 2

print("El promedio de las notas es: ", promedio)


if segundoParcial > primerParcial:
    print("Aprobó el segundo parcial\nProgreso del 1er al 2do parcial: Mejoró su desempeño")
elif segundoParcial < primerParcial:
    print("Desaprobó el segundo parcial\nProgreso del 1er al 2do parcial: Empeoró su desempeño")
else:
    print("Igualó el segundo parcial\nProgreso del 1er al 2do parcial: Mantuvo la nota")
    
if promedio >= 7:
    print("Promocionó la materia")
elif promedio>=4:
    print("Debe rendir final")
else:
    print("Recursa la materia")