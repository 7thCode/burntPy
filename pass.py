#!python
# -*- coding: utf-8 -*-

import sys
import math

args = sys.argv
if len(args) == 2:

    mediocre = ['qqww1122', 'hottie', '7777777', 'letmein', 'donald', 'master', '123qwe', 'qwerty123',
            '12345', '1234', 'admin', 'adobe123', '12345678', 'michael', 'hello', 'shadow', '1234567',
            'bailey', '1234567890', 'whatever', 'iloveyou', '123123', 'Dragon', 'qazwsx', '!@#$%^&*',
            'solo', 'trustno1', 'photoshop', 'ninja', 'princess', 'Qwertyuiop', '123456789', 'Iloveyou',
            '1q2w3e4r', 'Million2', 'login', 'football', 'access', 'charlie', 'starwars', '18atcskd2w',
            '3rjs1la7qe', 'monkey', 'picture1', '12345679', '123321', '1q2w3e', 'aaron431', '1111111',
            'freedom', '123', 'flower', 'senha', '1q2w3e4r5t', 'mustang', 'zaq1zaq1', 'ashley', 'zxcvbnm',
            'mynoob', 'azerty', 'google', 'batman', '555555', '696969', '000000', '1qaz2wsx', 'jesus',
            'Monkey', 'Football', '987654321', 'abc123', '123456', 'qwertyuiop', '121212', 'baseball',
            'dragon', 'superman', 'aa123456', 'loveme', 'password1', 'password', '654321', '888888',
            '666666', 'qwerty', 'sunshine', 'passw0rd', 'lovely', '111111', 'welcome']

    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
    symbol = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "{", "}", "[", "]", "|", "\\",
          ":", ";", "'", '"', "<", ",", ">", ".", "?", "/"]

    password = args[1]
    result = 1

    if password in mediocre:
        print("NG")
    else:
        for s in password:
            if s in number:
                result *= len(number)
            elif s in upper:
                result *= len(upper)
            elif s in lower:
                result *= len(lower)
            elif s in symbol:
                result *= len(symbol)

        sec = result /1000

        print(str(int(sec / 60)) + "分")
        print(str(int((sec / 60) / 60)) + "時間")
        print(str(int(((sec / 60) / 60) / 24)) + "日")
        print(str(int((((sec / 60) / 60) / 24) / 30)) + "か月")
        print(str(int(((((sec / 60) / 60) / 24) / 30) / 12)) + "年")
        print(str(int((((((sec / 60) / 60) / 24) / 30) / 12) / 10000)) + "万年")
        print(str(int(((((((sec / 60) / 60) / 24) / 30) / 12) / 10000) / 10000)) + "億年")
        print(str(int((((((((sec / 60) / 60) / 24) / 30) / 12) / 10000) / 10000) / 10000)) + "兆年")
        print(str(int(((((((((sec / 60) / 60) / 24) / 30) / 12) / 10000) / 10000) / 10000) / 10000)) + "京年")