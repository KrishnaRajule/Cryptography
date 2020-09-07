###### Caesar Cipher ######
#
###### Author: SHRIKRISHNA BHAGIRATH RAJULE
#
###### Dated: 07/09/2020
#
###### Description: This code would decrypt and encrypt messages with a shift provided by the user or you can also get all of them at once(By just following the commands),
###### This is a Basic Cryptography method - Caesar type enryption and decryption.
#
#
type = int(input("Enter 1 to encode and 0 decode: "))
inp = list()
a = list()
out = list()
up = dict()
for x in range(26):
    up[65+x] = up.get(65+x,x)
lo = dict()
for y in range(26):
    lo[97+y] = lo.get(97+y,y)

def split(word):
    return [char for char in word]

def get_up_key(val):
    for key,value in up.items():
        if val == value:
            return key

def get_lo_key(val):
    for key,value in lo.items():
        if val == value:
            return key

if type == 0:
    cipher_text = input("Enter the Cipher Text: ")
    shift = input("Enter the shift number/Press Enter to get all: ")
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
                if a[k] in range(32,48) or a[k] in range(58,65) or a[k] in range(91,97) or a[k] in range(123,127) or a[k] in range(48,58):
                    out.append(chr(a[k]))
                    continue
                if a[k] in up:
                    v = up.get(a[k])
                    valu = abs(v-j+26)%26
                    out.append(chr(get_up_key(valu)))
                else:
                    v = lo.get(a[k])
                    valu = abs(v-j+26)%26
                    out.append(chr(get_lo_key(valu)))
            print("".join(out))
    else:
        for k in range(length):
            if a[k] in range(32,48) or a[k] in range(58,65) or a[k] in range(91,97) or a[k] in range(123,127) or a[k] in range(48,58):
                out.append(chr(a[k]))
                continue
            if a[k] in up:
                v = up.get(a[k])
                valu = abs(v-int(shift)+26)%26
                out.append(chr(get_up_key(valu)))
            else:
                v = lo.get(a[k])
                valu = abs(v-int(shift)+26)%26
                out.append(chr(get_lo_key(valu)))
        print("".join(out))
else:
    plain_text = input("Enter the Plain Text: ")
    shift = input("Enter the shift number/Press Enter to get all: ")
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
                if a[k] in range(32,48) or a[k] in range(58,65) or a[k] in range(91,97) or a[k] in range(123,127) or a[k] in range(48,58):
                    out.append(chr(a[k]))
                    continue
                if a[k] in up:
                    v = up.get(a[k])
                    valu = abs(v+j+26)%26
                    out.append(chr(get_up_key(valu)))
                else:
                    v = lo.get(a[k])
                    valu = abs(v+j+26)%26
                    out.append(chr(get_lo_key(valu)))
            print("".join(out))
    else:
        for k in range(length):
            if a[k] in range(32,48) or a[k] in range(58,65) or a[k] in range(91,97) or a[k] in range(123,127) or a[k] in range(48,58):
                out.append(chr(a[k]))
                continue
            if a[k] in up:
                v = up.get(a[k])
                valu = abs(v+int(shift)+26)%26
                out.append(chr(get_up_key(valu)))
            else:
                v = lo.get(a[k])
                valu = abs(v+int(shift)+26)%26
                out.append(chr(get_lo_key(valu)))
        print("".join(out))

###########################################################################################################################################################
