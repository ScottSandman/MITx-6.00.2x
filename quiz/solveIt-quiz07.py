# -*- coding: utf-8 -*-
"""
Created on Thu May 10 14:14:08 2018

@author: Sandman
"""



def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    x = 0
    while test(x) is False:
        if x < 100:
            x += 1
        else:
            x = -100
    return x
    

def f(x):
    return (x+15)**0.5 + x**0.5 == 15
    return x == 0
    return x == 100
    return x == 26
    return x**2 == 9
    return x == -4
    return x**2 + x + 0 == 0
    return x == -80
    return x == 2
    return [1,2,3][-x] == 1 and x !=0

#print(solveit(f))
#print(f(x))
#test = f(x)
print(solveit(f))

