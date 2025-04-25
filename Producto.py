#Pedimos que ingresen la informacion requerida

producto = str(input("Ingrese el nombre del producto: "))
#Para la entrada de datos, se ingresa a un bucle para verificar que si ingresen los datos correspondientes
while True:
    #Utilizamos try-except para la verificacion de datos
    try:
        punitario = float(input("Ingrese el precio por unidad: "))
        while punitario<0: #Bucle while para entrada de precios positivos
            print("¡Error! Ingresa un valor positivo: ")
            punitario = float(input("Ingrese el precio por unidad: ")) #Se pide de nuevo que ingrese el dato correspondiente
        break #Sale del bucle
    except ValueError:    
            print("¡Error! Debes ingresar un número.")
while True:
    try: #Utilizamos try-except para la verificacion de datos
        cantidad = int(input("Ingrese la cantidad de producto: "))
        while cantidad<0: #Bucle while para verificar que sean valores positivos
             print("¡Error! Ingresa un valor positivo: ")
             cantidad= int(input("Ingrese la cantidad del producto: "))
        break #Sale del bucle
    except ValueError:
        print("¡Error! Debes ingresar un número.")
while True:
    try: #Utilizamos try-except para la verificacion de datos
        porcentaje = float(input("Ingrese el valor de descuento: "))
        while not (0<=porcentaje<=100): #Bucle while para verificar que el porcentaje de descuento este entre 0 y 100
            print("¡Error! Ingresa un valor entre 0 y 100 para el descuento: ")
            porcentaje = float(input("Ingresa el valor de descuento: "))
        break #Sale del bucle
    except ValueError:
            print("¡Error! Debes ingresar un número.")
#Imprimimos y realizamos las operaciones requeridas en el mismo print para ahorrar espacio en funciones
print(f"Tu producto: {producto} \nTiene un costo de: {punitario*cantidad} mil pesos \nAplicando el {porcentaje}% de descuento \nTendria un valor de {(punitario*cantidad)*(porcentaje/100)} mil pesos en total")


