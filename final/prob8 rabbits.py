import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    count = 0
    for rabbit in range(CURRENTRABBITPOP):
        if CURRENTRABBITPOP <= MAXRABBITPOP:
            repro_prob = 1 - (CURRENTRABBITPOP / MAXRABBITPOP)
            if random.random() <= repro_prob:
                count += 1
    CURRENTRABBITPOP += count          
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    count = 0
    for fox in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            eat_prob = CURRENTRABBITPOP / MAXRABBITPOP
            if random.random() <= eat_prob:
                CURRENTRABBITPOP -= 1
                if random.random() <= 1/3:
                    count += 1
            else:
                if random.random() <= 9/10 and CURRENTFOXPOP > 10:
                    count -= 1
    CURRENTFOXPOP += count
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_pop = []
    fox_pop = []
    
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_pop.append(CURRENTRABBITPOP)
        fox_pop.append(CURRENTFOXPOP)


    pylab.plot(rabbit_pop, label = 'Rabbits')
    pylab.plot(fox_pop, label = 'Foxes')
    pylab.xlabel("Time Steps")
    pylab.ylabel("Population")
    pylab.legend(loc = "best")
    coeff = pylab.polyfit(range(len(rabbit_pop)), rabbit_pop, 2)
    pylab.plot(pylab.polyval(coeff, range(len(rabbit_pop))))
    coeff2 = pylab.polyfit(range(len(fox_pop)), fox_pop, 2)
    pylab.plot(pylab.polyval(coeff2, range(len(fox_pop))))
    pylab.show()
    
    return (rabbit_pop, fox_pop)
    
runSimulation(200)

        
        
