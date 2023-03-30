# Pedimos al usuario que ingrese el costo del artículo y el dinero entregado por el cliente
costo = float(input("Ingrese el costo del artículo: "))
dinero_entregado = float(input("Ingrese el dinero entregado por el cliente: "))

# Si el dinero entregado es mayor que el costo del artículo, calculamos el cambio y lo imprimimos
if dinero_entregado > costo:
    cambio = dinero_entregado - costo
    print("El cambio que se debe entregar es:", cambio)

# Si el dinero entregado es igual al costo del artículo, imprimimos un mensaje indicando que no hay cambio
elif dinero_entregado == costo:
    print("El cliente ha pagado exactamente el valor del artículo. No se requiere cambio.")

# Si el dinero entregado es menor que el costo del artículo, calculamos la cantidad de dinero faltante y lo imprimimos
else:
    faltante = costo - dinero_entregado
    print("Falta por pagar:", faltante)
