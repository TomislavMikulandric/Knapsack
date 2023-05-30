
# Returns the maximum value that
# can be put in a knapsack of
# capacity W

import random
import time

NBR_ITEMS= 5

random.seed(64)

def recursiveKnapSack(W, wt, val, n):

	# Base Case
	if n == 0 or W == 0:
		return 0

	# If weight of the nth item is
	# more than Knapsack of capacity W,
	# then this item cannot be included
	# in the optimal solution
	if (wt[n-1] > W):
		return recursiveKnapSack(W, wt, val, n-1)

	# return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	else:
		return max(
			val[n-1] + recursiveKnapSack(
				W-wt[n-1], wt, val, n-1),
			recursiveKnapSack(W, wt, val, n-1))

def main():
	random.seed(64)
	starting_items = {}
	items = {}
	# Create random items and store them in the items' dictionary.
	for i in range(NBR_ITEMS):
		starting_items[i] = (random.randint(1, 10), random.uniform(0, 100))
	for i in range(NBR_ITEMS*3):
		items[i]= starting_items[i%NBR_ITEMS]

	start_time = time.time()
	W = 50

	values = []
	weights = []
	for i in range(NBR_ITEMS*3):
		values.append(items[i][1])
		weights.append(items[i][0])

	values2 = []
	weights2 = []
	for i in range(NBR_ITEMS):
		values2.append(items[i][1])
		weights2.append(items[i][0])

	print(recursiveKnapSack(W, weights, values, NBR_ITEMS*3))


	print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()  
