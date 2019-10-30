frecuenciaEsperada = [12.53,1.42,4.68,5.86,13.68,0.69,1.01,0.70,6.25,0.44,0.02,4.97,3.15,6.71,8.68,2.51,0.88,6.87,7.98,4.63,3.93,0.90,0.01,0.22,0.90,0.52]
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


def decode(key, mensaje):
    mensajeDescifrado = ""
    for letra in mensaje:
        mensajeDescifrado += chr(
            122 - key + ord(letra) - 96 if ord(letra) - key < 97 else ord(letra) - key) if letra.isalpha() else letra
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
    expectedFrec = {}
    potentialKeys = []
    for x in range(0, 26):
        expectedFrec[chr(x+97)] = frecuenciaEsperada[x]
    for i in range(0, 26):
        chisqrd = 0
        for j in range(0, 26):
            e = expectedFrec[chr(j+97)]*numLetras
            if(i+j+97 <123):
                o = obtainedFrequencies[chr(i+j+97)]
            else:
                o = obtainedFrequencies[chr(96+i-(122-(97+j)))]
            chisqrd += ((e-o)**2)/e
        potentialKeys.append(chisqrd)
    return (potentialKeys.index(min(potentialKeys)))



def keyFinder(mensaje):
    """with open('output.json', encoding="UTF-8") as json_file:
        database = json.load(json_file)"""
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


key = random.randint(0, 26)
originalMessage = "hola mundo"
codedMessage = encode(key, originalMessage)
print(originalMessage)
print(key)
print(codedMessage)
print(keyFinder(codedMessage))
print(decode(keyFinder(codedMessage), codedMessage))