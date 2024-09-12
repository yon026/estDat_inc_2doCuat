"""
La universidad requiere un programa para organizar las aulas para los alumnos de primer año, de acuerdo
al número de día, sabiendo que 1 es lunes y 6 es sábado.
a. Aulas: Desarrollar un programa que permita ingresar el número de día entre 1 y 6. Los días cuyo número
de orden son pares los alumnos cursan en el aula A-300, mientras que aquellos días impares cursan en el 
aula A-315.
b. Descuento: Además se requiere un programa que otorgue un descuento especial del 25% en el valor de la
cuota a aquellos alumnos que deseen cursar en el turno Tarde y se inscriban a más de 3 materias, para el
resto de los casos el descuento será de un 5%. El programa debe imprimir el valor de la cuota con descuento
de acuerdo al caso.
c. Estacionamiento: También se requiere que el programa asigne un costo diario de estacionamiento de $ 300
a aquellos alumnos que vengan en auto o en moto y de $ 50 si vienen en bicicleta

Ejemplo:
==================== Aulas ====================
Ingrese el numero del dia: 1 (lunes) a 6 (sábado): 4
Aula: A-300
========= Descuento y estacionamiento =========
Ingrese el turno: Mañana, Tarde o Noche: Tarde
Ingrese la cantidad de materias: 4
El valor de la cuota es: 7500.0
Ingrese el vehículo en el que ingresa: Auto, Moto o Bicicleta:
Auto
El costo de estacionamiento para Auto es: 300

Contador de palabras para que el formato coincida
frase_uno="==================== Aulas ===================="
frase_dos="========= Descuento y estacionamiento ========="
cont1 = 0
cont2 = 0
for i in frase_uno:
    cont1+=1

for i in frase_dos:
    cont2+=1

print(cont1,"letras tiene frase 1")
print(cont2,"letras tiene frase 2")
"""

vehiculo=""
turno=""
medioTransporte=""
cuota = float(input("Ingrese el valor de la cuota: "))

while True:
    print("==================== Aulas ====================")
    dia=int(input("Ingrese el numero del dia: 1 (lunes) a 6 (sábado):\n"))
    if (dia>6 or dia<1):
        print("El valor ingresado es incorrecto, intente nuevamente")
        continue
    else:
        break

if dia % 2 == 0:
    aula = "A-300"
else:
    aula = "A-315"

print("Aula:",aula)



while not(turno == "mañana" or turno == "tarde" or turno == "noche"):
    print("========= Descuento y estacionamiento =========")
    turno=input("Ingrese el turno: Mañana, Tarde o Noche:\n").lower()

cantidadMateria = int(input("Ingrese la cantidad de materias: "))
print(f"El valor de la cuota es ${cuota}")

if cantidadMateria > 3 and turno == "tarde":
    cuotaDescuentoExtra = cuota * 0.75
    print(f"Aplica descuento de 25% en cuota, cuota final= ${cuotaDescuentoExtra}")
else:
    cuotaDescuentoNormal = cuota * 0.95
    print(f"Aplica descuento de 5% en cuota, cuota final= ${cuotaDescuentoNormal}")


while not(medioTransporte=="si" or medioTransporte=="no"):
    medioTransporte=input("Posee vehiculo si/no:\n").lower()

if medioTransporte == "si":
    while not(vehiculo=="auto" or vehiculo=="moto" or vehiculo=="bicicleta"):
        vehiculo = input("Ingrese el vehículo en el que ingresa: Auto, Moto o Bicicleta:\n").lower()
    
    if vehiculo == "auto" or vehiculo == "moto":
        estacionamiento = 300
    else:
        estacionamiento = 50
    print(f"El costo de estacionamiento para {vehiculo} es ${estacionamiento}")    
else:
    print("No abona estacionamiento")


