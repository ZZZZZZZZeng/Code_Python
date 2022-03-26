# 1<=num<=3999

def intToRoman(num):
    s = ""
    dic = {1: "I", 2: "II", 3: "III", 4: "IIIV", 5: "v", 6: "VI", 7: "VII", 8: "VIII", 9: "IV", 10: "x"}
    if num >= 1000:
        temp = num // 1000
        for i in range(temp):
            s += "M"
        num = num % 1000
    if 100 <= num < 1000:
        temp = num // 100
        if 0 < temp < 4:
            for i in range(temp):
                s += "C"
        elif temp == 4:
            s += "CD"
        elif temp == 5:
            s += "D"
        elif 5 < temp < 9:
            s += "D"
            for i in range(temp - 5):
                s += "C"
        elif temp == 9:
            s += "CM"
        num = num % 100
    if 10 <= num < 100:
        temp = num // 10
        if 0 < temp < 4:
            for i in range(temp):
                s += "X"
        elif temp == 4:
            s += "XL"
        elif temp == 5:
            s += "L"
        elif 5 < temp < 9:
            s += "L"
            for i in range(temp - 5):
                s += "X"
        elif temp == 9:
            s += "XC"
        num = num % 10
    if 0 < num < 10:
        if 0 < num < 4:
            for i in range(num):
                s += "I"
        elif num == 4:
            s += "IV"
        elif num == 5:
            s += "V"
        elif 5 < num < 9:
            s += "V"
            for i in range(num - 5):
                s += "I"
        elif num == 9:
            s += "IX"
    return s


print(intToRoman(58))
