import datetime as dt
fecha_ingreso = input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
fecha_ingreso = dt.datetime.strptime(fecha_ingreso, "%d/%m/%Y")
fecha_actual = dt.datetime.now()


print(fecha_actual)
print(fecha_ingreso)
