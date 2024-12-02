def Total_Dolares ():
    TazaDC = int(input("ingrese la taza de cambios"))

    while True:
        
        dolares = float(input("ingrese dolares: "))

        pesos = dolares * TazaDC

        print(f"{dolares} dolares equivalen a {pesos:.2f} pesos: ")

        continuar = input("Deseas realizar otra conversacion? (si/no): ")

        if continuar != 'si':
            print("Finalizado")
            break
Total_Dolares()