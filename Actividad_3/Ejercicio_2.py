cantidad_inicial_inventario = int(input("Ingrese la cantidad inicial de inventario: "))
cantidad_productos_recibidos = int(input("Ingrese la cantidad de productos recibidos: "))
cantidad_inicial_vendido = int(input("Ingrese la cantidad inicial vendida: "))

suma = cantidad_inicial_inventario + cantidad_productos_recibidos
inventario_actual = suma - cantidad_inicial_vendido

print(f"Cantidad inicial de inventario: {cantidad_inicial_inventario:>3}")
print(f"Cantidad de productos recibidos: {cantidad_productos_recibidos:>3}")
print(f"Cantidad de productos vendidos: {cantidad_inicial_vendido:>3}")

print(f"Inventario actual: {inventario_actual:>3}")
print(f"cantidad de prodcutos en inventario actual: {inventario_actual:>3}")    