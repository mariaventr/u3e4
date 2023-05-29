import numpy as np
from claseContratado import EmpleadoContratado
from claseExterno import EmpleadoExterno

class arregloEmpleados:
    def __init__(self, size):
        self.__empleados = np.empty(size, dtype=object)
        self.__size = size
        self.__cont = 0
    
    def agregar_empleado(self, empleado):
        if self.__cont < self.__size:
            self.__empleados[self.__cont] = empleado
            self.__cont += 1
        else:
            print("Error: No hay suficiente espacio en la colección.")

    def opcion1(self, dni, horas):
     i = 0
     band = False
     while i < len(self.__empleados) and not band:
        if self.__empleados[i] is not None and self.__empleados[i].getDni() == dni:
            if isinstance(self.__empleados[i], EmpleadoContratado):
                band = True
                self.__empleados[i].horasTrabajadas(horas)
                print(f"Horas actualizadas: {self.__empleados[i].getHoras()}")
                print("Se registraron las horas trabajadas correctamente.")
            else:
                band= True
                print("Error: Solos los empleados contratados pueden incrementar sus horas")
        else:
            i+=1

     if i >= len(self.__empleados):
        print("Error: No se encontró un empleado con el DNI proporcionado.")

    def opcion2(self, tarea):
     fecha_actual=input("Ingresar fecha actual (en formato año-mes-dia): ")
     i = 0
     total=0
     band = False
     while i < len(self.__empleados):
        if isinstance(self.__empleados[i], EmpleadoExterno) and self.__empleados[i].getTarea() == tarea and self.__empleados[i].getFechaFin() > fecha_actual:
            total+=self.__empleados[i].getMonto() 
            i+=1
            band=True
        else:
            i+=1
        
     if band==False:
         print("Error: No se encontró la tarea ingresada.")
     else:
         print(f"Monto Total de la tarea {tarea}: {total}") 

    
    def opcion3(self):
        i=0
        while i < len(self.__empleados):
            if self.__empleados[i] is not None and self.__empleados[i].calcular_sueldo() < 150000 :
                print(self.__empleados[i])
                print(f"Sueldo: {self.__empleados[i].calcular_sueldo()}")
                i+=1
            else:
                i+=1
    
    def opcion4(self):
        for empleado in self.__empleados:
            if empleado is not None:
                print(f"Apellido y Nombre: {empleado.getNombre()}\nTelefono: {empleado.getTelefono()}\nSueldo: {empleado.calcular_sueldo()}\n")
