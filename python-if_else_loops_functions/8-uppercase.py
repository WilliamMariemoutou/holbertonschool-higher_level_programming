#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            result += (chr(ord(char) - (ord('a') - ord('A'))), end="")
        else:
            result += char
            
    print(result)
    print()
        