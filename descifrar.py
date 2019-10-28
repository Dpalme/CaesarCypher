frecuenciaEsperada = [12.53,1.42,4.68,5.86,13.68,0.69,1.01,0.70,6.25,0.44,0.02,4.97,3.15,6.71,0.31,8.68,2.51,0.88,6.87,7.98,4.63,3.93,0.90,0.01,0.22,0.90,0.52]

def cifrar(mensaje, llave):
    mensajeDescifrado = ""
    mensaje = mensaje.split()
    for palabra in mensaje:
        palabra = palabra.lower()
        palabraCifrada = ""
        for letra in palabra:
            x = ord(letra)
            if x + llave> 122:
                x = 96 + llave - (122 - x)
            else:
                x += llave
            palabraCifrada += chr(x)
        mensajeDescifrado += " " + palabraCifrada
    return mensajeDescifrado


def descifrar(mensaje, llave):
    mensajeDescifrado = ""
    mensaje = mensaje.split()
    for palabra in mensaje:
        palabra = palabra.lower()
        palabraDescifrada = ""
        for letra in palabra:
            x = ord(letra)
            if x - llave < 97:
                x = 122 - llave + (x - 96)
            else:
                x -= llave
            palabraDescifrada += chr(x)
        mensajeDescifrado += " " + palabraDescifrada
    return mensajeDescifrado


def main():
    mensaje = "hola mundo zzz"
    llave = 1
    msj = cifrar(mensaje, llave)
    print(msj)
    msj = descifrar(msj, llave)
    print(msj)


main()