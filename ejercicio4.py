def Calcular_años():
    capital_inicial = float(input("Introduce la inversion: "))


    interes_anual = float(input("Introduce el interés anual: "))

    año = (1)

    interes_decimal = interes_anual / 100

    capital_final = capital_inicial * (1 + interes_decimal) ** año

    print(f"El capital final después de {año} años será: {capital_final} unidades monetarias.")
Calcular_años()