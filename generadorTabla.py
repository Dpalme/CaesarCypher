import matplotlib.pyplot as plot

quijote = open("Quijote.txt", "r", encoding="UTF-8")
Letras = {}
contador = 0

for linea in quijote.readlines():
    for caracter in linea.lower():
        contador+=1
        try:
            Letras[caracter] = Letras[caracter] + 1
        except KeyError:
            Letras[caracter] = 1

archivoVolcado = open("output.txt", "w", encoding="UTF-8")
archivoVolcado.write("{")

# Totales
archivoVolcado.write('"totales":{')
for i in range(ord("a"), ord("z") + 1):
    try:
        archivoVolcado.write(str('"' + chr(i) + '": ' + str(Letras[chr(i)]) + ", "))
    except KeyError:
        archivoVolcado.write(str('"' + chr(i) + '": ' + "0.0000" + ", "))
    archivoVolcado.write('\n')
archivoVolcado.write("}")

# Porcentuales
archivoVolcado.write('"porcentuales":{')
for i in range(ord("a"), ord("z") + 1):
    try:
        archivoVolcado.write(str('"' + chr(i) + '": ' + "%.4f" % (Letras[chr(i)]/contador) + ", "))
    except KeyError:
        archivoVolcado.write(str('"' + chr(i) + '": ' + "0.0000" + ", "))
    archivoVolcado.write('\n')
archivoVolcado.write("}")

archivoVolcado.write("}")