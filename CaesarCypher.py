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


def decode(key, stringToDecode):
    finalString = ""
    for char in stringToDecode.lower():
        if char.isalpha():
            if chr(ord(char) - key).isalpha():
                if chr(ord(char) - key).islower():
                    finalString += chr(ord(char) - key)
                else:
                    finalString += chr((ord(char) - key) + (ord("z")-ord("a")))
            else:
                finalString += chr((ord(char) - key) - (ord("z")-ord("a")+1))
        else:
            finalString+=char
    return finalString

print(decode(24, encode(24, "Que pedo soy el mero mero miguel hidalgo hdtptm. viaje en el tiempo para partirte tu reputisima madre")))