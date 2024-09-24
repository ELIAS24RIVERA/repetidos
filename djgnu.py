def aparesca(lista, numero):
    if lista.count(numero)==2:
        return True
    else:
        return False
lista = [1, 2, 3, 4, 7, 5, 6, 7]
numero= 7
print(f"el numero 7 repiter dos veces?:",aparesca(lista, numero))
numero = 3
print(f"el numero 3 repite dos veces?:", aparesca(lista, numero))