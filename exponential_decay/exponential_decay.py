"""
Monte Carlo simulation example

Used to solve a problem that is not stochastic.
There is no uncertainty about the result.

Concentration of a drug in the human body.

Assume that at each point in time, t, a molecule of the drug has a probability p of being cleared by the body.
The fact that a molecule didn't get cleared at a time t has no impact (doesn't change the probability p) on whether or not the molecule will get cleared at a time t1.

At time t = 1, what is the prob of the molecule still being in the body?
If the probability of being cleared is p, then the prob of not being cleared is 1 - p.

What is the prob of it still being in the body at time t = 2?
(1-p)^2.

In general at time step t, the prob of the molecule being there is
(1 - p)^t.

Suppose at time t = 0, there are n molecules. How many molecules are there likely to be at any time t?

Note that these are exponential decay problems from ODEs. except there, we would have given the
rate at which the moleculues dissolve per unit of time.
"""

from bokeh.plotting import figure, output_file, show
import random

def clear(n, clearProb, steps=[]):
    """
    this is the analytical model (probability)
    """
    numRemaining = [n]
    for t in steps:
        numRemaining.append(n*((1-clearProb)**t))

    return numRemaining

# clear(1000, 0.01, 500)

def clearSimulation(n, clearProb, steps=[]):
    """
    this is the MC simulation
    """
    numRemaining = [n]
    for t in steps:
        molecules = numRemaining[-1]
        # for each molecule, decide wheter it clears or not
        for m in range(0, molecules):
            if random.random() <= clearProb:
                molecules = molecules - 1
        numRemaining.append(molecules)
    return numRemaining

steps = [x for x in range(0, 500)]
clearRes = clear(1000, 0.01, steps)
clearSimRes = clearSimulation(1000, 0.01, steps)
print(clearSimRes)
p = figure()
p.line(x=steps, y=clearRes, color='red', legend='exponential decay')
p.line(x=steps, y=clearSimRes, legend='simulation')
output_file('decay.html')
show(p)
