# encoding = UTF-8
import json
import random

def encode(key, stringToEncode):
    finalString = ""
    for char in stringToEncode.lower():
        if char.isalpha():
            if ord(char) + key > 122:
                finalString += chr(96 + key - (122 - ord(char)))
            else:
                finalString += chr(ord(char) + key)
        else:
            finalString += char
    return finalString


def normalizeString(string):
    string = string.lower()
    string = string.replace("í", "i")
    string = string.replace("é", "e")
    string = string.replace("á", "a")
    string = string.replace("ó", "o")
    string = string.replace("ú", "u")
    string = string.replace("ñ", "n")
    return string


def decode(key, mensaje):
    mensajeDescifrado = ""
    for letra in mensaje:
            mensajeDescifrado += chr(122 - key + ord(letra) - 96 if ord(letra) - key < 97 else ord(letra) - key) if letra.isalpha() else letra
    return mensajeDescifrado


def maxKey(dictionary):
    maximum = 0
    maxKeyValue = ""
    for key in dictionary:
        if dictionary[key] > maximum:
            maximum = dictionary[key]
            maxKeyValue = key
    return maxKeyValue

def keyWithChi(obtainedFrequencies, numLetras):
    with open('output.json', encoding="UTF-8") as json_file:
        database = json.load(json_file)
    expectedFrec = database["porcentajes"]
    potentialKeys = []
    for i in range(0, 26):
        chisqrd = 0
        for j in range(0, 26):
            e = expectedFrec[chr(j+97)]*numLetras
            if(i+j+97 <123):
                o = obtainedFrequencies[chr(i+j+97)]
            else:
                o = obtainedFrequencies[chr(96+i-(122-(97+j)))]
            try:
                chisqrd += ((e-o)**2)/e
            except ZeroDivisionError:
                chisqrd += 0
        potentialKeys.append(chisqrd)
    return (potentialKeys.index(min(potentialKeys)))


def keyFinder(mensaje):
    Letras = {}
    for x in range(97, 123):
        Letras[chr(x)] = 0
    contador = 0
    for char in mensaje.lower():
        if char.isalpha():
            contador += 1
            try:
                Letras[char] = Letras[char] + 1
            except KeyError:
                Letras[char] = 1
    return keyWithChi(Letras, contador)

key = random.randint(0,26)
originalMessage="Las autoridades han informado que las fuertes lluvias se continuarán presentando en los próximos días en diversas zonas de la CDMX. Además, se prevé que la temperatura disminuya, debido a la entrada del frente frío número 7. Una de las alcaldías que más afectaciones ha presentado debido a las fuertes precipitaciones es Iztapalapa, donde las inundaciones alcanzan hasta los 60 centímetros. De acuerdo con Excélsior, otras alcaldías que han sido afectadas son Azcapotzalco, Álvaro Obregón, Cuauhtémoc, Gustavo A. Madero y Miguel Hidalgo, aunque sólo con leves daños materiales y, eso sí, serios detrimentos al tránsito."
originalMessage = normalizeString(originalMessage)
codedMessage = encode(key, originalMessage)
print(originalMessage)
print(codedMessage)
print(decode(keyFinder(codedMessage), codedMessage))
