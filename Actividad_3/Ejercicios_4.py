litros_precio = 49.57 #Precio del litro de gasolina

distancia_km = float(input("Ingrese la distancia en km: "))
litros_consumidos = float(input("Ingrese los litros consumidos: "))

division = distancia_km / litros_consumidos

multiplicacion = litros_precio * litros_consumidos

print(f"La distancia recorrida es: {distancia_km} km")
print(f"Litros de gasolina consumidos: {litros_consumidos} L") 
print(f"El precio de la gasolina es: {litros_precio} $/L")
print(f"El rendimiento del vehiculo es: {division} km/L")  
print(f"El costo del viaje es: {multiplicacion} $")
print(f"El costo por km es: {multiplicacion / distancia_km} $/km")