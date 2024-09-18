"""
 Desarrollar una funcion que reciba tres numeros enteros positivos y verifique si
corresponden a una fecha valida ( dia, mes, año ) Devolver true o false segun la 
fecha sea correcta o no. Realizar tambien un programa para verificar el 
comportamiento de la funcion
"""

#Meses con 31 dias 1, 3, 5, 7, 8, 10, 12

#Meses con 30 dias 4, 6, 9, 11

def carga():
    dia = int(input("Ingrese un dia: "))
    mes = int(input("Ingrese un mes: "))
    anio = int(input("Ingrese un año: "))
    
    fecha = [dia,mes,anio]
    return fecha

def validacion(dia, mes, anio):
    mesTreinta = [ 4, 6, 9, 11 ]
    mesTreintaUno = [ 1, 3, 5, 7, 8, 10, 12 ]
    cont = 0
    
    if anio>=0 or anio<=3000:
        cont+=1
        
    if mes>0 or mes<13:
        cont+=1
    
    if (mes in mesTreinta and ( dia<31 and dia>0 ))  or  ( mes in mesTreintaUno and ( dia<=31 and dia>0 ) ):
        cont +=1
    
    if cont == 3:
        resultado = True
    else:
        resultado = False
        
    return resultado, cont

fechaCarga= carga()

print(f"La fecha {fechaCarga[0]}/{fechaCarga[1]}/{fechaCarga[2]} es Fecha valida?", validacion(*fechaCarga))

