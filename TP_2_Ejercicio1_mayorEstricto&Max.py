"""
 Desarrollar una funcion que reciba tres numeros positivos y devuelva el mayor de
los tres, solo si este es unico ( mayor estricto ) En caso de no existir el mayor
estricto devolver - No utilizar operadores logicos ( and,or, not ) Desarrollar
tambien un programa para ingresar los tres valores, invocar a la funcion y
mostrar el maximo hallado, o un mensaje informativo si este no existe
"""

def mayorEstricto(*valores):
    numeroMaximo=max(valores)
    #[expresion for item in iterable if condicion]
    contador = sum(1 for valor in valores if valor == numeroMaximo )
    
    if contador == 1:
        return numeroMaximo
    else:
        return "Inexistente"

numeros=[]

for i in range(1,4):
    num=0
    while num <= 0:
        num = float(input(f"Ingrese un numero_{i} positivo:"))
    numeros.append(num)

maxNum=mayorEstricto(*numeros)

print(f"El mayor estricto es: {maxNum}" )