#Calcula el área de un rectángulo a partir de base y altura ingresadas por el usuario.
print("Vamos a calcular el area de un rectnagulo, ingresa los siguientes valores: ")
base = float(input("Ingrese el valor de la base: "))
altura = float(input("Ingresa el valor de la altura: "))

def areaRectangulo(b, a):
    area = b*a
    return area

print(areaRectangulo(base, altura))

