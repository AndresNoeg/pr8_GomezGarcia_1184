# pr8_GomezGarcia_1184

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

![image](https://github.com/user-attachments/assets/8cae5e56-500f-47b0-bd53-1d91b59c2b6e)

![image](https://github.com/user-attachments/assets/eb29c14e-c945-482f-bd15-6c34ef16d9b7)



class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self._titular = titular  # Variable que guarda el titular de la cuenta
        self._cantidad = cantidad  # Variable que guarda el saldo de la cuenta

  
    def get_titular(self):
        return self._titular


    def set_titular(self, titular):
        self._titular = titular


    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        # Si intentamos modificar la cantidad no se hace nada
        print("No se puede modificar la cantidad directamente. Usa los métodos ingresar o retirar.")

    # Muestra los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self._titular}")  
        print(f"Cantidad: {self._cantidad}")  

    # Ingresa dinero en la cuenta
    def ingresar(self, cantidad):
        if cantidad > 0:  # Comprobamos que la cantidad sea positiva
            self._cantidad += cantidad  # Sumamos la cantidad al saldo de la cuenta
        else:
            print("La cantidad a ingresar debe ser positiva.") 

    # Retira dinero de la cuenta
    def retirar(self, cantidad):
        if cantidad > 0:  # Comprueba que la cantidad sea positiva
            self._cantidad -= cantidad  
        else:
            print("La cantidad a retirar debe ser positiva.")  

# Ejemplo de uso
cuenta = Cuenta("Juan Pérez", 1000.0)  
cuenta.mostrar()  # Mostramos los datos de la cuenta

cuenta.ingresar(500) 
cuenta.mostrar()  # Mostramos los datos actualizados

cuenta.retirar(200) 
cuenta.mostrar()  # Mostramos los datos actualizados

cuenta.retirar(1500) 
cuenta.mostrar()  # Mostramos los datos actualizados

![image](https://github.com/user-attachments/assets/1b486f4b-b93c-4afb-8755-a8df397e4fa6)


![image](https://github.com/user-attachments/assets/296e1bfa-d3f0-4541-9004-97862cfadb37)



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

![image](https://github.com/user-attachments/assets/45c3113b-79a8-4a9b-95b1-65e9cb9ffe1c)

![image](https://github.com/user-attachments/assets/f3a78aed-5e4c-4d54-be32-92cfb733013f)





