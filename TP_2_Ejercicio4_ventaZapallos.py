"""
 Crear un programa que venda zapallos con un costo de 1000 pesos cada uno
 Depende el tipo de divisa que se paga tiene distintos descuentos:
* Si se paga con dolares, tenga un 5% de descuentos, con yenes 15%, con guaranies
20%, pesos 10%
* Debe mostrar los descuentos que tiene segun el tipo de moneda
* Si desea pagar con otro tipo de moneda puede realizarlo pero tiene un AUMENTO
del 10%
* Al final debe emitir un recibo con nombre del comprador, nombre de la empresa,
tipo de moneda, desc o incremento segun la moneda cantidad, producto y precio
total en pesos segun la moneda elegida
"""

costoZapallo = 1000.0

monedas = {"dolares":0.95, "guaranies":0.80, "yenes":0.85, "otra":1.10} #Guardo el descuento o incremento a aplicarse con su respectiva moneda
recibo = {"Nombre del comprador":None,"Nombre de la empresa":None,"Tipo de moneda":None,"Desc. o Inc.":None,"Producto":"zapallo","Cantidad":None,"Precio":None}

print(f"-----------------------Compra de zapallos-----------------------\nElija una de las sgtes. divisas: {", ".join(monedas.keys())}")

while True: #Pedir ingreso hasta que sea una de las monedas existentes
    divisaElegida=input("Ingrese su divisa: ")
    if divisaElegida in monedas.keys():
        recibo["Tipo de moneda"] = divisaElegida
        break
    else:
        print(f"\nERROR! Intente nuevamente\nDivisas disponibles: {", ".join(monedas.keys())}")

if divisaElegida == "otra": #Aplica incremento o descuento segun sea la divisa elegida anteriormente
    recibo["Desc. o Inc."]=f"Incremento del {round((monedas[divisaElegida]-1)*100)}%"
else:
    recibo["Desc. o Inc."]=f"Descuento del {round((1-monedas[divisaElegida])*100)}%"
    
print("\n------Ingrese sus datos para el recibo------")

#Asignacion de valores para el recibo
recibo["Nombre del comprador"]=input("Ingrese su nombre: ")
recibo["Nombre de la empresa"]=input("Ingrese el nombre de su empresa: ")
recibo["Cantidad"]=int(input("Ingrese la cantidad de zapallos: "))
recibo["Precio"]=round(recibo["Cantidad"]*costoZapallo*monedas[divisaElegida])

#Muestra de recibo
print("\nRecibo:")

for k,v in recibo.items():
    print(f"{k}: {v}")




    
