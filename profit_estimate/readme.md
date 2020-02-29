The code is implemented based on the problem described [here](https://www.solver.com/monte-carlo-simulation-example)

You are planning to introduce a new product and you need to estimate the first year net profit from this product, which will depend on:
- sales volume in units
- price per unit 
- unit cost
- fixed cost

Net profit will be calculated as: `netProfit = salesVolume * (sellingPrice - unitCost) - fixedCosts`. (note that the sellingPrice is the unitPrice in code.)

Fixed costs (for overhead, advertising, etc) are known to be $ 120, 000.
Other factors involve some **uncertainty**. 

Based on market research, you believe there are equal chances the market will be Slow, OK or Hot. In each scenario the the sellingPrice and the salesVolume are different.

Based on information from the production manager, the unit costs may be anywhere from $5.50 to $7.50, with a most likely cost of $6.50. In this case, the most likely cost is also the average cost.

Try running the simulation mady times, the average net profit will usually be around $92,000 or $93,000. Since we are sampling, whenever we run the simulation (with different seed), there will be different results. Whenever you're sampling, you can't be guaranteed to get perfect accuracy. It's always possible you get a weird sample, that is not to say you can't get exactly the right answer.


