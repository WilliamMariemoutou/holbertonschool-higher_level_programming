#!/usr/bin/python3
def no_c(my_string):
    letter = "c"
    new_list = []
    
    for s in my_string:
        new_s = ""
        for char in s:
            if char != letter:
                new_s += char
        new_list.append(new_s)
    print(new_list)
