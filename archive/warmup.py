#!/usr/bin/env python3 

def len(seq): 
    if type(seq) in [list,dict]:
        return -1
    nelems=0
    for elem in seq:
        nelems+=1

    return nelems

len() 
