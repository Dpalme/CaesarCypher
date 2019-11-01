# encoding = UTF-8
import json
import random

# Esta funcion regresa el número de caracter en Unicode.
def num(char):
    return ord(char)-97

# Regresa el caracter que se encuentra en la posición "number" del abecedario traducido a Unicode.
def character(number):
    return chr(97 + number%26)


def normalizeString(string):
    string = string.lower()
    string = string.replace("í", "i").replace("é", "e").replace("á", "a").replace("ó", "o").replace("ú", "u")
    string = string.replace("ñ", "n").replace("à", "a").replace("ù", "u").replace("ï", "i").replace("ù", "u")
    return string.replace("ü", "u")

# Codifica el mensaje usando la llave recibida y regresa el mensaje
def encode(key, stringToEncode):
    finalString = ""
    for char in stringToEncode.lower():
        # // Junta todos los caracteres en un único string.
        # // Es una condición que checa si el caracter está entre la "a" y la "z". 
        # // Si es cierto regresa el caracter modificado con la llave.
        # // Si la condición no se cumple solo añade el caracter (Esto para que los espacios se queden en su lugar y no cambiar puntos ni comas.
        # //              condicion verdadera        condicion           condicion falsa
        finalString += character(num(char)+ key) if char.isalpha() else finalString += char
    return finalString
    
# // Decodifica el mensaje con la llave que se le de
def decode(key, mensaje):
    mensajeDescifrado = ""
    for letra in mensaje:
            # // Al igual que la codificacion, junta una cadena con las letras codificadas y los espacios en su lugar.
            mensajeDescifrado +=  character(num(letra)-key) if letra.isalpha() else letra
    return mensajeDescifrado

# // Funcion que intenta todas las llaves y regresa un mensaje con cada llave probada
# // Esta funcion se usa cuando el mensaje es muy chico, porque el metodo de frecuencia no es eficaz.
def bruteForce(message):
    # // For que usa todas las diferentes llaves
    for i in range (0, 26):
        for char in message:
            msg += character(num(char)+1) if char.isalpha() else char
        message = msg
        # // For que crea los mensajes con cada llave y los añade a una sola cadena
        print(message + "|| key=%d" % i)

# // Funcion que descifra el mensaje con el uso de chi cuadrada
def keyWithChi(mensaje):
    # // Primero se crea un diccionario con todas las letras.
    Letras = {character(x): 0 for x in range(26)}
    contador = 0
    # // Este for recorre todos los caracteres del mensaje y los cuenta.
    # // El conteo se modifica en el diccionario "frequency" y también cuenta el número total de letras
    for char in mensaje.lower():
        if char.isalpha():
            contador += 1
            Letras[char] = Letras[char] + 1
    with open('output.json', encoding="UTF-8") as json_file:
        expectedFrec = json.load(json_file)["porcentajes"]
    potentialKeys = []
    # // Compara las frecuencias esperadas (Quijote) con las obtenidas (usando lo anterior)
    for i in range(0, 26):
        chisqrd = 0
        # // este for recorre todas las llaves posibles
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
    return keyWithChi(mensaje) if len(mensaje)>6 else bruteForce(mensaje)


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