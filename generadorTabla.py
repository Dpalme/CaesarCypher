import matplotlib.pyplot as plot
import json

quijote = open("Quijote.txt", "r", encoding="UTF-8")
totales = {}

data = {}
contador = 0

for linea in quijote.readlines():
    for caracter in linea.lower():
        contador+=1
        try:
            totales[caracter] = totales[caracter] + 1
        except KeyError:
            totales[caracter] = 1

data["totales"] = totales

# Porcentuales
porcentajes = {}
for i in totales:
    porcentajes[i] = totales[i]/contador
data["porcentajes"] = porcentajes

archivoVolcado = open("output.json", "w", encoding="UTF-8")
archivoVolcado.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
