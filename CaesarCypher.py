def encode(key, stringToEncode):
    finalString = ""
    for char in stringToEncode.lower():
        finalString += 96 + key - (122 - ord(char)) if ord(char) + key> 122 else char
    return finalString


def decode(key, mensaje):
    mensajeDescifrado = ""
    for letra in mensaje.lower():
            mensajeDescifrado += chr(122 - key + ord(letra) - 96 if ord(letra) - key < 97 else ord(letra) - key) if letra.isalpha() else letra
    return mensajeDescifrado