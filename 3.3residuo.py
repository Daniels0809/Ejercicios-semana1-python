#Calcula el residuo de dividir dos números dados por el usuario.
print("Calcular el residuo de dos numeros")
n1 = int(input("Ingrese el primer valor: "))
n2 = int(input("Ingresa el segundo valor: "))

def calcularResiduo (n1, n2):
    residuo = n1 % n2
    return residuo

print("El residuo de los numeros,",n1,",",n2, "es: ",calcularResiduo(n1,n2))