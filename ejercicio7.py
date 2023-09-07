correo = input("Por favor, introduce tu correo electrónico: ")

nombre_usuario, dominio = correo.split('@')

nuevo_correo = nombre_usuario + '@ceu.es'

print("Nuevo correo electrónico papá:", nuevo_correo)
