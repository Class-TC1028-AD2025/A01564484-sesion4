numero=int(input("dame un número: "))

if(numero>=0 and numero%2==0):
    print("Es par positivo")
elif(numero>=0):
    print("es impar positivo")
elif(numero%2==0):
    print("Es par negativo")
else:
    print("impar negativo")