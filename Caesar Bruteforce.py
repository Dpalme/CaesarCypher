message = "cjgv"

def num(char):
    return ord(char)-97


def character(number):
    return chr(97 + number%26)


for i in range (0, 26):
    msg = ""
    for char in message:
        msg += character(num(char)+1) if char.isalpha() else char
    message = msg
    print(message + "|| key=%d" % i)
