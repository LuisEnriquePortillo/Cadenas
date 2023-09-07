print("Debes poner tu nombre y luego un numero y tu nombre se repetira esa cantidad de veces, Intentalo!!!")
nombre_usuario = input("Escibre tu nombre: ")

numero = int(input("introduce un número entero: "))

for _ in range(numero):
    print(nombre_usuario)
