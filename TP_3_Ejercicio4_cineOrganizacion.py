# Corroborar funcionamiento

class Cine:
    def __init__(self):
        self.butacas = [['Vacío' for _ in range(10)] for _ in range(7)]
        self.reservaciones = {}

    def mostrar_butacas(self):
        for fila in self.butacas:
            print(" ".join(fila))
        print("\n")

    def reservar_butaca(self, fila, columna, nombre, telefono):
        if self.butacas[fila][columna] == 'Vacío':
            self.butacas[fila][columna] = 'Usado'
            self.reservaciones[(fila, columna)] = {'nombre': nombre, 'telefono': telefono}
            print(f"Asiento en fila {fila+1}, columna {columna+1} reservado exitosamente.")
        else:
            print("El asiento ya está reservado.")

    def consultar_reservacion(self, fila, columna):
        if (fila, columna) in self.reservaciones:
            info = self.reservaciones[(fila, columna)]
            print(f"Reservado por: {info['nombre']}, Teléfono: {info['telefono']}")
        else:
            print("El asiento no está reservado.")

# Ejemplo de uso
cine = Cine()
cine.mostrar_butacas()
cine.reservar_butaca(2, 5, 'Juan Pérez', '123456789')
cine.mostrar_butacas()
cine.consultar_reservacion(2, 5)
cine.consultar_reservacion(0, 0)
