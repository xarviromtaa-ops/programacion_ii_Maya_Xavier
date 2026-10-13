##Funciones
#funciones sin parametros
def activar_sistema():
    print("==sistema de naboo==")
    print("Sistema de control activado")
    
activar_sistema()

#Funciones con parametro

def saludar_jedi(nombre):
    print(f"Que la fuerza te acompañe: {nombre}")
    
saludar_jedi("Qui-gon jim")
saludar_jedi("Obi-wan Kenobi")

def mostrar_nave(nombre, combustible):
    print(f"nave: {nombre}")
    print(f"cabtudad combustible: {combustible}")
    
    mostrar_nave("caza N-1", 80)
    
#funciones que devuelven dato o informacion

#return

def calcular_combustible(inicial, consumo):
    restante = inicial - consumo
    return restante

resultado = calcular_combustible(100,25)
print(f"combustible: {resultado}")