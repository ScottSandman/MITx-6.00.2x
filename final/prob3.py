# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:37:49 2018

@author: Sandman
"""
import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    same_color = 0
    for i in range(numTrials):
        bucket = ['red', 'red', 'red', 'red', 'green', 'green', 'green', 'green']
        x = random.choice(bucket)
        bucket.remove(x)
        y = random.choice(bucket)
        bucket.remove(y)
        z = random.choice(bucket)
        if x == y == z:
            same_color += 1
    return same_color / float(numTrials)
