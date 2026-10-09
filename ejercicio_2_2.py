class TipoPlaneta:
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    def __init__(self, nombre: str, cantidad_satelites: int, masa: float, volumen: float, diametro: int, distancia_sol: int, tipo: str, observable: bool):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.observable = observable

    def imprimir_datos(self) -> None:
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa: {self.masa}")
        print(f"Volumen: {self.volumen}")
        print(f"Diámetro: {self.diametro}")
        print(f"Distancia media al Sol (millones de km): {self.distancia_sol}")
        print(f"Tipo de planeta: {self.tipo}")
        print(f"Observable a simple vista: {self.observable}")

    def calcular_densidad(self) -> float:
        if self.volumen == 0:
            return 0.0
        return self.masa / self.volumen

    def es_planeta_exterior(self) -> bool:
        limite_en_km = 3.4 * 149597870
        distancia_en_km = self.distancia_sol * 1000000
        if distancia_en_km > limite_en_km:
            return True
        else:
            return False

def main():
    planeta1 = Planeta("Tierra", 1, 5.972e24, 1.083e12, 12742, 150, TipoPlaneta.TERRESTRE, True)
    planeta2 = Planeta("Júpiter", 79, 1.898e27, 1.431e15, 139820, 778, TipoPlaneta.GASEOSO, True)

    print("--- Datos del Planeta 1 ---")
    planeta1.imprimir_datos()
    print(f"Densidad: {planeta1.calcular_densidad()}")
    print(f"Es planeta exterior: {planeta1.es_planeta_exterior()}")
    
    print("\n--- Datos del Planeta 2 ---")
    planeta2.imprimir_datos()
    print(f"Densidad: {planeta2.calcular_densidad()}")
    print(f"Es planeta exterior: {planeta2.es_planeta_exterior()}")

if __name__ == "__main__":
    main()