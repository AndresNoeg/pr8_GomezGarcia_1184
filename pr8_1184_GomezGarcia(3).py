# Clase Persona
class Persona:
    def __init__(self, nombre, edad, dni):
        # Inicializamos los atributos de la persona
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def mostrar(self):
        # Muestra los detalles de la persona
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

# Clase Cuenta
class Cuenta:
    def __init__(self, titular, cantidad=0):
        # Inicializamos la cuenta con un titular y una cantidad de dinero (por defecto 0)
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar(self):
        # Muestra los detalles de la cuenta
        return f"Cuenta - Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad}"

# Clase CuentaJoven (hereda de Cuenta)
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        # Inicializamos la cuenta joven con un titular, una cantidad y una bonificación
        super().__init__(titular, cantidad)  # Llama al constructor de la clase base (Cuenta)
        self.bonificacion = bonificacion
    
    def mostrar(self):
        # Muestra los detalles de la cuenta joven, incluyendo la bonificación
        return f"Cuenta Joven - Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad}, Bonificación: {self.bonificacion}%"

# Aquí comienza el programa
if __name__ == "__main__":
    # Crear una persona (titular)
    persona = Persona("Noé Gómez", 20, "12345678A")
    
    # Crear una cuenta joven con bonificación
    cuenta_joven = CuentaJoven(persona, 1000, 5)
    
    # Mostrar los detalles de la cuenta joven
    print(cuenta_joven.mostrar())


  
