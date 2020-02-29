"""
net profit = sales volume * (selling price - unit cost) - fixed cost

fixed cost ... $120 000

sales volume, selling price ... three market scenarios

"""

import random
from decimal import Decimal
import statistics



def profit_analysis(numTrials):
    fixedCost = 120000
    marketScenarios = [
        {'salesVolume': 50000, 'unitPrice': 11}, # slow
        {'salesVolume': 75000, 'unitPrice': 10}, # OK
        {'salesVolume': 100000, 'unitPrice': 8} # hot
    ]

    netProfits = []

    for trial in range(0, numTrials):
        market = random.choice(marketScenarios)
        unitCost = random.triangular(5.5, 7.5, 6.5)
        netProfit = market['salesVolume'] * (market['unitPrice'] - unitCost) - fixedCost
        netProfits.append(netProfit)

    return statistics.mean(netProfits), statistics.stdev(netProfits)


def run_simulation():
    trials = [20, 50, 70, 100, 150, 170, 500, 1000, 10000]

    mean_profits = []
    stdevs = []

    for n in trials:
        mean, stdev = profit_analysis(n)
        mean_profits.append(mean)
        stdevs.append(stdev)

    for i in range(0, len(trials)):

        print(f"Running simulation for {trials[i]} trials, estimated profit: {round(mean_profits[i], 2)}")

run_simulation()
