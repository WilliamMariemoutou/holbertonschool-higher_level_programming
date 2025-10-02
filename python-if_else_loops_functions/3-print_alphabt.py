#!/usr/bin/python3

alphabet = ""
for i in range(97, 123):
    if i != 101 and i != 113:
        alphabet += "{}".format(chr(i))
print(alphabet, end="")
