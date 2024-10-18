print("Please input the number")
num = int(input())
print("What system is the number from? d(decimal), b(binary), h(hex),o(octal)")
system = input()
original = num

def hex():              ##Need a decimal number
    global h
    global num
    temp_num = num
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
    temp_num = num
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
    temp_num = num
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