# -*- coding: utf-8 -*-
"""
Created on Thu May 10 16:23:00 2018

@author: Sandman
"""
L = []

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    str_lengths = []
    for i in range(len(L)):
        str_lengths.append(len(L[i]))
    total = 0
    mean = sum(str_lengths) / float(len(L))
#    except ZeroDivisionError:
#        return
    for x in str_lengths:
        total += (mean - x)**2
    std = (total / len(L))**0.5
    return std
    

stdDevOfLengths(L)       
        