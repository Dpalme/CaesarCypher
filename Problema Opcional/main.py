# encoding: UTF-8

import random


def normalizeString(string):
    string = string.lower()
    string = string.replace("í", "i")
    string = string.replace("é", "e")
    string = string.replace("á", "a")
    string = string.replace("ó", "o")
    string = string.replace("ú", "u")
    string = string.replace("ñ", "n")
    return string


def avg(array):
    sum = 0
    for x in array:
        sum += x
    return sum//len(array)


def contarLetrasDiferentes(message):
    Letras = []
    for char in normalizeString(message):
        if char.isalpha():
            try:
                Letras.index(char)
            except ValueError:
                Letras.append(char)
    return len(Letras)


def num(char):
    return ord(char)-96


def character(number):
    return chr(96 + number%27)


def encode(key, message):
    cycle = 0
    newString = ""
    for char in normalizeString(message):
        newString += character(num(char) + num(key[cycle])) if char.isalpha() else char
        cycle = cycle + 1 if cycle < len(key) - 1 else 0
    return newString


def decode(key, message):
    cycle = 0
    newString = ""
    for char in normalizeString(message):
        newString += character(num(char) - num(key[cycle])) if char.isalpha() else char
        cycle = cycle + 1 if cycle < len(key) - 1 else 0
    return newString


def keyFinder(message):
    messageNumbers = [ord(x) - 97 for x in message]
    return avg(messageNumbers)


key = "abba"
message = "Las autoridades han informado que las fuertes lluvias se continuarán presentando en los próximos días en diversas zonas de la CDMX. Además, se prevé que la temperatura disminuya, debido a la entrada del frente frío número 7. Una de las alcaldías que más afectaciones ha presentado debido a las fuertes precipitaciones es Iztapalapa, donde las inundaciones alcanzan hasta los 60 centímetros. De acuerdo con Excélsior, otras alcaldías que han sido afectadas son Azcapotzalco, Álvaro Obregón, Cuauhtémoc, Gustavo A. Madero y Miguel Hidalgo, aunque sólo con leves daños materiales y, eso sí, serios detrimentos al tránsito."
encodedMessage = encode(key, message)
print(96%26)
print(normalizeString(message))
print(contarLetrasDiferentes(normalizeString(message)))
print(encodedMessage)
print(contarLetrasDiferentes(encodedMessage))
print(decode(key, encodedMessage))
print(contarLetrasDiferentes(message))
