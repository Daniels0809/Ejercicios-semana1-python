#Ejercicio 2: Aprobado o reprobado 
# Crea un programa que reciba la calificación de un estudiante (0 a 100) 
# e indique si está aprobado (60 o más) o reprobado (menos de 60).

cali = int(input("Ingresa tu calificación de 0 a 100: "))

if cali >= 60:

    print("¡Felicitaciones aprobasteeee!")

elif cali <60:
    print("Que lastima reprobaste, sera en la proxima.")