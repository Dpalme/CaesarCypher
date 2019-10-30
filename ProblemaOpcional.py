# encoding: UTF-8

import random
from generadorTabla import normalizeString
from CaesarCypher import character, num


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
    key = ""
    for x in range(3):
        key += character(random.randint(0,26))
    return key 


def main():
    key = "sol"
    message = "Las autoridades han informado que las fuertes lluvias se continuarán presentando en los próximos días en diversas zonas de la CDMX. Además, se prevé que la temperatura disminuya, debido a la entrada del frente frío número 7. Una de las alcaldías que más afectaciones ha presentado debido a las fuertes precipitaciones es Iztapalapa, donde las inundaciones alcanzan hasta los 60 centímetros. De acuerdo con Excélsior, otras alcaldías que han sido afectadas son Azcapotzalco, Álvaro Obregón, Cuauhtémoc, Gustavo A. Madero y Miguel Hidalgo, aunque sólo con leves daños materiales y, eso sí, serios detrimentos al tránsito."
    encodedMessage = encode(key, normalizeString(message))
    print(encodedMessage)
    contador = 0
    while keyFinder(encodedMessage) != key:
        contador += 1
    print(contador)
    # key = keyFinder(encodedMessage)
    print(key)
    print(decode(key, encodedMessage))

main()