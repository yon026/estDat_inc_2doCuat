from collections import deque

class AtencionCliente:
    def __init__(self):
        self.cola = deque()

    def agregar_cliente(self, nombre):
        self.cola.append(nombre)
        print(f"{nombre} ha sido agregado a la cola.")

    def atender_cliente(self):
        if self.cola:
            cliente_atendido = self.cola.popleft()
            print(f"{cliente_atendido} está siendo atendido.")
        else:
            print("No hay clientes en la cola.")

    def clientes_en_cola(self):
        print(f"Clientes en cola: {len(self.cola)}")

# Ejemplo de uso
oficina = AtencionCliente()
oficina.agregar_cliente("Juan")
oficina.agregar_cliente("María")
oficina.clientes_en_cola()
oficina.atender_cliente()
oficina.clientes_en_cola()
oficina.atender_cliente()
oficina.atender_cliente()
