#!/usr/bin/python3
def islower(c):
    if type(c) != str or len(c) != 1:
        print("Error: input must be a single character")
        raise TypeError
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
