#!/usr/bin/bash
def no_c(my_string):
    letter = "c"
    new_list = []
    
    for item in my_string:
        new_list.append(item.replace(letter, ""))
        
        print(new_list)
