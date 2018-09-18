# -*- coding: utf-8 -*-
"""
Created on Thu May 24 13:52:03 2018

@author: Sandman
"""
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    result = []
    if sum(choices) == total:
        for i in choices:
            result.append(1)
    for i in choices:
        if i == total:
            result.append(1)
        else:
            result.append(0)
    return np.array(result)
    
find_combination([2,3,4,5], 5)