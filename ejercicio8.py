precio = float(input("introduce el precio del producto en dolares con dos decimales: "))

dolar = int(precio)
centimos = int((precio - dolar) * 100)  

print(f"El precio es {dolar} dolares y {centimos} centavos.")
