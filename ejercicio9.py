fecha_nacimiento = input("Por favor, introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

comp = fecha_nacimiento.split('/')

dia = comp[0].rjust(2, '0')  
mes = comp[1].rjust(2, '0')  
año = comp[2]

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {año}")
