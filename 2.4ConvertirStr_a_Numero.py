#Escribe una función que reciba un string y devuelva True si puede convertirse a número y False si no.

#No es necesario crear una variable adentro de la función
def esNumero(a):
    try:
        float(a)
        print("Exitoso: ")
        return(True)

    except:
        print("Imposible: ")
        return(False)
    

print(esNumero(input(f"Ingrese algo para verificar si es posible convertirlo a numero: ")))
   