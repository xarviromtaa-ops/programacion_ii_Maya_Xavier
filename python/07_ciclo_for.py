#ciclo for
naves = [
    "Caza n-1",
    "Nave real de Naboo",
    "transporte"
    
]
for nave in naves:
    print("inspecionando", nave)
    
print("inspeccion realizada")

rondas = range(1,6)

print("tipo de rondas: ", type(rondas))
for ronda in rondas:
    print(f"ronda de vigilancia: {ronda}")
    print(f"tipo de dato ronda: {type(ronda)}")
    
droides = range(1,17,2)

print("tipo de droides: ", type(droides))
for droide in droides:
    print(f"reparar : droide B1 {droide}")
    print(f"tipo de dato droide: {type(droide)}")
    
planetas= [
    "Naboo",
    "Tatooine",
    "Coruscant",
]

recorrido = enumerate(planetas, start=1)

for posicio, planeta in recorrido:
    print(f"planeta {posicio}: {planeta}")
    print(f"tipos de datos {type(posicio)}: {type(planeta)}")
    
paises = [
    "ecuador",
    "venezuela",
    "chile",
    "brasil",
    "ESTADOS UNIDOS",
]
for pais in paises:
    if pais == "chile":
        continue
    if pais == "brasil":
        break
    print(f"pais visitado: {pais}")