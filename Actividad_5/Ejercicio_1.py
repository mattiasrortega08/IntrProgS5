calificacion = float(input("Ingrese la calificación: "))

if calificacion >= 0 and calificacion <= 10:
    if calificacion >= 9 and calificacion <= 10:
        print("A")
    elif calificacion >= 7 and calificacion < 9:
        print("B")
    elif calificacion >= 5 and calificacion < 7:
        print("C")
    elif calificacion >= 3 and calificacion < 5:
        print("D")
    else:
        print("F")
else:
    print("Calificación fuera de rango")