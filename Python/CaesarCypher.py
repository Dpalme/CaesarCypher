# encoding = UTF-8
import json
import matplotlib.pyplot as plot
import random


def num(char):
    return ord(char)-97


def character(number):
    return chr(97 + number%26)


def normalizeString(string):
    string = string.lower()
    string = string.replace("í", "i").replace("é", "e").replace("á", "a").replace("ó", "o").replace("ú", "u")
    string = string.replace("ñ", "n").replace("à", "a").replace("ù", "u").replace("ï", "i").replace("ù", "u")
    return string.replace("ü", "u")


def encode(key, stringToEncode):
    finalString = ""
    for char in stringToEncode.lower():
        if char.isalpha():
            character(num(char)+ key)
        else:
            finalString += char
    return finalString
    

def decode(key, mensaje):
    mensajeDescifrado = ""
    for letra in mensaje:
            mensajeDescifrado +=  character(num(letra)-key) if letra.isalpha() else letra
    return mensajeDescifrado


def keyWithChi(obtainedFrequencies, numLetras):
    with open('output.json', encoding="UTF-8") as json_file:
        expectedFrec = json.load(json_file)["porcentajes"]
    potentialKeys = []
    for i in range(0, 26):
        chisqrd = 0
        for j in range(0, 26):
            e = expectedFrec[character(j)]*numLetras
            o = obtainedFrequencies[character(i+j)]
            try:
                chisqrd += ((e-o)**2)/e
            except ZeroDivisionError:
                chisqrd += 0
        potentialKeys.append(chisqrd)
    return potentialKeys.index(min(potentialKeys))


def keyFinder(mensaje):
    Letras = {character(x): 0 for x in range(26)}
    contador = 0
    for char in mensaje.lower():
        if char.isalpha():
            contador += 1
            Letras[char] = Letras[char] + 1
    return keyWithChi(Letras, contador)


def main():
    codedMessage = "b ho fxhuyr qxqfd hpsuhqglr ho yxhor, dxq vljxh srvdgr vreuh ho exvwr gh sdodv, vreuh ho glqwho gh pl sxhuwd"
    key = keyFinder(codedMessage)
    print("mensaje codificado: " + str(codedMessage))
    print("key:" + str(key))
    print("mensaje decodificado: " + str(decode(key, codedMessage)))


# b ho fxhuyr qxqfd hpsuhqglr ho yxhor, dxq vljxh srvdgr vreuh ho exvwr gh sdodv, vreuh ho glqwho gh pl sxhuwd
# key:3
# y el cuervo nunca emprendio el vuelo, aun sigue posado sobre el busto de palas, sobre el dintel de mi puerta

# lfy yz sp nzyzntoz l ylotp opw bfp yz afpol lacpyopc lwrz
# key:11
# aun no he conocido a nadie del que no pueda aprender algo

# vtlmbzt xqatnlmh xe ihlmx mhlvh r lxvh, r tlxznkt bgytnlmh jnx at oblmh ehl xlixvmkhl
# key:19
# castiga exhausto el poste tosco y seco, y asegura infausto que ha visto los espectros

# elix bpql bp rkx morbyx
# key:23
# hola esto es una prueba

# sv xbl kpnv lz mhszv
# key:7
# lo que digo es falso

# cjgv
# key: 4
# hola