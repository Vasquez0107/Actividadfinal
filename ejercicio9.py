def Total_NtT ():
    NombreAprendiz = input("Infresa nombre: ")
    Asignatura = input("Igrese su asignatura: ")

    Nota1 = float(input("ingrese su nota N1: "))
    Nota2 =  float(input("ingrese su nota N2: "))
    Nota3 =  float(input("ingrese su nota N3: "))

    CalificacionF = (Nota1 * 0.30) + (Nota2 * 0.30) + (Nota3 * 0.40)

    print(f"\n{NombreAprendiz} ha obtenido una Calificación final de {CalificacionF:.2f} en la asignatura {Asignatura}.")

    if CalificacionF >= 4.0:
        print (" Has Aprobado ")
    else:
        print ("Desaprovado")
Total_NtT()
    