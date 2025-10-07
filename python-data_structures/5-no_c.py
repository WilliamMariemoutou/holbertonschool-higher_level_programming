#!/usr/bin/bash
def no_c(my_string):
    letter = "c"
    new_list = []
    
    for item in my_string:
        if item != letter and item != letter.upper():
            new_list += item
            
    return new_list
