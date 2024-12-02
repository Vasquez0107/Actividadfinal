def Total_Ed():
    edad = int(input("Ingrese su edad: "))
    sexo = input("Ingrese su sexo: ").lower()

    if sexo == "m":
        if edad >= 63:
            print("¡Puede jubilarse!")
        else:
            print("Aún no puede jubilarse.")
    elif sexo == "f":
        if edad > 54:
            print("¡Puede jubilarse!")
        else:
            print("Aún no puede jubilarse.")
    else:
        print("Sexo no válido. Ingrese 'Hombre' o 'Mujer'.")
Total_Ed()