# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:47:09 2018

@author: Sandman
"""
import random, pylab

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    mean = []
    for trial in range(numTrials):
        max_count = 1
        temp = []
        for num in range(numRolls):
            r = Die.roll(die)
            temp.append(r)
        count = 1
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1]:
                count += 1
                if count == len(temp):
                    max_count = count            
            else:
                if count > max_count:
                    max_count = count
                count = 1
        mean.append(max_count)
    makeHistogram(mean, 10, 'Number Rolls', 'Mean Longest', title=None)
    return round(sum(mean) / len(mean), 3)
        
            
          
    
# One test case
#print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
print(getAverage(Die([1]), 10, 1000))



