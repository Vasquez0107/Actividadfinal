def Total_NaC ():
    nombredelaprendiz = input("Ingrese el nombre del aprendiz: ")
    asignatura = input("Ingrese la asignatura: ")
    calificacion = float(input("Ingrese la calificación final (1-10): "))

    if 1 <= calificacion <= 10:
        if calificacion >= 7:
            print(f"{nombredelaprendiz} ha aprobado en la asignatura {asignatura} con una calificación de {calificacion}. APROBADO")
        else:
            print(f"{nombredelaprendiz} ha reprobado enla asignatura {asignatura} con una calificación de {calificacion}. REPROBADO.")
    else:
        print("La calificación ingresada no es válida. Debe estar entre 1 y 10")
Total_NaC()