class Empleado:
    __dni: int
    __nombre: str
    __direccion: str
    __telefono: str
    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getTelefono(self):
        return self.__telefono

    def calcular_sueldo(self):
        pass

    def __str__(self):
        return f"Apellido y Nombre: {self.__nombre}\nDireccion: {self.__direccion}\nDNI: {self.__dni}\n"