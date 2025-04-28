num = float(input("Ingresa un numero para ver su doble y triple: "))
print("Elegiste el numero",num," y el doble es: ",num*2," ahora el triple es: ",num*3)

#Bucles Ejercicio 3:
#Escribe un programa que muestre la tabla de multiplicar de un número ingresado por el usuario (del 1 al 10) usando un bucle for.
while True:
    try:
        numero = int(input("Ingresa un numero para saber su tabla del 1 al 10: "))
        break
    except ValueError:
        print("Error!  Ingresa un número.")

def mult(numero):
    for i in range(1,11):
        result = numero * i
        print(f"La multiplicacion del numero {numero} es:")
        print(f"{numero} x {i}: {result}")
        
print(mult(numero))
