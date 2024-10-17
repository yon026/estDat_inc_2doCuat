def validaBalance(cadena):
    pila = []
    for caracter in cadena:
        if caracter == "(":
            pila.append(caracter)
        elif caracter == ")":
            if not pila:
                return False
            pila.pop()
    return len(pila) == 0



# La funcion validaBalance carga  la  pila  con ( y si no coincide ese valor evalua si es ).
# De ser ) y estar vacia la pila retorna falso, de lo contrario borra el ( cargado anteriormente
# para volver a comenzar el bucle. Al final del mismo si la pila esta vacia devuelve Verdadero
# justificando el balance de parentesis


# Valores de prueba
# ()() Devuelve True
# ((())) Devuelve True
# (() Devuelve False
# )( Devuelve False

valor = input("Ingrese los parentesis: ")
if validaBalance(valor):
    print("Parentesis balanceados")
else:
    print("Parentesis no balanceados")
