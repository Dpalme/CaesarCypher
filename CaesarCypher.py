def encode(key, stringToEncode):
    finalString = ""
    for char in stringToEncode.lower():
            finalString += chr(ord(char) + key - (ord("z")-ord("a")+1) if ord(char)+key > ord("z") else ord(char) + key) if char.isalpha() else char
    return finalString


def decode(key, mensaje):
    mensajeDescifrado = ""
    for palabra in mensaje.lower():
        for letra in palabra:
                mensajeDescifrado += chr(122 - key + ord(letra) - 96 if ord(letra) - key < 97 else ord(letra) - key) if letra.isalpha() else letra
    return mensajeDescifrado