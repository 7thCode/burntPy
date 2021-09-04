# 引数の数チェック
import sys

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

    print(str(int(result)))

else:
    print("no arg.")

