class TipoCombustible:
    GASOLINA = "Gasolina"
    DIESEL = "Diésel"

class TipoAutomovil:
    COMPACTO = "Compacto"
    SUV = "SUV"

class Color:
    BLANCO = "Blanco"
    ROJO = "Rojo"

class Automovil:
    def __init__(self, marca: str, modelo: int, motor: float, combustible: str, tipo: str, puertas: int, asientos: int, vel_max: int, color: str):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.combustible = combustible
        self.tipo = tipo
        self.puertas = puertas
        self.asientos = asientos
        self.vel_max = vel_max
        self.color = color
        self.vel_actual = 0

    # Solo un get/set para cumplir el requisito sin alargar el código
    def get_vel_actual(self) -> int: return self.vel_actual
    def set_vel_actual(self, vel: int) -> None: self.vel_actual = vel
    
    def acelerar(self, inc: int) -> None:
        if self.vel_actual + inc > self.vel_max:
            print("Error: Supera velocidad máxima.")
        else:
            self.vel_actual += inc

    def desacelerar(self, dec: int) -> None:
        if self.vel_actual - dec < 0:
            print("Error: Velocidad negativa.")
        else:
            self.vel_actual -= dec

    def frenar(self) -> None:
        self.vel_actual = 0

    def calcular_tiempo(self, distancia: float) -> float:
        return 0.0 if self.vel_actual == 0 else distancia / self.vel_actual

    def mostrar(self) -> None:
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")
        print(f"Velocidad actual: {self.vel_actual} km/h")
        print("-" * 30)

def main():
    auto = Automovil("Mazda", 2024, 2.0, TipoCombustible.GASOLINA, TipoAutomovil.COMPACTO, 4, 5, 200, Color.ROJO)
    
    auto.set_vel_actual(100)
    print(f"Velocidad ajustada: {auto.get_vel_actual()} km/h")
    
    auto.acelerar(20)
    print(f"Tras acelerar: {auto.get_vel_actual()} km/h")
    
    auto.desacelerar(50)
    print(f"Tras desacelerar: {auto.get_vel_actual()} km/h")
    
    auto.frenar()
    print(f"Tras frenar: {auto.get_vel_actual()} km/h")

if __name__ == "__main__":
    main()