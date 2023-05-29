from claseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    __valor_hora = 100
    __fecha_inicio: str
    __fecha_fin_: str
    __horas_trabajadas: int

    def __init__(self, dni, nombre, direccion, telefono, fecha_inicio, fecha_fin, horas_trabajadas):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__horas_trabajadas = horas_trabajadas
    
    def calcular_sueldo(self):
        sueldo = self.__horas_trabajadas * self.__valor_hora
        return sueldo
    
    def horasTrabajadas(self, horas):
        self.__horas_trabajadas += horas

    def getHoras(self):
        return self.__horas_trabajadas
