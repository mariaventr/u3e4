import csv
from claseContratado import EmpleadoContratado

class LectorContratados:
    @staticmethod
    def leer_archivo():
        empleados_contratados = []

        with open("contratados.csv", "r") as file:
            reader = csv.reader(file)
            cabecera=True
            for row in reader:
                if cabecera:
                    cabecera=False
                else:
                    dni, nombre, direccion, telefono, fecha_inicio, fecha_fin, horas_trabajadas = row
                    empleado = EmpleadoContratado(int(dni), nombre, direccion, telefono, fecha_inicio, fecha_fin, int(horas_trabajadas))
                    empleados_contratados.append(empleado)
        return empleados_contratados

