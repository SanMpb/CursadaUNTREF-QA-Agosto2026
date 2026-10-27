def es_primo(numero):
    if numero < 2:
        return False
 
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
 
    return True
 
 
numero = int(input("Ingrese un número: "))
 
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")