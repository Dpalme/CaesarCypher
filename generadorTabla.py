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
LetrasChar = []
for key in Letras:
    Letras[key] = Letras[key]/contador
    archivoVolcado.write(str('"' + key + '": ' + "%.4f" % Letras[key] + ", "))
    LetrasChar.append((key, Letras[key]))

plot.plot(LetrasChar)
plot.show()