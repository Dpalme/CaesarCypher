def encode(key, stringToEncode):
    print(stringToEncode)
    finalString = ""
    for char in stringToEncode.lower():
        if char.isalpha():
            finalString += chr(ord(char) + key - (ord("z")-ord("a")+1) if ord(char)+key > ord("z") else ord(char) + key)
        else:
            finalString+=char
    print(finalString)
    return finalString


def decode(key, mensaje):
    mensajeDescifrado = ""
    for palabra in mensaje.lower():
        for letra in palabra:
            if letra.isalpha():
                x = ord(letra)
                if x - key < 97:
                    x = 122 - key + (x - 96)
                else:
                    x -= key
                mensajeDescifrado += chr(x)
            else:
                mensajeDescifrado += letra
    return mensajeDescifrado

print(decode(24, encode(24, "Que pedo soy el mero mero miguel hidalgo hdtptm. viaje en el tiempo para partirte tu reputisima madre")))