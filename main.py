print("Please input the number")
num = input()
print("What system is the number from? d(decimal), b(binary), h(hex),o(octal)")
system = input()
original = num

def toDecimal():
    global num
    dec = 0
    if system == "h":
        num = num.upper()
        for i in range(len(num)):
            temp = num[len(num)-(i+1)]
            if temp == "A":
                temp = 10
            elif temp == "B":
                temp = 11
            elif temp == "C":
                temp = 12
            elif temp == "D":
                temp = 13
            elif temp == "E":
                temp = 14
            elif temp == "F":
                temp = 15
            dec = dec + int(temp)*(16**i)
        num = dec
        return num
    elif system == "o":
        if not num.isalnum():
            print("That's not an Octal number")
        for i in range(len(num)):
            temp = num[len(num)-(i+1)]
            dec = dec + int(temp)*(8**i)
        num = dec
        return num
    elif system == "b":
        for i in range(len(num)):
            temp = num[len(num)-(i+1)]
            temp = int(temp)
            if temp > 1 or temp < 0:
                print("That´s not a binary number")
            dec = dec + int(temp)*(2**i)
        num = dec
        return num

def hex():              ##Need a decimal number
    global h
    global num
    temp_num = int(num)
    h = ""
    while True:
        i = temp_num % 16
        temp_num = int(temp_num / 16)
        if i == 10:
            i = "A"
        elif i == 11:
            i = "B"
        elif i == 12:
            i = "C"
        elif i == 13:
            i = "D"
        elif i == 14:
            i = "E"
        elif i == 15:
            i = "F"

        h = str(i) + h
        if temp_num == 0:
            break
def octal():                ##Need a decimal as well. So, i need a toDecimal() before calling those
    global o
    global num
    temp_num = int(num)
    o = ""
    while True:
        i = temp_num % 8
        temp_num = int(temp_num/8)
        o = str(i) + o
        if temp_num == 0:
            break
def binary():               ##Same decimal thing
    global b
    global num
    temp_num = int(num)
    b = ""
    while True:
        i = temp_num % 2
        temp_num = int(temp_num/2)
        b = str(i) + b
        if temp_num == 0:
            break

if system =="d":
    hex()
    octal()
    binary()
    print(f"Decimal: {original} \nHexadecimal: {h} \nOctal: {o} \nBinary: {b}")
elif system == "h":
    toDecimal()
    octal()
    binary()
    original = original.upper()
    print(f"Decimal: {num} \nHexadecimal: {original} \nOctal: {o} \nBinary: {b}")
elif system == "o":
    toDecimal()
    hex()
    binary()
    print(f"Decimal: {num} \nHexadecimal: {h} \nOctal: {original} \nBinary: {b}")
elif system == "b":
    toDecimal()
    hex()
    octal()
    print(f"Decimal: {num} \nHexadecimal: {h} \nOctal: {o} \nBinary: {original}")
else:
    print("Error, Input not recognized")
