import math
 
 
def calcular_raices(a, b, c):
    if a == 0:
        raise ValueError("El valor de 'a' no puede ser 0.")
 
    discriminante = b ** 2 - 4 * a * c
 
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return x1, x2
 
    elif discriminante == 0:
        x = -b / (2 * a)
        return x, x
 
    else:
        return "La ecuación no tiene raíces reales"
 
 
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
 
resultado = calcular_raices(a, b, c)
 
print("Resultado:", resultado)