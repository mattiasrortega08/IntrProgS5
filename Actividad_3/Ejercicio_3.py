capital_inicial = float(input("Ingrese el capital inicial: "))
tiempo = float(input("Ingrese la cantidad de años: "))
tasa_interes = float(input("Ingrese la tasa de interés: "))

tasa_interes_dec = tasa_interes / 100
monto_final = capital_inicial * (1 + tasa_interes_dec) ** tiempo
interes_ganado = monto_final - capital_inicial
2
print(f"Capital inicial: {capital_inicial:>6.2f}")
print(f"Tiempo: {tiempo:>15.2f}")
print(f"Tasa de interés: {tasa_interes:>6.2f}")
print(f"Monto final: {monto_final:>13.2f}")
print(f"Interés ganado: {interes_ganado:>10.2f}")