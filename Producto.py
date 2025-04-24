#Pedimos que ingresen la informacion requerida

producto = str(input("Ingrese el nombre del producto: "))

#Ingresamos lo datos
while True:
    try:
        punitario = float(input("Ingrese el precio por unidad: "))
        break
    except ValueError:
            
            print("¡Error! Debes ingresar un número.")
try:
    cantidad = int(input("Ingrese la cantidad de producto: "))
except ValueError:
    print("¡Error! Debes ingresar un número.")

try:
        porcentaje = float(input("Ingrese el valor de descuento: "))
except ValueError:
        print("¡Error! Debes ingresar un número.")


