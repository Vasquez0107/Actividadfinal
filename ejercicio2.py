def total_impares():
    inicio = int(input("Introduce el valor de inicio: "))
    fin = int(input("Introduce el valor final: "))

    for i in range(inicio, fin + 1):
        if i % 2 != 0: 
            print(i)
total_impares()
