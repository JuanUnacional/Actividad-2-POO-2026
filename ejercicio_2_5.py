class TipoCuenta:
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:
    def __init__(self, nombres: str, apellidos: str, numero_cuenta: str, tipo_cuenta: str):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0  # Se inicializa en 0 según el requerimiento

    def imprimir(self) -> None:
        print(f"Titular: {self.nombres} {self.apellidos}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta}")
        print(f"Saldo actual: ${self.saldo}")
        print("-" * 30)

    def consultar_saldo(self) -> float:
        return self.saldo

    def consignar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            print(f"Se consignaron ${valor}. Saldo actualizado: ${self.saldo}")

    def retirar(self, valor: float) -> None:
        if valor > self.saldo:
            print("Error: El valor a retirar supera el saldo actual de la cuenta.")
        elif valor > 0:
            self.saldo -= valor
            print(f"Se retiraron ${valor}. Saldo actualizado: ${self.saldo}")

def main():
    # Creación de la cuenta
    cuenta = CuentaBancaria("Juan", "Pérez", "123456789", TipoCuenta.AHORROS)
    
    # Pruebas de los métodos
    cuenta.imprimir()
    cuenta.consignar(150000)
    print(f"Consulta directa de saldo: ${cuenta.consultar_saldo()}")
    cuenta.retirar(50000)
    cuenta.retirar(200000)  # Esto debe lanzar el error de saldo insuficiente
    cuenta.imprimir()

if __name__ == "__main__":
    main()