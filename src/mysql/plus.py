# encoding=utf-8

import sys
def ReadKeyWord():
    f = open("test")
    keyWord = []
    for line in f.readlines():
        tmp = line.split(",")
        keyWord.append(tmp[0])
        keyWord.append(tmp[1])
    return keyWord
