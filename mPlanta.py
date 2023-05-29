import csv
from clasePlanta import EmpleadoPlanta

class LectorPlanta:
    @staticmethod
    def leer_archivo():
        empleados_planta = []

        with open("planta.csv", "r") as file:
            reader = csv.reader(file)
            cabecera=True
            for row in reader:
                if cabecera:
                    cabecera=False
                else:
                    dni, nombre, direccion, telefono, sueldo_basico, antiguedad = row
                    empleado = EmpleadoPlanta(int(dni), nombre, direccion, telefono, float(sueldo_basico), int(antiguedad))
                    empleados_planta.append(empleado)
        return empleados_planta
