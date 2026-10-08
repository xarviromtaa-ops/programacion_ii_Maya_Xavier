#condicional if
#if

combustible = 10
if combustible >= 10:
    print("puedes despegar")
    
#condicional if-else
creditos = int(input("ingresa la cantidad de creditos: "))
precio_repuesto = int(input("ingresa el precio del repuesto: "))
if creditos >= precio_repuesto:
    print("puedes comprar el repuesto")
else:
    print("no tienes suficientes creditos para comprar el repuesto")

#if anidado

if creditos >= precio_repuesto:
    print("puedes comprar el repuesto")
    if creditos > precio_repuesto:
        print("te sobraran creditos")
    else:
        print("te quedas justo con los creditos necesarios")
else:
    print("no tienes suficientes creditos para comprar el repuesto")
    
#condicional if-elif-else
if creditos > precio_repuesto:
    print("puedes comprar el repuesto y te sobraran creditos")
elif creditos == precio_repuesto:
    print("puedes comprar el repuesto y te quedas justo con los creditos necesarios")
else:
    print("no tienes suficientes creditos para comprar el repuesto")
    
    
tipo_repuesto = input("ingresa el tipo de repuesto (motor, ala, escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_repuesto and tipo_repuesto == "escudo":
    print("puedes comprar el respuesto y te sobraran creditos")
elif tipo_repuesto == "ala" and creditos >= precio_repuesto:
    print("puedes comprar el respuesto y te sobraran creditos")
elif tipo_repuesto == "escudo" and creditos >= precio_repuesto:
    print("puedes comprar el respuesto y te sobraran creditos")
else:
    print("tipo de respuesto no valido")
    