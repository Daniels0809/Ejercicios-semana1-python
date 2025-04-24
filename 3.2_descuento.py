#Dado un precio y un porcentaje de descuento, muestra el valor final a pagar.

precio = float(input("Ingresa precio: "))
descuento = float(input("Ingresa valor de descuento sin el porcentaje: "))

def valorFinal(p, d):
    desc = p*(d/100)
    final = p-desc
    return final
print("El valor final a pagar es: ", valorFinal(precio, descuento), "mil pesos")