#!python

# コマンドに
import sys

print(sys.version_info)

args = sys.argv
if len(args) == 2:

    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
    symbol = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "{", "}", "[", "]", "|", "\\",
          ":", ";", "'", '"', "<", ",", ">", ".", "?", "/"]

    result = 1
    password = args[1]

    for s in password:
        if s in number:
            result *= len(number)
        elif s in upper:
            result *= len(upper)
        elif s in lower:
            result *= len(lower)
        elif s in symbol:
            result *= len(symbol)

    sec = int(result / 1000)
    min  = int(sec / 60)
    hour = int(min / 60)
    days = int(hour / 24)
    mon = int(days / 30)
    year = int(mon / 12)
    myear = int(year / 10000)
    byear = int(myear / 10000)
    tyear = int(byear / 10000)
    qyear = int(tyear / 10000)

    print(str(min) + "分")
    print(str(hour) + "時間")
    print(str(days) + "日")
    print(str(mon) + "か月")
    print(str(year) + "年")
    print(str(myear) + "万年")
    print(str(byear) + "億年")
    print(str(tyear) + "兆年")
    print(str(qyear) + "京年")

else:
    print("no arg.")

