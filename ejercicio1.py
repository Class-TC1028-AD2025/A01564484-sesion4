numero=int(input("dame un número: "))

if(numero>=0):
    print("Es positivo")
    if(numero%2==0):
        print("y par")
    else:
        print("e impar")
else:
    print("es negativo")
    if(numero%2==0):
        print("y par")
    else:
        print("e impar")