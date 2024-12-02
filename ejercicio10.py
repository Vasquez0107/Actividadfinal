def Total_Ds ():
    precio = float(input("Ingrese el valor de su compra: $"))

    if precio > 20000:
        descuento = precio * 0.20  
        precio_final = precio - descuento
        print(f"Se ha aplicado un descuento del 20%. El valor final a pagar es: ${precio_final:.2f}")
    else:
        print(f"El valor final a pagar es: ${precio:.2f}")
Total_Ds()

