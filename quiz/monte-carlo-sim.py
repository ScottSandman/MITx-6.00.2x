# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:44:19 2018

@author: Sandman
"""
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns a decimal - the fraction of times 3 
    balls of the same color were drawn.
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
    print(same_color)
    return same_color / numTrials

print(noReplacementSimulation(100000))