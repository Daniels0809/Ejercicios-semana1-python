#Escribe una fórmula que use al menos tres operadores diferentes y muestre el resultado.
print("Ingresa dos valores para sumarlos, multiplicarlos y sabes la potencia entre el primer y segundo número: ")

a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))

def suma(a, b):
    sum = a+b
    return sum

def mult(a,b):
    mul = a*b
    return mul

def potencia (a,b):
    p= a**b, b**a
    return p

print(f"Los valores de suma son: {suma(a,b)} Los valores de multiplicacion son: {mult(a,b)} y los valores de potencia son: {potencia(a,b)}")
