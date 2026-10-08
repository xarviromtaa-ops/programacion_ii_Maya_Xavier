#string cadenas de caracteres
jedi = "Qui-Gon Jinn"
aprendiz = "Obi-Wan Kenobi"
droide = "R2-D2"
planeta = "Naboo"
code = "327"

print("El Jedi es: " + jedi)
print("el jedi", type(jedi))
print("El aprendiz es: " + aprendiz)
print("el aprendiz", type(aprendiz))
print("El droide es: " + droide)
print("el droide", type(droide))       
print("El planeta es: " + planeta)
print("el planeta", type(planeta))
print("El codigo es: " + code)
print("el codigo", type(code))

longitud_jedi = len(jedi)
print("la longitud del nombre del jedi es:" + str(longitud_jedi))
longitud_aprendiz = len(aprendiz)
print("la longitud del nombre del aprendiz es:" + str(longitud_aprendiz))


mensaje = "La federación de comercio ha establecido un bloqueo en Naboo"
print("El mensaje es: " + mensaje)
mensaje_mayusculas = mensaje.upper()
print("El mensaje en mayúsculas es: " + mensaje_mayusculas)
mensaje_minusculas = mensaje.lower()
print("El mensaje en minúsculas es: " + mensaje_minusculas)

comunicado = "Los jedis son enviados a Naboo"
print("El comunicado es: " + comunicado)
nuevo_comunicado = comunicado.replace("Naboo", "Tatooine")
print("El comunicado reemplazado es: " + nuevo_comunicado)

planetas = "Naboo, Tatooine, Coruscant, Alderaan"
planetas_lista = planetas.split(", ")
print(planetas_lista)
print("La lista de planetas es: " + str(planetas_lista))
print("El primer planeta es: " + planetas_lista[0])

droide = "R2-D2"
print("El droide es: " + droide)
print("El primer caracter del droide es: " + droide[0])
print("El segundo caracter del droide es: " + droide[1])
print("El tercer caracter del droide es: " + droide[2])
print("El cuarto caracter del droide es: " + droide[3])
print("El quinto caracter del droide es: " + droide[4])
print("El sexto caracter del droide es: " + droide[-1])

planeta = " Naboo "
print("El planeta es: " + planeta)
print("El planeta sin espacios es: " + planeta.strip())
