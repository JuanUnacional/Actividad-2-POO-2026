class Persona:
    def __init__(self, nombre: str, apellido: str, documento: str, anio_nacimiento: int):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.anio_nacimiento = anio_nacimiento

    def imprimir_datos(self) -> None:
        print(f"Nombre completo: {self.nombre} {self.apellido}")
        print(f"Documento de identidad: {self.documento}")
        print(f"Año de nacimiento: {self.anio_nacimiento}")
        print("-" * 30)

def main():
    persona1 = Persona("Juan Jose", "Arcila Vega", "1000000000", 2008)
    persona2 = Persona("Walter Hugo", "Arboleda Mazo", "99999999", 1980)

    print("Datos de la Persona 1:")
    persona1.imprimir_datos()
    
    print("Datos de la Persona 2:")
    persona2.imprimir_datos()

if __name__ == "__main__":
    main()