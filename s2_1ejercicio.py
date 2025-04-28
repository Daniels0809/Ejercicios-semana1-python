#Estructuras Condicionales Ejercicio 1: 
# Clasificador de números. Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero.

numero = int(input("Ingresa un número para determinar si es positivo, negativo o cero: "))
def queEs(n):
        if n<0:
            input(f"El número {n} es negativo.")
        elif n>0:
            input(f"El número {n} es positivo.")
        else:
            input("Es cero.")
   
print(queEs(numero))