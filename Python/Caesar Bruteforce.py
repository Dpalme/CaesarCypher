from CaesarCypher import num, character

message = "cjgv"

for i in range (0, 26):
    msg = ""
    for char in message:
        msg += character(num(char)+1) if char.isalpha() else char
    message = msg
    print(message + "|| key=%d" % i)
