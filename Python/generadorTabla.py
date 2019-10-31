import matplotlib.pyplot as plot
import json
from CaesarCypher import normalizeString


quijote = open("Quijote.txt", "r", encoding="UTF-8")

totales = {"k": 0}
data = {}
contador = 0

for linea in quijote.readlines():
    for caracter in normalizeString(linea):
        if caracter.isalpha():
            contador+=1
            try:
                totales[caracter] = totales[caracter] + 1
            except KeyError:
                totales[caracter] = 1
data["totales"] = totales

# Porcentuales
porcentajes = {"k": 0.0}
for i in totales:
    porcentajes[i] = totales[i]/contador
data["porcentajes"] = porcentajes

archivoVolcado = open("output.json", "w", encoding="UTF-8")
archivoVolcado.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
