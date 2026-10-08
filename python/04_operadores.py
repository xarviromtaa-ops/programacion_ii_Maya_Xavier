#operadores
"""

operadores aritméticos
- + (suma)
- - (resta)
- * (multiplicación)
- / (división)       
- % (módulo)
- ** (potencia)
"""
valor1 = 10
valor2 = 3
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
modulo = valor1 % valor2
potencia = valor1 ** valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)

print("tabla de multiplicar del 5:")
multiplicador = 5
print(multiplicador, "x 1 =", multiplicador * 1)
print(multiplicador, "x 2 =", multiplicador * 2)
print(multiplicador, "x 3 =", multiplicador * 3)
print(multiplicador, "x 4 =", multiplicador * 4)
print(multiplicador, "x 5 =", multiplicador * 5)
print(multiplicador, "x 6 =", multiplicador * 6)
print(multiplicador, "x 7 =", multiplicador * 7)
print(multiplicador, "x 8 =", multiplicador * 8)
print(multiplicador, "x 9 =", multiplicador * 9)
print(multiplicador, "x 10 =", multiplicador * 10)

print("Área de un triángulo con base 5 y altura 10:", 0.5 * 5 * 10)
# operadores de comparación

"""
- == (igual)
- != (diferente)
- > (mayor)
- < (menor)
- >= (mayor o igual)
- <= (menor o igual)
"""

velocidad_anakin = 950
velocidad_sebulba = 900

print("¿Anakin es más rápido que Sebulba?", velocidad_anakin > velocidad_sebulba)
print("¿Anakin es más lento que Sebulba?", velocidad_anakin < velocidad_sebulba)
print("¿Anakin es igual a Sebulba?", velocidad_anakin == velocidad_sebulba)
print("¿Anakin es diferente a Sebulba?", velocidad_anakin != velocidad_sebulba)
print("¿Anakin es mayor o igual a Sebulba?", velocidad_anakin >= velocidad_sebulba)
print("¿Anakin es menor o igual a Sebulba?", velocidad_anakin <= velocidad_sebulba)


resultado = velocidad_anakin > velocidad_sebulba
print("Resultado de la comparación:", resultado)
print("Tipo de resultado:", type(resultado))


#operadores lógicos
"""
- and (y)
- or (o)
- not (no)
"""

motores_funcionando = True
escudos_activados = False
combustible = 80 

print("todos los sistemas en funcionamiento:", motores_funcionando and escudos_activados and combustible > 0)
print("algunos sistemas en funcionamiento:", motores_funcionando or escudos_activados or combustible > 0)
print("¿los sistemas no están en funcionamiento?", not (motores_funcionando and escudos_activados and combustible > 0))

cantidad_motores = 2
cantidad_alas = 4
combustible = 80

print("¿La nave tiene al menos 2 motores y 4 alas?")
print(cantidad_motores >= 2 and cantidad_alas >= 4 and combustible >= 50)
print("¿La nave tiene al menos 2 motores o 4 alas?")
print(cantidad_motores >= 2 or cantidad_alas >= 4 and combustible >= 50)
print("¿La nave no tiene al menos 2 motores y 4 alas?")
print(not cantidad_motores >= 2 and cantidad_alas >= 4 and combustible >= 50)
 
#operadores de asignación
"""
- = (asignación)
- += (suma y asignación)
- -= (resta y asignación)
- *= (multiplicación y asignación)
- /= (división y asignación)
- %= (módulo y asignación)
- **= (potencia y asignación)
"""

velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad después de acelerar:", velocidad)
velocidad -= 30
print("Velocidad después de frenar:", velocidad)
multiplicador = 2
velocidad *= multiplicador
print("Velocidad después de multiplicar:", velocidad)
divisor = 4
velocidad /= divisor
print("Velocidad después de dividir:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad después de aplicar módulo:", velocidad)
velocidad **= 2
print("Velocidad después de elevar al cuadrado:", velocidad)


#precedencia de operadores
"""
1. ()
2. ** (potencia)
3. *, /, %(multiplicación, división, módulo)
4. +, - (suma, resta)
"""

resultado_1 = 10 + 5 * 2
print("resultado_1:", resultado_1)
resultado_2 = (10 + 5) * 2
print("resultado_2:", resultado_2)


          
