import math

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio
        
    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)
        
    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
        
    def calcular_area(self) -> float:
        return self.base * self.altura
        
    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado
        
    def calcular_area(self) -> float:
        return self.lado * self.lado
        
    def calcular_perimetro(self) -> float:
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
        
    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2
        
    def calcular_hipotenusa(self) -> float:
        return math.sqrt((self.base ** 2) + (self.altura ** 2))
        
    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()
        
    def determinar_tipo(self) -> str:
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura and self.base == hipotenusa:
            return "Equilátero"
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            return "Escaleno"
        else:
            return "Isósceles"

def main():
    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)
    cuadrado = Cuadrado(3)
    triangulo = TrianguloRectangulo(3, 4)
    
    print(f"Círculo - Área: {circulo.calcular_area():.2f}, Perímetro: {circulo.calcular_perimetro():.2f}")
    print(f"Rectángulo - Área: {rectangulo.calcular_area()}, Perímetro: {rectangulo.calcular_perimetro()}")
    print(f"Cuadrado - Área: {cuadrado.calcular_area()}, Perímetro: {cuadrado.calcular_perimetro()}")
    
    print(f"Triángulo Rectángulo - Área: {triangulo.calcular_area()}, Perímetro: {triangulo.calcular_perimetro()}")
    print(f"Hipotenusa: {triangulo.calcular_hipotenusa()}, Tipo: {triangulo.determinar_tipo()}")

if __name__ == "__main__":
    main()