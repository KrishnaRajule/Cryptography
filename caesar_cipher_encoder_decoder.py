## Encoder Decoder (Caesar) ##
#
#Author: Shrikrishna B Rajule
#Date: 07/09/2020
#
type = int(input("Enter 1 to encode and 0 decode: "))
inp = list()
a = list()
out = list()
def split(word):
    return [char for char in word]

if type == 0:
    cipher_text = input("Enter the Cipher Text: ")
    shift = input("Enter the shift number/Press Enter: ")
    if shift == "":
        s = False
    else:
        s = True

    inp = split(cipher_text)
    length = len(inp)

    for i in range(length):
        a.append(ord(inp[i]))

    if s == False:
        for j in range(1,27):
            out.clear()
            for k in range(length):
                if a[k] == 32:
                    continue
                out.append(chr(a[k]-j))
            print("".join(out))
    else:
        for k in range(length):
            if a[k] == 32:
                continue
            out.append(chr(a[k]-int(shift)))
        print("".join(out))
else:
    plain_text = input("Enter the Plain Text: ")
    shift = input("Enter the shift number/Press Enter: ")
    if shift == "":
        s = False
    else:
        s = True

    inp = split(plain_text)
    length = len(inp)

    for i in range(length):
        a.append(ord(inp[i]))

    if s == False:
        for j in range(1,27):
            out.clear()
            for k in range(length):
                if a[k] == 32:
                    continue
                out.append(chr(a[k]+j))
            print("".join(out))
    else:
        for k in range(length):
            if a[k] == 32:
                continue
            out.append(chr(a[k]+int(shift)))
        print("".join(out))
