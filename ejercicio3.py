print("Ingresa 3 números enteros que sean mayores de 0 y que formen los lados de un triángulo")
x=abs(int(input("Ingresa el valor del lado X: ")))
y=abs(int(input("Ingresa el valor del lado Y: ")))
z=abs(int(input("Ingresa el valor del lado Z: ")))

if(x*y*z==0):
    print("Que no uses ningún 0 >:(")
else:
#verificamos que los lados si sean de un triángulo, en caso de que si, lo clasificamos
    if(x+y>z and x+z>y and y+z>x):
        if(x==z and y==z):
            print("Es un triángulo escaleno")
        elif(x==z or x==z or y==z):
            print("Es un triángulo isóceles")
        else:
            print("Es un triángulo escaleno")
    else:
        print("No son lados que hagan un triángulo perro")
        