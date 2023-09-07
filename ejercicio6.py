frase = input("introduce una frase: ")

vocal = input("introduce una vocal: ")

if len(vocal) == 1 and vocal.lower() in 'aeiou':
    vocal_mayuscula = vocal.upper()

    frase_con_vocal_mayuscula = frase.replace(vocal, vocal_mayuscula)

    print("Frase pero con la vocal en mayúscula:", frase_con_vocal_mayuscula)
else:
    print("Por favor, introduce una única vocal (a, e, i, o, u) en minúscula no es tan dificil tan dura fue la primaria? algo tan simple no pudiste hacer??????????!!!!!.")
