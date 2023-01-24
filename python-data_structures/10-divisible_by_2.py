#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    
    for i in my_list:
        r = []    
        if i % 2 == 0:
            r.append(True)
        else:
            r.append(False)
    return r
