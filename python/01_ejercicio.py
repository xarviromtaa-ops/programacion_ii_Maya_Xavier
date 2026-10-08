print("bienvenido a entregas")

peso = int(input("ingresa el peso del paquete en kg: "))
print ("zonas: 1. america; 2. europa; 3. resto del mundo")
zona_destino = int(input("ingresa la zona de destino (1, 2 o 3): "))
costo_envio = 0
if zona_destino == 1:
    costo_envio = peso*5.0
elif zona_destino == 2:
    costo_envio = peso*7.5
elif zona_destino == 3:
    costo_envio = peso*10
else:
    print("zona de destino no valida")

print("el costo de envio es:", costo_envio)

    
