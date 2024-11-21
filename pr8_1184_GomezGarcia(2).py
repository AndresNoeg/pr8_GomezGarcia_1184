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



