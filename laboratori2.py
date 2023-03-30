numeros = []
for i in range(3):
    num = int(input("Ingrese un número entero: "))
    numeros.append(num)

numeros.sort()
maximo = numeros[2]
medio = numeros[1]
minimo = numeros[0]

print(f"El número {maximo} es el número más grande de los tres")
print(f"El número {minimo} es el número más pequeño de los tres")
print(f"El número {medio} es el número de en medio de los tres")

    



 
