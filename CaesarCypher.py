def encode(key, stringToEncode):
    finalString = ""
    for char in stringToEncode.lower():
        finalString += 96 + key - (122 - ord(char)) if ord(char) + key> 122 else char
    return finalString


def decode(key, mensaje):
    mensajeDescifrado = ""
    for letra in mensaje:
            mensajeDescifrado += chr(122 - key + ord(letra) - 96 if ord(letra) - key < 97 else ord(letra) - key) if letra.isalpha() else letra
    return mensajeDescifrado


def keyFinder(mensaje):
    distBase = open("output.json", "r", encoding="UTF-8")
    Letras = {}
    contador = 0

    for char in mensaje.lower():
        contador+=1
        try:
            Letras[char] = Letras[char] + 1
        except KeyError:
            Letras[char] = 1
    LetrasChar = []
    for key in Letras:
        Letras[key] = Letras[key]/contador
        LetrasChar.append((key, Letras[key]))