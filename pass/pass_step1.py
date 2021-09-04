# passwordに使える文字
# 数字
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# 大文字アルファベット
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]
# 小文字アルファベット
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
# 記号
symbol = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "{", "}", "[", "]", "|", "\\",
          ":", ";", "'", '"', "<", ",", ">", ".", "?", "/"]

# 絶対に一回は試す
result = 1

# 対象のパスワード候補
password = "Test10@#dff3556"

# passwordの一文字づつ順番に
for s in password:
    # それは数字？
    if s in number:
        # 数字であればそのとりえる数を掛ける。
        result *= len(number)
    # それは大文字？
    elif s in upper:
        # 大文字であればそのとりえる数を掛ける。
        result *= len(upper)
    # それは小文字？
    elif s in lower:
        # 小文字であればそのとりえる数を掛ける。
        result *= len(lower)
    # それは記号？
    elif s in symbol:
        # 記号であればそのとりえる数を掛ける。
        result *= len(symbol)

# 文字列に含まれる文字種からその取りえる数は
print(str(result))




