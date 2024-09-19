"""
La universidad esta mejorando sus sistemas y ha solicitado lo siguiente:
A) Listado de aulas:  desarrollar un programa que muestre en dos columnas el número de día y el aula, de
acuerdo al número de día par o impar desarrollado en el ejercicio anterior. Imprimir el listado como el 
siguiente:

Ejemplo:
=========Listado de Aulas=========
Dia Aula
1 A-315
2 A-300
...
5 A-315
6 A-300

B) Carga de edades: se desea mejorar el sistema de carga de edades, validando que correspondan a mayores
de edad. Desarrollar un programa que solicite edades válidas e imprima la edad ingresada y cuántas cargas
erróneas se realizaron.
C) Promedio de notas: cargar las notas de 5 alumnos y obtener el promedio (for). Nota: Al usar for probar
cómo se podría plantear el ejercicio usando 1, 2 o 3 parámetros.
D) Costo del comedor: Finalmente se pide calcular el costo del comedor. La cuota vale $ 1250 por día y se
desea imprimir un informe que muestre la cantidad de días (de 1 a 6) y el costo total (for). Por ejemplo: 
1 día cuesta $ 1250, 2 días cuestan $ 2500…

Ejemplo:
========================Carga de edades========================
Ingrese una edad mayor o igual a 18: 16
Error! Ingrese una edad mayor o igual a 18: 12
Error! Ingrese una edad mayor o igual a 18: 5
Error! Ingrese una edad mayor o igual a 18: 18
La edad ingresada es: 18
Se ha ingresado la edad erróneamente 3 veces

========================Promedio de notas========================
Ingrese la nota: 8
Ingrese la nota: 4
Ingrese la nota: 7
Ingrese la nota: 6
Ingrese la nota: 10
El promedio de notas es: 7.0

========================Costo del comedor========================
Dia             Costo
1               $ 1250
2               $ 2500
3               $ 3750
4               $ 5000
5               $ 6250
6               $ 7500
"""


dia = [1,2,3,4,5,6]
cargasErroneas=1
edad = 0

print("=============== Listado de aulas ===============")
print("Día          Aula")
for i in dia:
    if i % 2 == 0:
        aula = "A-300"
        print(i,"          ",aula)
    else:
        aula = "A-315"
        print(i,"          ",aula)

while edad <18:
    if cargasErroneas == 1:
        edad = int(input("Ingrese una edad mayor o igual a 18: "))    
    else:  
        edad = int(input("Error! Ingrese una edad mayor o igual a 18: "))
    cargasErroneas += 1

print(f"La edad ingresada es: {edad}\nSe ha ingresado la edad erroneamente {cargasErroneas-2} veces")

curso=dict()
costoDiaComedor = 1250

for i in range(1,6):
    notas=[]
    alumno = input(f"\nIngrese el nombre completo del alumno_{i}: ")
    print("\n====================== Carga de notas ======================")
    for j in range(1,6):
        nota = float(input(f"Ingrese la nota_{j} del alumno {alumno}: "))
        notas.append(nota)
      
    curso[alumno] = notas

# curso = {"Renzo":[3.0,6.0], "Laura":[3.33,2.99]} #Valor de prueba

print("\n====================== Promedio de notas ======================")
for k in curso:
    print(f"El alumno {k} tiene {sum(curso[k])/len((curso[k]))} de promedio")
    
print("\n====================== Costo del comedor ======================\nDia                Costo")

for l in range(1,7):
    print(f"{l}                  $ {costoDiaComedor*l}")