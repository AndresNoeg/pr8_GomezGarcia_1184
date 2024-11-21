# Clase Persona
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        # Inicializa los datos de la persona: nombre, edad y DNI
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        # Devuelve los datos de la persona como texto
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

    def esMayorDeEdad(self):
        # Verifica si la persona tiene 18 años o más
        return self.edad >= 18



if __name__ == "__main__":
    # Crea una persona con nombre, edad y DNI
    persona = Persona("Noé Gómez", 20, "12345678A")
    
    # Muestra los datos de la persona
    print(persona.mostrar())
    
    # Indica si es mayor de edad
    print("Mayor de edad:", persona.esMayorDeEdad())
