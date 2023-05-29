from claseEmpleado import Empleado

class EmpleadoExterno(Empleado):
    __tarea: str
    __fecha_inicio: str
    __fecha_fin: str
    __monto_viatico: float
    __costo_obra: float
    __monto_seguro_vida: float
    def __init__(self, dni, nombre, direccion, telefono, tarea, fecha_inicio, fecha_fin, monto_viatico, costo_obra, monto_seguro_vida):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__monto_viatico = monto_viatico
        self.__costo_obra = costo_obra
        self.__monto_seguro_vida = monto_seguro_vida
    
    def calcular_sueldo(self):
        sueldo = self.__costo_obra - self.__monto_viatico - self.__monto_seguro_vida
        return sueldo
    
    def getTarea(self):
        return self.__tarea
    
    def getFechaFin(self):
        return self.__fecha_fin
    
    def getMonto(self):
        return self.__costo_obra
