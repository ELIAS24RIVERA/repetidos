def numeros_repetidos (lista):
    vistos = set()
    repetidos = set()
    for numero in lista:
        if numero in vistos:
            repetidos.add(numero)
        else:
            vistos.add(numero)
    return list(repetidos)
entrada= input("ingrese una lista de numeros separados con espacios: ")
lista = list(map(int, entrada.split()))
print(" el numeros repetidos:", numeros_repetidos(lista))