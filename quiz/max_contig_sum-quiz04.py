# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:44:41 2018

@author: Sandman
"""
L = [3, 4, -8, 15, -1, 2]

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L 
    """
    max = sum(L)
    for i in range(len(L)):
        count = 0
        for j in range(len(L[i:])):
            if count == 0:
                temp_max = sum(L[i:])
            else:
                temp_max = (sum(L[i:count]))
#                print(temp_max)
            count -= 1
            if temp_max > max:
                max = temp_max
#    print(max)
    return max
            
        
        
    
    
    
    
max_contig_sum(L)