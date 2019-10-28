import json

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
            mensajeDescifrado += chr(122 - key + ord(letra) - 96 if ord(letra) - key < 97 else ord(letra) - key) if letra.isalpha() else letra
    return mensajeDescifrado


def maxKey(dictionary):
    maximum = 0
    maxKeyValue = ""
    for key in dictionary:
        if dictionary[key] > maximum and key != " ":
            maximum = dictionary[key]
            maxKeyValue = key
    return maxKeyValue


def keyFinder(mensaje):
    with open('output.json', encoding="UTF-8") as json_file:
        database = json.load(json_file)
    Letras = {}
    contador = 0
    for char in mensaje.lower():
        contador+=1
        try:
            Letras[char] = Letras[char] + 1
        except KeyError:
            Letras[char] = 1
    
    for key in Letras:
        Letras[key] = Letras[key] / contador
    return ord(maxKey(Letras)) - ord("e")


codedMessage = encode(4 ,"bebe no quiero ver netflix quiero ver tu carita toda la vida")
print(codedMessage)
key = keyFinder(codedMessage)
print(key)
print(decode(key, codedMessage))