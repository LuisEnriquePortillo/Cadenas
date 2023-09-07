import re

telefono = input("Por favor, introduce un número de teléfono con el formato +34-XXXXXXXXX-XX: ")

patron = r'\+34-(\d+)-\d{2}'

resultado = re.search(patron, telefono)

if resultado:
    numero_telefono = resultado.group(1)
    print("Número de teléfono sin prefijo y extensión:", numero_telefono)
else:
    print("El formato del número de teléfono no es válido pongalo bien JAJA.")
