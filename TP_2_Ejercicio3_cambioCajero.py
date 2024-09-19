"""
 Un comercio de eletrodomesticos necesita para su linea de cajas un programa que
le indique al cajero el cambio que se debe entregarle al cliente. Para eso se 
ingresan dos numeros enteros, correspondientes al total de la compra y al dinero
recibido, informar cuantos billetes de cada denominacion deben ser entregados al 
cliente como vuelto, de tal forma que se minimice la cantidad de billetes. 
Considerar que existen billetes de $500, $100, $50, $20, $10, $5, $1 Emitir un
mensaje de error si el dinero recibido fuera insuficiente.
 Ejemplo: Si la compra es de $317 y se abona con $500, el vuelto debe contener 1
billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes
de $1
"""

d = [500, 100, 50, 20, 10, 5, 1] # valores de billetes existentes
lb = len(d) #cantidad de billetes existentes
b = [0] * lb #cantidad de billetes por cada valor existente para posterior operacion de calculo

n1 = int(input("\nIngrese el total de la compra: "))
while True:
    n2 = int(input("\nIngrese el dinero recibido: "))
    if n2 < n1:
        print(f"\nEl dinero recibido es insuficiente, intente nuevamente.\nSu total de compra es ${n1}")
    else:
        break
        
n = v = n2-n1 #Vuelto y primer variable de iteracion
print("\nVuelto:")

for i in range(lb):
    
    if n == 0 and i == 0:
        print("       cero")
        break
    elif n<d[i]:
        continue
    else:
        b[i] = n // d[i]
        n = n %  d[i]  
        
        if b[i] == 1:
            print(f"       {b[i]} billete de ${d[i]}")
        else:
            print(f"       {b[i]} billetes de ${d[i]}")    
    