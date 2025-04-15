class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    def __str__(self):
        return f"Nombre completo: {self.nombre} {self.apellido}\nNumero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}"
    def depositar(self, valor_a_depositar):
        self.balance += valor_a_depositar
        print(f"Se depositaron ${valor_a_depositar}")
    def retirar(self, valor_a_retirar):
        if valor_a_retirar <= self.balance:
            self.balance -= valor_a_retirar
            print(f"Se retiraron ${valor_a_retirar}")
        else:
            print(f"No hay suficiente dinero para retirar ${valor_a_retirar}")

def menu(cliente):
    menu = ["Consultar cuenta", "Depositar", "Retirar", "Salir"]
    while True:
        for opcion, item in enumerate(menu):
            print(f"{opcion + 1} - {item}")
        opcion = int(input())
        match opcion:
            case 1:
                print(cliente)
            case 2:
                valor_a_depositar = int(input("Ingrese la cantidad a depositar: "))
                cliente.depositar(valor_a_depositar)
                print(cliente)
            case 3:
                valor_a_retirar = int(input("Ingrese la cantidad a retirar: "))
                cliente.retirar(valor_a_retirar)
                print(cliente)
            case 4:
                break
cliente = Cliente("Alex", "Bolivar", 123456789, 100)
menu(cliente)