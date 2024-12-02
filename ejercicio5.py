def total_nAprendiz ():

    total_notas = 0
    cantidad_notas = int(input("¿Cuántas notas va a ingresar el profesor? "))

    for i in range(cantidad_notas):
        while True:
            nota = float(input(f"Ingrese la nota {i + 1}: "))
            if 0 <= nota <= 5:
                total_notas += nota
                break
            else:
                print("Nota fuera de rango, por favor ingrese una nota entre 0 y 5")

    promedio = total_notas / cantidad_notas

    if promedio >= 4.5:
        print(f"Promedio: {promedio:.2f}. ¡Aprobado!")
    else:
        print(f"Promedio: {promedio:.2f}. No aprobado.")
total_nAprendiz()